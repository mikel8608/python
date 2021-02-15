#!/usr/bin/env python
# Located in: 10.130.0.215/var/www/powerweb-monitor/app/cachecontroller.py

import boto
import boto.ec2.autoscale
import requests
import sys
import xml.etree.ElementTree as ET

import Queue
import threading
import urllib2

from flask import Flask
from flask import request
from flask import Response

import logging
from logging.handlers import RotatingFileHandler

from config import Config

app = Flask(__name__)
app.config["DEBUG"] = True

app.logger.warning("starting up")

RESULT = '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd"><soap:Header><wsa:Action>http://tempuri.org/%sResponse</wsa:Action><wsa:MessageID>urn:uuid:6b012a2a-7a2d-4ab2-bb60-35d9351043cc</wsa:MessageID><wsa:RelatesTo>urn:uuid:458fda54-9516-48f8-8242-f7c83db868ff</wsa:RelatesTo><wsa:To>http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous</wsa:To><wsse:Security><wsu:Timestamp wsu:Id="Timestamp-0cf7c838-136f-455b-95a6-ba016e7c6249"><wsu:Created>2015-03-17T09:11:23Z</wsu:Created><wsu:Expires>2215-03-17T09:16:23Z</wsu:Expires></wsu:Timestamp></wsse:Security></soap:Header><soap:Body><%sResponse xmlns="http://tempuri.org/"><%sResult>true</%sResult></%sResponse></soap:Body></soap:Envelope>'

# get ec2 connections
def get_connections(key, secret, region):
    class Connections:
        pass

    conn = Connections()
    conn.autoscale = boto.ec2.autoscale.connect_to_region(
        region, aws_access_key_id=key, aws_secret_access_key=secret
    )
    conn.ec2 = boto.ec2.connect_to_region(
        region, aws_access_key_id=key, aws_secret_access_key=secret
    )

    return conn


# get ips
def get_ips(conn, asg_names):
    groups = conn.autoscale.get_all_groups(names=asg_names)
    instance_ids = []
    for g in groups:
        for i in g.instances:
            instance_ids.append(i.instance_id)

    ips = []
    reservations = conn.ec2.get_all_instances(instance_ids=instance_ids)
    for reservation in reservations:
        for instance in reservation.instances:
            ips.append(instance.private_ip_address)

    return ips


def do_call(task, ips, hosts, body, *args):
    func = globals()[task["func"]]
    q = Queue.Queue()

    for host in hosts:
        for ip in ips:
            t = threading.Thread(
                target=func, args=(q, task["method"], ip, host, task, body, args)
            )
            t.daemon = True
            t.start()

    reply_total = len(ips) * len(hosts)
    reply_count = 0
    while reply_count < reply_total:
        result = q.get()
        reply_count = reply_count + 1
        if result[1] == 200:
            app.logger.info("%s: %s   -->  OK" % (result[2], result[3]))
        else:
            app.logger.warning(
                "%s: %s   -->  FAILED (%s)" % (result[2], result[3], result[1])
            )


def handle_url(method, url, host, data, timeout=5):
    headers = {
        "Host": host,
    }

    try:
        if method == "get":
            r = requests.get(url, data=data, headers=headers, timeout=timeout)
        else:
            r = requests.post(url, data=data, headers=headers, timeout=timeout)
    except:
        return (False, None, url, host)

    if r.status_code == 200:
        return (True, r.status_code, url, host)

    return (False, r.status_code, url, host)


@app.route("/services/cachecontroller.asmx", methods=["POST"])
@app.route("/services/premierMonitor.asmx", methods=["POST"])
def handle_incoming():
    body = request.get_data()

    tree = ET.fromstring(body)
    command = tree.getchildren()[0].getchildren()[0].tag[21:]
    conn = get_connections(Config.ACCESS_KEY, Config.SECRET_KEY, Config.REGION)
    ips = get_ips(conn, Config.ASG_NAMES)
    app.logger.info("### IPS to Hit: ")
    for x in ips:
        app.logger.info("   - %s" % x)

    app.logger.info("got %s" % command)
    if command in Config.SERVICE_CALLS:
        do_call(
            Config.SERVICE_CALLS[command], ips, Config.PREMIER_HOSTS, body, sys.argv[2:]
        )

    return_msg = RESULT % (command, command, command, command, command)
    app.logger.info(return_msg)

    response = Response(return_msg, mimetype="text/xml")
    response.headers.add("Cache-Control", "private, max-age=0")
    response.headers.add("Vary", "Accept-Encoding")

    return response


def expire_connect(q, method, ip, host, task, body, *args):
    tree = ET.fromstring(body)
    expression = tree.find(task["xml"]).text

    url = "http://%s%s?expression=%s" % (ip, task["uri"], expression)
    data = "."

    q.put(handle_url(method, url, host, data))


def expire_show(q, method, ip, host, task, body, *args):
    tree = ET.fromstring(body)
    show_id = tree.find(task["xml"]).text
    url = "http://%s%s?showID=%s" % (ip, task["uri"], show_id)
    data = "."

    q.put(handle_url(method, url, host, data))


def expire_categories(q, method, ip, host, task, body, *args):
    url = "http://%s%s" % (ip, task["uri"])
    data = "."

    q.put(handle_url(method, url, host, data))


def expire_shows(q, method, ip, host, task, body, *args):
    url = "http://%s%s" % (ip, task["uri"])
    data = "."

    q.put(handle_url(method, url, host, data))


def expire_venues(q, method, ip, host, task, body, *args):
    url = "http://%s%s" % (ip, task["uri"])
    data = "."

    q.put(handle_url(method, url, host, data))


def load_globalsettings(q, method, ip, host, task, body, *args):
    url = "http://%s%s" % (ip, task["uri"])
    data = "."

    q.put(handle_url(method, url, host, data))


if __name__ == "__main__":
    handler = RotatingFileHandler("foo.log", maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0")

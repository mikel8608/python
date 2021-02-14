import os
import sys
'''
  Add new path where you have other code
  This is not the preferred version as you need to do this in all scripts.
    sys.path.append("<add extra paths where you have scripts>")
  Better option is to create a PYTHONPATH variable and asssign the path to this.
'''

def show_all_env_vars():
  for key,value in os.environ.items():
    print (key,value)


def show_key_sys_vars():
  print('USERPROFILE',os.environ['USERPROFILE'])
  print('USERNAME',os.environ['USERNAME'])
  print('WINDIR',os.environ['WINDIR'])
  print('SYSTEMDRIVE',os.environ['SYSTEMDRIVE'])
  print('OS',os.environ['OS'])
  print('PROGRAMFILES',os.environ['PROGRAMFILES'])


#show_all_env_vars()
#show_key_sys_vars()

print('Default Python Version on this System is:',sys.prefix)

'''
  Show all paths used by python.
  List 1st: path where script is running
  List 2nd: paths in the O.S. environment variable
  List 3rd: standard library paths
  List 4th: site packages, 3rd party directories
'''
print('Show System Path:',sys.path)
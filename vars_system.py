import os

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
show_key_sys_vars()
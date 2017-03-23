from fabric.api import *

env.user = 'ec2-user'
env.key_filename = '~/Downloads/awscert.pem'
env.password = 'abcd1234'

def host_type():
    run('uname -s')

def host_load():
    run('uptime')

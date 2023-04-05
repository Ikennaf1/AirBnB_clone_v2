#!/usr/bin/python3
""" Deploys using fabric """
from fabric.api import *


env.hosts = ['52.87.230.189', '18.234.80.136']
env.user = "ubuntu"


def do_clean(number=0):
    """
    Cleans up
    """

    num = int(number)

    if num == 0:
        num = 2
    else:
        num += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(num))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, num))

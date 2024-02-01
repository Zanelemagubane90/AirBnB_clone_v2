#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""

from fabric.api import *

env.hosts = env.hosts = ['34.205.65.89', '100.26.162.105']   # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username

def do_clean(number=0):
    """Delete out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

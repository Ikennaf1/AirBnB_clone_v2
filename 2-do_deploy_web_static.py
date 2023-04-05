#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os import path


env.hosts = ['52.87.230.189', '18.234.80.136']


def do_pack():
    """
    The do_pack function to be used
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))


def do_deploy(tgz_path):
    """
    A Fabric script that distributes an archive to your web servers
    """

    if path.exists(tgz_path):
        archive = tgz_path.split('/')[1]
        t_path = "/tmp/{}".format(archive)
        directory = archive.split('.')[0]
        d_path = "/data/web_static/releases/{}/".format(directory)

        put(tgz_path, t_path)
        run("mkdir -p {}".format(d_path))
        run("tar -xzf {} -C {}".format(t_path, d_path))
        run("rm {}".format(t_path))
        run("mv -f {}web_static/* {}".format(d_path, d_path))
        run("rm -rf {}web_static".format(d_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(d_path))

        return True

    return False

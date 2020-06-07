import fabric
import os
import os.path
import glob
import zipfile
import fnmatch
import tempfile
import traceback
import time

import xml.dom.minidom

from xml.etree.ElementTree import ElementTree

from fabric.api import env, cd, run, local, get, put, settings, sudo, task, runs_once, execute

env.user = 'xxx'
env.password = 'xxxx'
env.sudo_password = 'xxxxxx'

env.roledefs = {}


def jar_mkdir_service(module, source):
    command1 = 'cd /data'
    # os.system(command1)
    dest_file = os.path.basename(source)
    with cd("/data"):
        run("mkdir %s" % module)
        # cd("/%s" % module)
    with open(source, 'rb') as source_file:
        run("pwd")
        try:
            put(source_file, "/data/%s/%s" % (module,dest_file))
        except e:
            traceback.print_exc()
            raise e
    # command2=f'put(source, "/data/%s" % {module})'
    # run(f'sudo {command2}')
    # with open(source, 'rb') as source_file:
    #     try:
    #         put(source_file, '/%s%s' % (module,))
    #     except Exception, e:
    #         traceback.print_exc()
    #         raise e

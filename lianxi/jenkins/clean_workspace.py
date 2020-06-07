import os
import shutil
import logging

from jenkinsapi.jenkins import Jenkins

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__file__)


def get_jenkins_instance():
    jenkins_url = "http://192.168.1.103:22"
    jenkins_username = "xx"
    jenkins_password = "xx"
    print(Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password))
    print(os.walk('/home/rongyi/.jenkins/workspace'))
    return Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)



get_jenkins_instance()
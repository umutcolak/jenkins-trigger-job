#!/usr/bin/env python3

# use of https://python-jenkins.readthedocs.io/en/latest/index.html

import sys
import jenkins
import json


def mandatory_arg(argv):
    if argv == "":
        raise ValueError("Only job_params can be empty. Required fields: url, token, user and path")
    return argv


# mandatory
JENKINS_URL = mandatory_arg(sys.argv[1])
JENKINS_TOKEN = mandatory_arg(sys.argv[2])
JENKINS_USER = mandatory_arg(sys.argv[3])
JOB_PATH = mandatory_arg(sys.argv[4])

# not mandatory
JOB_PARAMS = sys.argv[5]

# This code specific for our project
JOB_PARAMS = JOB_PARAMS.replace("refs/heads/", "")

# create/connect jenkins server
server = jenkins.Jenkins(url=JENKINS_URL, username=JENKINS_USER, password=JENKINS_TOKEN)

# build job
server.build_job(JOB_PATH, parameters=json.loads(JOB_PARAMS), token=JENKINS_TOKEN)

#!/usr/bin/env python

import sys

from cubeadev.docker_conn import exec_docker

if exec_docker(['exec', 'flower_1']+sys.argv[1:], shell=False):
    sys.exit(1)

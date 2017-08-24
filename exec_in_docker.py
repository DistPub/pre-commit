#!/usr/bin/env python

import sys

from cubeadev.docker_conn import exec_docker

if exec_docker(sys.argv[1:]):
    sys.exit(1)

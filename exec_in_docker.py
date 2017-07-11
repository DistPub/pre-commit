#!/usr/bin/env python

import sys

from dockconn import exec_docker, DEFAULT_CONTAINER_NAME

if exec_docker('exec {} {}'.format(DEFAULT_CONTAINER_NAME, ' '.join(sys.argv[1:]))):
    sys.exit(1)

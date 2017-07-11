# !python

import sys

from dockconn import exec_docker, DEFAULT_CONTAINER_NAME

exec_docker('exec {} {}'.format(DEFAULT_CONTAINER_NAME, ' '.join(sys.argv[1:])))

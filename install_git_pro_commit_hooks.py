#!/usr/bin/env python

import os
import sys

if len(sys.argv) == 1:
    raise SystemExit('[ERROR]: Require working-space directory!')
os.chdir(sys.argv[1])
os.system('pre-commit install')

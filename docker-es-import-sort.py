#!/usr/bin/env python
import sys

from cubeadev.docker_conn import exec_docker

results = []
for fp in sys.argv[1:]:
    with open(fp) as f:
        lines = [line.strip() for line in f]
    if '/* eslint sort-imports:0 */' in lines:
        continue
    results.append(exec_docker(['exec', 'flower_1', 'import-sort', '-o']+[fp]))
if any(results):
    sys.exit(1)

#!/bin/bash
for i in $@ ; do
    skip_file=0
    while read line; do
        if [[ $line = '/* eslint sort-imports:0 */' ]]; then
            skip_file=1
            break
        fi
    done < $i;
    if [[ $skip_file = 1 ]]; then
        continue
    fi
    exec_in_docker.py import-sort -o $i
done;

# require
* running dockerlize omms env
* cubeadev

# pre-commit
本项目是git pre-commit钩子的 repo，有以下几种钩子：
* docker-pylint
* docker-eslint
* docker-es-import-sort
* docker-stylelint
* docker-python-isort
* python-isort
* python-pylint

# 使用说明
1. 本地工作区安装pre-commit到.git
2. 在working-space-dir即项目根目录添加.pre-commit-config.yaml文件来配置使用的钩子
3. 若想对某些js文件跳过es-import-sort更改，可以使用/* eslint sort-imports:0 */来跳过该文件。

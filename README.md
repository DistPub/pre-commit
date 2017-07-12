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
1. 脚本install_git_pro_commit_hooks.py working-space-dir来安装钩子
2. 在working-space-dir即项目根目录添加.pre-commit-config.yaml文件来配置使用的钩子
import os
import platform

DEFAULT_WIN7_BASE_URL = "tcp://192.168.99.100:2376"
DEFAULT_WIN7_TLS_HOME = r"{}\\.docker\\machine\\machines\\default\\".format(
    os.environ.get('USERPROFILE').replace('\\', '\\\\')
)
DEFAULT_CONTAINER_NAME = 'web_server_1'

def exec_in_win7_docker(cmd):
    return os.system(
        'docker -H {url} --tls --tlscert {tls_home}cert.pem --tlskey {tls_home}key.pem {cmd}'.format(
        url=DEFAULT_WIN7_BASE_URL,
        tls_home=DEFAULT_WIN7_TLS_HOME,
        cmd=cmd,
        )
    )

def exec_in_win10_docker(cmd):
    return os.system('docker {}'.format(cmd))

def exec_in_unix_docker(cmd):
    return os.system('docker {}'.format(cmd))

if platform.system() == 'Windows':
    if platform.release() == '10':
        exec_docker = exec_in_win10_docker
    else:
        exec_docker = exec_in_win7_docker
else:
    exec_docker = exec_in_unix_docker


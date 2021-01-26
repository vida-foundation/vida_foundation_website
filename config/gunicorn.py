from pathlib import Path

bind = 'unix:/tmp/nginx.socket'
backlog = 2048
workers = 2

def pre_fork(server, worker):
    Path('/tmp/app-initialized').touch()

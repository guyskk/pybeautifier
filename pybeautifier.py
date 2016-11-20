import os
import subprocess
import sys

import pybeautifier_server

server = os.path.join(os.path.dirname(__file__), 'pybeautifier_server.py')


def daemon():
    subprocess.Popen(
        ['python', server, '-d'],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def main():
    IS_DAEMON = len(sys.argv) > 1 and sys.argv[1] == '-d'
    if IS_DAEMON:
        daemon()
    else:
        pybeautifier_server.main()


if __name__ == '__main__':
    main()

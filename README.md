# PyBeautifier

Python beautifier tcp server based on autopep8, yapf, isort.  
Only suport Unix-like system and python3.3+ currently.

## Why

Before this, I use [atom-beautify](https://github.com/Glavin001/atom-beautify) to format my code, but it's too slow(about 3 seconds) because every format operation will create a new python process.

So I write the beautifier server in python and beautifier client in node.js, they communicate by tcp socket. It's performance is much better(about 300 ms).

## Install

    $ pip install pybeautifier

Besides, you should install one or more of autopep8, yapf, isort based on your needs.

## Usage

    $ pybeautifier       # front ground process
    $ pybeautifier -d    # daemon process, logging to /tmp/pybeautifier.log

It will listening tcp://<HOST>:<PORT>.

Env variables:
BEAUTIFIER_HOST - IP address or hostname (Default: 127.0.0.1)
BEAUTIFIER_PORT - Port number (Default: 36805)

Start at boot via systemd(Ubuntu16 or Arch Linux):

    $ wget https://raw.githubusercontent.com/guyskk/pybeautifier/master/pybeautifier.service
    $ cp pybeautifier.service /usr/lib/systemd/system/
    $ systemctl start pybeautifier
    $ systemctl enable pybeautifier

## Protocol

Request(JSON):

    {
        'data': 'text_need_format',
        'formaters': [
            {
                'name': 'formater_name',
                'config': {}  # None or dict
            },
            ... # formaters
        ]
    }

Response(JSON):

    {
        'error': 'error message',
        'data': 'formated text'
    }

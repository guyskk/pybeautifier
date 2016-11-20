# PyBeautifier

Python beautifier tcp server based on autopep8, yapf, isort.  
Only suport python3.3+ currently.

## Why

Before this, I use atom-beautify to format my code, but it's too slow(about 3 seconds) because every format operation will create a new python process.

So I write the beautifier server in python and beautifier client in node.js, they communicate by tcp socket. It's performance is much better(about 300 ms).

The client not merged yet.  
See also: https://github.com/guyskk/atom-beautify

## Install

    $ pip install pybeautifier

Besides, you should install one or more of autopep8, yapf, isort based on your needs.

## Usage

    $ pybeautifier       # front ground process
    $ pybeautifier -d    # daemon process, logging to /tmp/pybeautifier-xx.log

It will listening tcp://127.0.0.1:36805

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

import json
import logging
import os
import socket
import sys
import tempfile

try:
    from autopep8 import fix_code

    def autopep8(x, ignore=None, max_line_length=79):
        return fix_code(x, options={
            'ignore': ignore,
            'max_line_length': max_line_length
        })
except:
    autopep8 = None
try:
    from yapf.yapflib.yapf_api import FormatCode

    def yapf(x, style_config=None):
        return FormatCode(x, style_config=style_config)[0]
except:
    yapf = None
try:
    from isort import SortImports

    def isort(x, multi_line_output=None):
        return SortImports(
            file_contents=x,
            multi_line_output=multi_line_output
        ).output
except:
    isort = None

IS_DAEMON = len(sys.argv) > 1 and sys.argv[1] == '-d'
FORMATERS = {
    'yapf': yapf,
    'autopep8': autopep8,
    'isort': isort
}
ADDRESS = ('127.0.0.1', 36805)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# prevent port can’t be immediately reused
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


def setup_logging():
    format = '[%(levelname)-5s %(asctime)s] %(message)s'
    if IS_DAEMON:
        logfile = tempfile.NamedTemporaryFile(
            mode='w', suffix='.log', prefix='python-beautifier-'
        )
        logging.basicConfig(
            stream=logfile, filemode='w', format=format, level=logging.INFO
        )
    else:
        logging.basicConfig(format=format, level=logging.DEBUG)
    logging.info('PID is %d' % os.getpid())
    logging.info('Listening tcp://%s:%s' % ADDRESS)


def send(client, error, data):
    response = {'error': error, 'data': data}
    response = json.dumps(response, ensure_ascii=False)
    logging.debug('response size: %s' % len(response))
    client.sendall(response.encode('utf-8'))


def handle(client, request):
    """
    Handle format request

    request struct:

        {
            'data': 'data_need_format',
            'formaters': [
                {
                    'name': 'formater_name',
                    'config': {}  # None or dict
                },
                ... # formaters
            ]
        }

    if no formaters, use autopep8 formater and it's default config
    """
    formaters = request.get('formaters', None)
    if not formaters:
        formaters = [{'name': 'autopep8'}]
    logging.debug('formaters: ' + json.dumps(formaters, indent=4))
    data = request.get('data', None)
    if not isinstance(data, str):
        return send(client, 'invalid data', None)
    for formater in formaters:
        name = formater.get('name', None)
        config = formater.get('config', {})
        if name not in FORMATERS:
            return send(client, 'formater {} not support'.format(name), None)
        formater = FORMATERS[name]
        if formater is None:
            return send(client, 'formater {} not installed'.format(name), None)
        data = formater(data, **config)
    return send(client, None, data)


def main():
    try:
        server.bind(ADDRESS)
        server.listen(1)
        setup_logging()
        while True:
            client, addr = server.accept()
            try:
                request = client.recv(1024 * 1024).decode('utf-8')
                logging.debug('request size: %s' % len(request))
                if request:
                    handle(client, json.loads(request))
            except KeyboardInterrupt:
                break
            except Exception as ex:
                try:
                    send(client, repr(ex), None)
                except:
                    pass
                logging.exception(ex)
            finally:
                client.close()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()


if __name__ == '__main__':
    main()

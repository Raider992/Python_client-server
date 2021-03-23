from socket import *
import click
import time
import json
import logging
import utils.log.client_log_config
from utils.log_decorator import Trace

@Trace()
def form_auth_message():
    t = int(time.time())
    data = {
        'action': 'authenticate',
        'time': t,
        'user': {
            'account_name': 'user',
            'account_password': 'P@ssw0rd'
        }
    }
    return json.dumps(data)

@Trace()
def form_presence_message():
    t = int(time.time())
    data = {
        'action': 'presence',
        'time': t,
        'type': 'status',
        'user': {
            'account_name': 'user',
            'account_password': 'P@ssw0rd'
        }
    }
    return json.dumps(data)


@click.command()
@click.option('-port', default=7777, )
@click.option('-addr', default='localhost', help="host's address, default=localhost")
@Trace()
def client_function(port, addr):
    clt_log = logging.getLogger('client_log')

    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect((addr, port))
        except Exception as e:
            clt_log.exception(str(e))
        clt_log.debug('Соединение с сервером установлено')
        msg = form_auth_message()
        clt_log.debug('Сформировано сообщение аутентификации')
        try:
            s.send(msg.encode('utf-8'))
            clt_log.debug('Сообщение аутентификации отправлено на сервер')
        except Exception as e:
            clt_log.exception(str(e))
        try:
            data = s.recv(1000000)
            clt_log.debug('Получен ответ от сервера')
        except Exception as e:
            clt_log.exception(str(e))
        data = json.loads(data)
        if data['response'] == 200:
            msg2 = form_presence_message()
            clt_log.debug('Сформировано сообщение присутствия')
            try:
                s.send(msg2.encode('utf-8'))
                clt_log.debug('Сообщение присутствия отправлено на сервер')
            except Exception as e:
                clt_log.exception(str(e))
        else:
            clt_log.exception('неверный статус ответа')


if __name__ == '__main__':
    client_function()

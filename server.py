# Формат команды: py server.py <port> <addr>

from socket import *
import click
import json
import logging
import utils.log.server_log_config
from utils.log_decorator import Trace

srv_log = logging.getLogger('server_log')

@Trace()
def form_auth_resp():
    msg = {
        'response': 200,
        'alert': 'auth success'
    }
    return json.dumps(msg)


@click.command()
@click.option('-port', default=7777, help='enter port, default=7777')
@click.option('-addr', default='', help='ip address to listen to, default - all addresses')
def run_server(port, addr):
    srv_log = logging.getLogger('server_log')
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.bind((addr, port))
            s.listen()
        except Exception as e:
            srv_log.exception(str(e))
        srv_log.debug(f'server listening at port {port}')

        while True:
            srv_log.debug('Сервер запущен')
            try:
                client, addr = s.accept()
                srv_log.debug('Соединение установлено')
            except Exception as e:
                srv_log.exception(str(e))
            data = client.recv(1000000)
            srv_log.debug('Данные получены')
            data = data.decode('utf-8')
            data = json.loads(data)
            if data['action'] == 'authenticate':
                msg = form_auth_resp()
                srv_log.debug('Ответ сформирован')
                try:
                    client.send(msg.encode('utf-8'))
                    srv_log.debug('Ответ отправлен клиенту')
                except Exception as e:
                    srv_log.exception(str(e))
            data2 = client.recv(1000000)
            srv_log.debug('presence-сообщение получено')
            data2 = data2.decode('utf-8')
            data2 = json.loads(data2)
            client.close()
            srv_log.debug('соединение остановлено')

if __name__ == '__main__':
    run_server()

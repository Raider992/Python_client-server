# Формат команды: py server.py <port> <addr>

from socket import *
import click
import json
import logging
from select import select

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


@Trace()
def read_requests(r_clients, all_clients):
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            data = json.loads(data)
            if data['action'] == 'chat':
                responses[sock] = json.dumps(data['contents'])
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


@Trace()
def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                for clt in w_clients:
                    if not clt == sock:
                        clt.send(resp)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


@Trace()
def read_auth_requests(r_clients):
    auth_responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            data = json.loads(data)
            if data['action'] == 'authenticate':
                auth_responses[sock] = form_auth_resp()
        except Exception as e:
            srv_log.exception(str(e))

    return auth_responses


@Trace()
def write_auth_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                sock.send(resp)
            except Exception as e:
                srv_log.exception(str(e))
        else:
            srv_log.exception('Unauthorised client')
            all_clients.remove(sock)
    return all_clients


@click.command()
@click.option('-port', default=7777, help='enter port, default=7777')
@click.option('-addr', default='', help='ip address to listen to, default - all addresses')
def run_server(port, addr):
    srv_log = logging.getLogger('server_log')
    clients = []

    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.bind((addr, port))
            s.listen(5)
            s.settimeout(0.2)
        except Exception as e:
            srv_log.exception(str(e))
        srv_log.debug(f'server listening at port {port}')

        while True:
            srv_log.debug('Сервер запущен')
            try:
                client, addr = s.accept()
            except Exception as e:
                srv_log.exception(str(e))
            else:
                print("Получен запрос на соединение с %s" % str(addr))
                clients.append(client)
            finally:
                wait = 10
                r = []
                w = []
                e = []
                try:
                    r, w, e = select(clients, clients, [], wait)
                except Exception as err:
                    srv_log.exception(str(err))

                auth_requests = read_auth_requests(r)
                if auth_requests:
                    clients = write_auth_responses(auth_requests, w, clients)

                requests = read_requests(r, clients)
                if requests:
                    write_responses(requests, w, clients)

            # data2 = client.recv(1000000)
            # srv_log.debug('presence-сообщение получено')
            # data2 = data2.decode('utf-8')
            # data2 = json.loads(data2)
            # client.close()
            # srv_log.debug('соединение остановлено')


if __name__ == '__main__':
    run_server()

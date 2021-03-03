from socket import *
import click
import time
import json


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
def client_function(port, addr):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((addr, port))
        msg = form_auth_message()
        s.send(msg.encode('utf-8'))
        data = s.recv(1000000)
        data = json.loads(data)
        if data['response'] == 200:
            msg2 = form_presence_message()
            s.send(msg2.encode('utf-8'))


if __name__ == '__main__':
    client_function()

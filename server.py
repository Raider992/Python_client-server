# Формат команды: py server.py <port> <addr>

from socket import *
import click
import json


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
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((addr, port))
        s.listen()

        while True:
            client, addr = s.accept()
            data = client.recv(1000000)
            data = data.decode('utf-8')
            data = json.loads(data)
            if data['action'] == 'authenticate':
                msg = form_auth_resp()
                client.send(msg.encode('utf-8'))
            data2 = client.recv(1000000)
            data2 = data2.decode('utf-8')
            data2 = json.loads(data2)
            print(data2)
            client.close()

if __name__ == '__main__':
    run_server()

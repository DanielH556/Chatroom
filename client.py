import socket
from threading import Thread
import os

def recebe_mensagens(socket_, username):
    while True:
        msg=socket_.recv(1024)
        if msg:
            print('\r{}\n{}: '.format(msg.decode('utf-8'), username), end = '')
        else:
            print('\nConexão perdida com o servidor!')
            print('\nSaindo...')
            socket_.close()
            os._exit(0)

def envia_mensagens(socket_, username):
    while True:
        msg = input('{}: '.format(username))
        if msg.lower() == "fim":
            socket_.sendall('Servidor >>> {} saiu da sala.'.format(username).encode('utf-8'))
            break
        else:
            socket_.sendall('{}: {}'.format(username, msg).encode('utf-8'))
    print("Envio de mensagens encerrado!")
    socket_.close()
    os._exit(0)

def client(h, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((h, p))

    username = input('Insira seu nome de usuário: ')

    envia=Thread(target=envia_mensagens,args=(s, username))
    recebe = Thread(target=recebe_mensagens, args=(s, username))

    envia.start()
    recebe.start()

    s.sendall('Servidor >>> {} entrou na sala.'.format(username).encode('utf-8'))
    print("Online")
    print('{}: '.format(username), end = '')

Client = Thread(target = client, args =(socket.gethostname(), 1234))
Client.start()
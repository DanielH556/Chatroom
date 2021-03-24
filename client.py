import socket
import threading
import os

class Enviar(threading.Thread):
    def __init__(self, socket_, nome):
        super().__init__()
        self.socket_ = socket_
        self.nome = nome
    
    def run(self):
      while True:
        msg = input('{}: '.format(self.nome))
        if msg.lower() == "fim":
            self.socket_.sendall('Servidor >>> {} saiu da sala.'.format(self.nome).encode('utf8'))
            break
        else:
            self.socket_.sendall('{}: {}'.format(self.nome, msg).encode('utf8'))
        print('\nSaindo...')
        self.socket_.close()
        os._exit(0)

class Recebe(threading.Thread):
    def __init__(self, socket_, nome):
        super().__init__()
        self.socket_ = socket_
        self.nome = nome
    
    def run(self):  
        while True:
            msg = self.socket_.recv(1024)
            if msg:
                print('\r{}\n{}: '.format(msg.decode('ascii'), self.nome), end = '')
            else:
                print('\nConexão com o servidor perdida.')
                print('\nSaindo...')
                self.socket_.close()
                os._exit(0)


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print('Tentando se conectar à {}:{}'.format(self.host, self.port))
        self.s.connect((self.host, self.port))
        print('Conexão com {} feita com sucesso'.format(self.host, self.port))

        nome = input('Insira seu usuário: ')

        envia = Enviar(self.s, nome)
        recebe = Recebe(self.s, nome)

        envia.start()
        recebe.start()

        self.s.sendall('Servidor >>> {} entrou na sala.'.format(nome).encode('ascii'))
        print('{}: '.format(nome), end = '')

client = Client(socket.gethostname(), 1234)
client.start()
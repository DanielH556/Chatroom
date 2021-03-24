import socket
import threading
import os

class Servidor(threading.Thread):
    def __init__(self, host, port): # Método construtor
        super().__init__()
        self.host = host
        self.port = port
        self.conexoes = []
    
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)

        while True:
            sc, socketNome = s.accept()
            print('Conexão aceita de {} para {}'.format(sc.getpeername(), sc.getsockname()))

            serverSocket = SocketServer(sc, socketNome, self)
            serverSocket.start()

            self.conexoes.append(serverSocket)
            print('Pronto para receber mensagens de', sc.getpeername)

    def broadcast(self, msg, src):
        for conexao in self.conexoes:
            if conexao.socketNome != src:
                conexao.send(msg)

class SocketServer(threading.Thread):
    def __init__(self, sc, socketNome, servidor):
        super().__init__()
        self.sc = sc
        self.socketNome = socketNome
        self.servidor = servidor

    def run(self):
        while True:
            msg = self.sc.recv(1024).decode('ascii')
            if msg:
                print('{} disse {!r}'.format(self.socketNome, msg))
                self.servidor.broadcast(msg, self.socketNome)
            else:
                print('{} encerrou a conexão'.format(self.socketNome))
                self.sc.close()
                servidor.remove_connection()
                return

    def send(self, msg):
        self.sc.sendall(msg.encode('ascii'))
    
    def exit(servidor):
        while True:
            ipt = input('')
            if ipt == 'q':
                print('Encerrando todas as conexões...')
                for conexao in servidor.conexoes:
                    conexao.sc.close()
                print('Desligando o servidor')
                os._exit(0)

if __name__ == '__main__':
    servidor = Servidor('', 1234)
    servidor.start()

    sair = threading.Thread(target = exit, args = (servidor, ))
    sair.start()
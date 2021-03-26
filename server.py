import socket
import threading
import os

class Servidor(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.L = []

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port))
        s.listen(5)

        while True:
            clientsocket, address = s.accept()
            print('Conexão com {} foi estabelecida'.format(clientsocket.getpeername()))

            serverSocket = ServerSocket(clientsocket, address, self)
            serverSocket.start()

            self.L.append(serverSocket)
            print('Pronto para receber mensagens de {}'.format(address))

    def transmissao(self, msg, src):
        for connection in self.L:
            if connection.socket_ != src:
                connection.enviarMsg(msg)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=

class ServerSocket(threading.Thread):
    def __init__(self, sc, socket_, servidor):
        super().__init__()
        self.sc = sc
        self.socket_ = socket_
        self.servidor = servidor

    def run(self):
      while True:
        msg = self.sc.recv(1024).decode('utf-8')
        if msg:
            print('{} -> {}'.format(self.socket_, msg))
            self.servidor.transmissao(msg, self.socket_)
        else:
            print('{} encerrou a conexão'.format(self.socket_))
            self.sc.close()
            return

    def enviarMsg(self, msg):
        self.sc.sendall(msg.encode('utf-8'))
    
    def sair(servidor):
        while True:
            ipt = input('')
            if ipt == 'close':
                print('Encerrando todas as conexões...')
                for c in servidor.L:
                    c.sc.close()
                print('Desligando o servidor...')
                os._exit(0)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=        
        
if __name__ == '__main__':
    server = Servidor(socket.gethostname(), 1234)
    server.start()
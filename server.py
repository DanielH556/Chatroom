import socket
import threading
import os

# Foi necessário a criação de duas classes: uma para a criação e configuração do servidor (classe Servidor) e outra para a criação e configuração do Socket do servidor (classe ServerSocket).
class Servidor(threading.Thread):
    # Método construtor da classe Servidor. Nela cria-se e instancia-se as variáveis "host", "port" e o array "L" que armazenará os usuários que estiverem na sala.
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.L = []
        self.isClicked = False

    # Função que configura o servidor e é a função chamada quando a classe é instanciada
    def run(self):
        # Configuração do servidor
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((self.host, self.port)) # Linha em que é atribuído o endereço e a porta do host para o servidor.
        s.listen(5) # Comando que possibilita que o servidor aceite novos usuários na sala

        while True:
            # Criação e armazenamento do servidor aceitando o socket do cliente e o seu endereço, armazenando-o na lista "L"
            clientsocket, address = s.accept()
            print('[SERVIDOR] Conexão com {} foi estabelecida'.format(clientsocket.getpeername()))
            if self.isClicked == True:
                with open('test.txt', "wb") as f:
                    print("[+] Receiving...")
                    while True:
                        data = f.read()
                        if not data:
                            print("[+] No data was read")
                            break
                        print("[+] Recebendo...")
                        f.write(data)
                        print("[+] Escrito no arquivo")
                        clientsocket.sendall(data)
                        
                    f.close()
                    print("[+] Download Completo")
                    self.isClicked = False

            serverSocket = ServerSocket(clientsocket, address, self) # Instância da classe "ServerSocket" para definir a conexão do socket do cliente e o endereço ao servidor
            serverSocket.start()

            self.L.append(serverSocket)
            print('[SERVIDOR] Pronto para receber mensagens de {}'.format(address))

    # Função responsável pelo encaminhamento de uma mensagem ao servidor e os outros clientes
    def transmissao(self, msg, src):
        for connection in self.L:
            #if connection.socket_ != src:
            connection.enviarMsg(msg)


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=

class ServerSocket(threading.Thread):
    # Método construtor da classe ServerSocket, criando e instanciando as variáveis "sc" (socket do cliente), "socket_" (endereço) e "servidor" (a classe Servidor)
    def __init__(self, sc, socket_, servidor):
        super().__init__()
        self.sc = sc
        self.socket_ = socket_
        self.servidor = servidor

    def run(self):
      while True:
        # Variável que recebe a mensagem do cliente, decodificando-a de bits para UTF-8
        msg = self.sc.recv(1024).decode('utf-8')
        if msg:
            print('{} -> {}'.format(self.socket_, msg)) # Imprime a mensagem recebida
            self.servidor.transmissao(msg, self.socket_) # Executa a função "transmissao" com a variável "msg"
        else:
            print('[SERVIDOR] {} encerrou a conexão'.format(self.socket_))
            self.sc.close()
            return

    # Função responsável por enviar a mensagem recebida para os outros clientes
    def enviarMsg(self, msg):
        self.sc.sendall(msg.encode('utf-8'))
    
    # Função responsável por fechar o servidor ao administrador digitar "close" no servidor (não está implementada a princípio)
    def sair(servidor):
        while True:
            ipt = input('')
            if ipt == 'close':
                print('Encerrando todas as conexões...')
                for c in servidor.L: # Encerra a conexão com os clientes que estão no array, ou seja, clientes conectados
                    c.sc.close()
                print('Desligando o servidor...')
                os._exit(0)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=        
# Esse "if" faz o papel do método main do java. Neste caso, está basicamente instanciando e iniciando a classe Servidor como uma Thread (definida nos parâmetros da classe - class Servidor(threading.Thread))  
if __name__ == '__main__':
    # os parâmetros do servidor está sendo colocado o endereço do host (nome do host) e a porta (1234)
    server = Servidor(socket.gethostname(), 1234)
    server.start()

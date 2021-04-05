import socket
from threading import Thread
import os

# Função responsável por receber mensagens do servidor
def recebe_mensagens(socket_, username):
        # Loop infinito para sempre estar recebendo as mensagens enquanto a conexão com o servidor estiver feita
    while True:
        msg=socket_.recv(1024) # variável que recebe a mensagem do servidor (1)

        # Condicional que verifica se a conexão ainda está feita com o servidor. ("if msg" e "if msg == True" é a mesma coisa)
        if msg:
            # Imprime a mensagem (2)
            print('\r{}\n{}: '.format(msg.decode('utf-8'), username), end = '')
        else:
            print('\nConexão perdida com o servidor!')
            print('\nSaindo...')
            socket_.close() # Fecha a conexão pendente
            os._exit(0) # Fecha o sistema

# Função responsável por enviar mensagens ao servidor
def envia_mensagens(socket_, username):
    while True:
        msg = input('{}: '.format(username)) # input para o usuário digitar a mensagem

        # Se o usuário enviar uma mensagem dizendo "fim", o usuário sai da sala.
        if msg.lower() == "fim":
            socket_.sendall('Servidor >>> {} saiu da sala.'.format(username).encode('utf-8'))
            break
        else:
            socket_.sendall('{}: {}'.format(username, msg).encode('utf-8')) # (3)
    print("Envio de mensagens encerrado!")
    socket_.close()
    os._exit(0)

# Função geral do client-side
def client(h, p):
    # Variável que representa a conexão com o servidor
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Configuração da conexão com o servidor
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((h, p))

    username = input('Insira seu nome de usuário: ') # Variável que armazena o nome do usuário

    # Execução dos métodos de envio e recepção de mensagens por meio de Threads (4)
    envia=Thread(target=envia_mensagens,args=(s, username))
    recebe = Thread(target=recebe_mensagens, args=(s, username))

    # Gatilho para iniciar os métodos de envio e recepção
    envia.start()
    recebe.start()

    # Feedback de quem entrou na sala
    s.sendall('Servidor >>> {} entrou na sala.'.format(username).encode('utf-8'))
    print("Online")
    print('{}: '.format(username), end = '')

Client = Thread(target = client, args =(socket.gethostname(), 1234))
Client.start()
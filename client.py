import socket
from threading import Thread
import time

def recebe_mensagens(socket_):
    while True:
        msg=socket_.recv(1024)
        if not (len(msg)):
            break
        print(msg.decode("utf-8"))
        print("Conexão com o servidor encerrada")

def envia_mensagens(socket_):
    while True:
        msg = input("mensagem: ")
        socket_.send(bytes(msg, "utf-8"))
        if msg.lower() == "fim":
            socket_.close()
            break
        print("Envio de mensagens encerrado!")

def client(h,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    envia=Thread(target=envia_mensagens,args=(s,))
    recebe = Thread(target=recebe_mensagens, args=(s,))

    envia.start()
    recebe.start()


    print("Programa encerrado")

    while True:
        try:
            s.connect((h, p))
            break
        except Exception as e:
            pass
    print("Online")



client(socket.gethostname(), 1234)

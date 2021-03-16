import socket
from threading import Thread

L=[]
def ConversaSimultanea(a,b):
    msg = ""
    while msg != "Fim":
        print ("entrou no loop da conversa")
        msg = L[a].recv(5000)
        if not msg:
            break
        L[b].sendall(msg)
    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 1234))
s.listen(5)

for i in range(2):
    clientsocket, address = s.accept()
    print(f"Conexão com {address} foi estabelecida!")
    L.append(clientsocket)
    clientsocket.send(bytes("Bem vindo ao servidor", "utf-8"))
t1=Thread(target=ConversaSimultanea,args=(1,0)).start()
t2=Thread(target=ConversaSimultanea,args=(0,1)).start()

while True:
    recebe=clientsocket.recv(1024)
    print(recebe)
print("fim de transmissao")



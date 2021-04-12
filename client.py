import socket
from threading import Thread
import os
import main
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *




# Função responsável por enviar mensagens ao servidor
def envia_mensagens(event=None):
    #while True:
    msg = messageInp.get()
    messageInp.delete(0, END) # Limpa o campo de texto

    # Se o usuário enviar uma mensagem dizendo "fim", o usuário sai da sala.
    if msg.lower() == "fim":
        s.sendall('Servidor >>> {} saiu da sala.'.format(username).encode('utf-8'))
    else:
        s.sendall('{}: {}'.format(username, msg).encode('utf-8')) # (3)




# Função responsável por receber mensagens do servidor
def recebe_mensagens():
        # Loop infinito para sempre estar recebendo as mensagens enquanto a conexão com o servidor estiver feita
    while True:
        msg=s.recv(1024).decode('utf-8') # variável que recebe a mensagem do servidor (1)

        # Condicional que verifica se a conexão ainda está feita com o servidor. ("if msg" e "if msg == True" é a mesma coisa)
        if msg:
            # Imprime a mensagem (2)
            chatBoxCont.insert(tk.END, msg)
        else:
            print('\nConexão perdida com o servidor!')
            print('\nSaindo...')
            s.close() # Fecha a conexão pendente
            os._exit(0) # Fecha o sistema




root = tk.Tk() # inicia a janela principal
root.title("Chatbox") # Título da janela
root.geometry("1280x720") # Tamanho da janela
root.resizable(False, False) # Impede que a janela seja redimensionada pelo usuário

#-----------------------------------------------------------------------------------------------------

# Lista de usuários da esquerda
# master = root | faz com que o frame "chatList" seja inserido na janela geral, e não dentro de outro frame aleatório onde não deveria estar
chatList = tk.Frame(master=root, width = 300, bg = "#156950")

# fill=tk.Y --> preenche o resto da janela no eixo Y (responsividade e simplicidade)
# side=tk.LEFT --> alinha a lista na esquerda da janela
# .pack() --> "pinta" o widget (no caso o frame chatList) na tela
chatList.pack(fill = tk.Y, side=tk.LEFT)

# Configuração da fonte utilizada
f = font.Font(family="Helvetica", size=20)
f2 = font.Font(family="Helvetica", size=15)

# Imagem de perfil dos usuários (literalmente visual pra charme)
pfp = PhotoImage(file = "Images/ProfilePicture.png")

# Botão de cada usuário na lista para mudar o chat
userLb = tk.Button(chatList, text="Grupo de Chat", height=70, width=230, pady=2, anchor=tk.W, relief="solid", bg="#156950", bd=3, fg="white", activebackground="#1C8767", font=f2, image=pfp, compound=LEFT)
userLb.pack()

#-----------------------------------------------------------------------------------------------------

# Criação e configuração da barra superior
upperBar = tk.Frame(root, height=80, bg="#08382a", padx=10, pady=10)
upperBar.pack(fill=tk.X, side=TOP)

# Criação e configuração do nome do usuário do chat atual
currentUser = tk.Label(upperBar, text="Grupo de Chat", font=f, bg="#08382a", fg="white")
currentUser.pack(fill=tk.BOTH, side=tk.LEFT)

#-----------------------------------------------------------------------------------------------------

# Container do chat (mensagens)
chatF = font.Font(family="Helvetica", size = 14)

chatBoxCont = tk.Listbox(master = root, height=25, width=170, font=chatF)
chatBoxCont.pack(side=tk.TOP)

#-----------------------------------------------------------------------------------------------------

# Criação e configuração do container da mensagem à ser enviada
msgBoxCont = tk.Frame(master = root, height=100, bd=1, relief="solid", padx=10, pady=20)
msgBoxCont.pack(fill=tk.X, side=tk.BOTTOM)

# Criação e configuração da caixa de input da mensagem pelo usuário
messageInp = tk.Entry(msgBoxCont, bg="#cbcbcb", width=150)
messageInp.bind("<Return>", envia_mensagens)
messageInp.pack(side=tk.LEFT, fill=tk.Y)
bIcon = PhotoImage(file = "Images/SendIcon.png") # O Ícone de enviar na direita

# Criação e configuração do botão de enviar mensagem
sendB = tk.Button(msgBoxCont, image=bIcon, compound=CENTER, height=80, width=80, bd=0, relief="flat", command=envia_mensagens)
sendB.pack()



username = input('Insira seu nome de usuário: ') # Variável que armazena o nome do usuário

h = socket.gethostname()
p = 1234

# Variável que representa a conexão com o servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuração da conexão com o servidor
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((h, p))
# Feedback de quem entrou na sala
s.sendall('Servidor >>> {} entrou na sala.'.format(username).encode('utf-8'))
print("Online")

print('{}: '.format(username), end = '')

recebe = Thread(target=recebe_mensagens)
recebe.start()





app = main.App(username, master = root) # inicia a classe e define o master como root
app.mainloop() # a princípio, faz com que a interface seja atualizada sem a necessidade de reiniciar o programa (não entendi direito na prática, eu só reiniciava tudo sempre que mudava algo no código)
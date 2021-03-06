from ftpserver import FTP_HOST, FTP_PORT
import socket
from threading import Thread
import os
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *
from tkinter import filedialog
from ftplib import FTP
import re

FTP_HOST = '192.168.15.141'
FTP_PORT = 21

BUFFERSIZE = 4096
filename = ""
# Função responsável por enviar mensagens ao servidor
def envia_mensagens(event=None):
    #while True:
    msg = messageInp.get()
    messageInp.delete(0, END) # Limpa o campo de texto
    # Se o usuário enviar uma mensagem dizendo "fim", o usuário sai da sala.
    if msg.lower() == "fim":
        s.sendall('[SERVIDOR] {} saiu da sala.'.format(username).encode('utf-8'))
    elif msg.lower() == "receber_arquivo":
        recebe_arquivo()
    else:
        s.sendall('{}: {}'.format(username, msg).encode('utf-8')) # (3)

def envia_arquivo(event=None): #thi- envia arquivos utilizando FDP
    # try:
        print('[+] Iniciando sessão (envio)...')
        session = FTP(FTP_HOST, user='saet', passwd='aps')
        session.login()
        print(session.pwd())
        session.cwd('server_data')
        print('[+] Sessão concluída')

        file= filedialog.askopenfile()
        print('[+] File: ',file)

        filepath_str = str(file).split(' ')
        print('[+] Filepath as string: ',filepath_str)

        filepath_str2 = filepath_str[1].split('=')
        print('[+] Filepath str 2: ',filepath_str2)

        filename_list = filepath_str2[1].split('/')
        print('[+] Filename list: ', filename_list)

        filename_p1 = filename_list[-1].split()
        print('Filename_p1: ', filename_p1)

        global filename
        filename = filename_p1[0]
        print('[+] Filename: ',filename)

        aaaa = filepath_str2[1].strip('"')
        print('[+] yea: ',aaaa)

        with open(aaaa.strip("'"), 'rb') as f:
            session.storbinary('STOR '+filename.strip("'"), f)
        f.close()
        # session.retrlines('LIST')
        session.quit()
        s.sendall('{}: {}'.format(username, "Arquivo enviado").encode('utf-8'))
    # except Exception as e:
    #     print('Erro encontrado: ', e)

def recebe_arquivo(event=None):
    print('[+] Iniciando sessão (receber)...')
    session = FTP(FTP_HOST, user='saet', passwd='aps')
    session.login()
    print(session.pwd())
    session.cwd('server_data')
    print('[+] Sessão concluída')
    session.retrlines('NLST')
    filename = session.nlst()
    with open(filename[-1], "wb") as f:
        session.retrbinary(f"RETR {filename[-1]}", f.write)
    f.close()
    session.quit()
    s.sendall('{}: {}'.format(username, "Arquivo recebido").encode('utf-8'))

# Função responsável por receber mensagens do servidor
def recebe_mensagens():
        # Loop infinito para sempre estar recebendo as mensagens enquanto a conexão com o servidor estiver feita
    while True:
        print("Receiving message...")
        msg=s.recv(BUFFERSIZE) # variável que recebe a mensagem do servidor (1)
        # Condicional que verifica se a conexão ainda está feita com o servidor. ("if msg" e "if msg == True" é a mesma coisa)
        
        if msg:
           
            print("Printing Message...")
            
            # Imprime a mensagem (2)

            chatBoxCont.insert(tk.END, msg)
            
        else:
            print('\n[CLIENTE] Conexão perdida com o servidor!')
            print('\n[CLIENTE] Saindo...')
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
f3 = font.Font(family="Helvetica", size=12)

# Imagem de perfil dos usuários (literalmente visual pra charme)
pfp = PhotoImage(file = "Images/ProfilePicture.png")

# Botão de cada usuário na lista para mudar o chat
userLb = tk.Button(chatList, text="Tratamento Rio", height=70, width=230, pady=2, anchor=tk.W, relief="solid", bg="#156950", bd=3, fg="white", activebackground="#1C8767", font=f2, image=pfp, compound=LEFT)
userLb.pack()

corpIcon = tk.PhotoImage(file = "Images/corpIcon.png")
corpL = tk.Label(chatList, image=corpIcon, bg="#156950")
corpL.pack(side = tk.BOTTOM)

name = tk.Label(chatList, text = "Companhia de Tratamento de Rios", bg = "#156950", fg="white", font=f3)
name.pack(side = tk.BOTTOM)

#-----------------------------------------------------------------------------------------------------

# Criação e configuração da barra superior
upperBar = tk.Frame(root, height=80, bg="#08382a", padx=10, pady=10)
upperBar.pack(fill=tk.X, side=TOP)

# Criação e configuração do nome do usuário do chat atual
currentUser = tk.Label(upperBar, text="Tratamento Rio", font=f, bg="#08382a", fg="white")
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
messageInp = tk.Entry(msgBoxCont, bg="#cbcbcb", width=130)
messageInp.bind("<Return>", envia_mensagens)
messageInp.pack(side=tk.LEFT, fill=tk.Y)
bIcon = PhotoImage(file = "Images/SendIcon.png") # O Ícone de enviar na direita

# Criação e configuração do botão de enviar mensagem
sendB = tk.Button(msgBoxCont, image=bIcon, compound=CENTER, height=80, width=80, bd=0, relief="flat", command=envia_mensagens)
sendB.pack(side=tk.RIGHT)

plusbtn = font.Font(size = 20, family="Helvetica")

fileUpload = tk.Button(msgBoxCont, text="+", height=20, width=15, bd=0, relief="flat", font=plusbtn, command=envia_arquivo)
fileUpload.pack(side=tk.LEFT)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

global temp_name
temp_name = tk.StringVar()
def handle_event():
    temp_name = usernamefield.get()
    loginRoot.destroy()
    return temp_name

def enterChat():
    global username
    username = handle_event()

    if username != "":
        loginRoot.destroy()
        h = '192.168.15.141'
        p = 8080

        # Variável que representa a conexão com o servidor
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Configuração da conexão com o servidor
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((h, p))
        print("[SERVIDOR] Online")
        # Feedback de quem entrou na sala
        s.sendall('[SERVIDOR] {} entrou na sala.'.format(username).encode('utf-8'))

        print('{}: '.format(username), end = '')

        recebe = Thread(target=recebe_mensagens)
        recebe.start()

loginRoot = tk.Toplevel(root)
loginRoot.geometry('350x200')
loginRoot.resizable(False, False)
loginRoot.title('Tela de Login')

f = font.Font(size = 25, family='Helvetica')

label = tk.Label(master = loginRoot, text = "Tela de login", foreground='black', font=f)
label.pack(side=tk.TOP)

midframe = tk.Frame(master = loginRoot)
midframe.pack(fill=tk.X)

tfLabel = tk.Label(master = midframe, text="Insira seu nome de usuário: ", foreground='black')
tfLabel.pack(padx=10, pady=35, side=tk.LEFT)

usernamefield = tk.Entry(master = midframe, bg='white', width=25, textvariable=temp_name.get())
usernamefield.pack(padx=2, side=tk.LEFT, ipady=3, fill=tk.X)

submit = tk.Button(master = loginRoot, text = "Enviar", width=20, height=2, command=enterChat)
submit.pack(side=tk.BOTTOM, pady=15)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
try:
    root.mainloop()
except ConnectionRefusedError:
    print("[CLIENTE] Conexão Recusada. O servidor está fechado.")

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *
import socket

class App(tk.Frame):
  # Método construtor que cria e inicia a variável "master" (variável geral do frame) e executa a função FrameConfig
  # a variável e parâmetro "master" referencia o frame geral - a janela toda
  def __init__(self,username,  master = None):
    super().__init__(master)
    self.master = master
    self.username = username
    self.FrameConfig(master)

  # Função que configura e coloca os widgets no frame geral (root)
  def FrameConfig(self, root):
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

    # Imagem de perfil dos usuários (literalmente visual pra charme)
    self.pfp = PhotoImage(file = "Images/ProfilePicture.png")

    # Botão de cada usuário na lista para mudar o chat
    userLb = tk.Button(chatList, text=" Usuário1", height=70, width=230, pady=2, anchor=tk.W, relief="solid", bg="#156950", bd=3, fg="white", activebackground="#1C8767", font=f, image=self.pfp, compound=LEFT)
    userLb.pack()
#-----------------------------------------------------------------------------------------------------
    # Criação e configuração da barra superior
    upperBar = tk.Frame(root, height=80, bg="#08382a", padx=10, pady=10)
    upperBar.pack(fill=tk.X, side=TOP)

    # Criação e configuração do nome do usuário do chat atual
    currentUser = tk.Label(upperBar, text="Usuario1", font=f, bg="#08382a", fg="white")
    currentUser.pack(fill=tk.BOTH, side=tk.LEFT)
#-----------------------------------------------------------------------------------------------------
    # Container do chat (mensagens)
    chatBoxCont = tk.Frame(master = root, height=520, width=100, bg="#EAEAEA")
    chatBoxCont.pack(fill=tk.X, side=tk.TOP)
#-----------------------------------------------------------------------------------------------------
    # Criação e configuração do container da mensagem à ser enviada
    msgBoxCont = tk.Frame(master = root, height=100, bd=1, relief="solid", padx=10, pady=20)
    msgBoxCont.pack(fill=tk.X, side=tk.BOTTOM)

    # Criação e configuração da caixa de input da mensagem pelo usuário
    messageInp = tk.Text(msgBoxCont, bg="#cbcbcb", width=110)
    messageInp.pack(side=tk.LEFT, fill=tk.Y)
    self.bIcon = PhotoImage(file = "Images/SendIcon.png") # O Ícone de enviar na direita

    # Criação e configuração do botão de enviar mensagem
    self.sendB = tk.Button(msgBoxCont, image=self.bIcon, compound=CENTER, height=80, width=80, bd=0, relief="flat")
    self.sendB.pack()
#---------------------------------------------------------------------------------------------------------
  # Função que lê a mensagem para poder enviar ao servidor
  def sendMessage(self):
    print("oi")

# Variáveis para iniciar o frame e os widgets
# root = tk.Tk() # inicia a janela principal
# app = App("Usuário1", master = root) # inicia a classe e define o master como root
# app.mainloop() # a princípio, faz com que a interface seja atualizada sem a necessidade de reiniciar o programa (não entendi direito na prática, eu só reiniciava tudo sempre que mudava algo no código)
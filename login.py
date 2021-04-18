import tkinter as tk
from tkinter import font
import client

def handle_event():
  temp_name = usernamefield.get()
  print(temp_name)
  loginRoot.destroy()
  print("screen destroyed")
  client.root.mainloop()

loginRoot = tk.Tk()
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

usernamefield = tk.Entry(master = midframe, bg='white', width=25)
usernamefield.pack(padx=2, side=tk.LEFT, ipady=3, fill=tk.X)

temp_name = tk.StringVar()

submit = tk.Button(master = loginRoot, text = "Enviar", width=20, height=2, command=handle_event)
submit.pack(side=tk.BOTTOM, pady=15)

loginRoot.mainloop()
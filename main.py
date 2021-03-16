import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.font import *

class App(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    self.master = master
    self.FrameConfig(master)

  def FrameConfig(self, root):
    root.title("Chatbox")
    root.geometry("1280x720")
    root.resizable(False, False)
#-----------------------------------------------------------------------------------------------------
    chatList = tk.Frame(master=root, width = 300, bg = "#156950")
    chatList.pack(fill = tk.Y, side=tk.LEFT)

    f = font.Font(family="Helvetica", size=20)

    self.pfp = PhotoImage(file = "Images/ProfilePicture.png")

    userLb = tk.Button(chatList, text=" Usuário1", height=70, width=230, pady=2, anchor=tk.W, relief="solid", bg="#156950", bd=3, fg="white", activebackground="#1C8767", font=f, image=self.pfp, compound=LEFT)
    userLb.pack()
#-----------------------------------------------------------------------------------------------------
    upperBar = tk.Frame(root, height=80, bg="#08382a", padx=10, pady=10)
    upperBar.pack(fill=tk.X, side=TOP)

    currentUser = tk.Label(upperBar, text="Usuario1", font=f, bg="#08382a", fg="white")
    currentUser.pack(fill=tk.BOTH, side=tk.LEFT)
#-----------------------------------------------------------------------------------------------------
    chatBoxCont = tk.Frame(master = root, height=520, width=100, bg="#EAEAEA")
    chatBoxCont.pack(fill=tk.X, side=tk.TOP)
#-----------------------------------------------------------------------------------------------------
    msgBoxCont = tk.Frame(master = root, height=100, bd=1, relief="solid", padx=10, pady=20)
    msgBoxCont.pack(fill=tk.X, side=tk.BOTTOM)

    self.messageInp = tk.Text(msgBoxCont, bg="#cbcbcb", width=110)
    self.messageInp.pack(side=tk.LEFT, fill=tk.Y)
    self.bIcon = PhotoImage(file = "Images/SendIcon.png")

    self.sendB = tk.Button(msgBoxCont, image=self.bIcon, compound=CENTER, height=80, width=80, bd=0, relief="flat", command=self.sendMessage)
    self.sendB.pack()
#---------------------------------------------------------------------------------------------------------
  def sendMessage(self):
    self.msgInp = self.messageInp.get('1.0', 'end-1c')
    event = self.msgInp
    print(event)

root = tk.Tk()
app = App(master = root)
app.mainloop()
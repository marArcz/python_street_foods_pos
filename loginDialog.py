import tkinter as tk
from tkinter import messagebox, ttk,Toplevel
import home
class Gui:
    def __init__(self,rootWindow):
        self.rootWindow = rootWindow
        self.root = Toplevel(rootWindow)
        self.root.geometry('408x125')

        self.image = tk.PhotoImage(file='./assets/cashier.png',width=65,height=65)
        self.imageLabel = tk.Label(self.root,image=self.image)
        self.imageLabel.pack(side='left',padx=20)

        self.frame = tk.Frame(self.root)
        self.frame.pack(side='left',fill='x',expand=True)

        self.label = tk.Label(self.frame,text='Please enter your pin:',font=('Arial',12),anchor='w')
        self.label.grid(row=0,column=0,sticky='w')
        self.userPin = ""
        self.entry = tk.Entry(self.frame,textvariable=self.userPin,font=('Arial',16),vcmd=self.login,show='*')
        self.entry.bind("<KeyPress>",self.onKeyPressed)
        self.entry.grid(row=1,column=0,pady=5)
        self.entry.focus()

        self.button = tk.Button(self.frame,text='GO',font=('Arial',12,'bold'),background='#7390a5',foreground='white',bd=0,command=self.login)
        self.button.grid(row=1,column=1)
        
        self.root.resizable(False,False)
        self.root.title('Logging In')

    def onKeyPressed(self,event):
        if event.keycode == 13:
            self.login()
    def login(self):
        f = open('pin.txt','r')
        pin = f.read()
        if(self.entry.get() == pin):
            messagebox.showinfo('Logging in',"Successfully logged in!")
            self.root.withdraw()
            self.rootWindow.withdraw()
            home.Gui(self.rootWindow)
        else:
            messagebox.showinfo('Logging in',"Sorry, you entered an incorrect pin!")
            self.root.focus()
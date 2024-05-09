import tkinter as tk
from tkinter import messagebox
import loginDialog

class Gui:
    TRANSPARENT_COLOR = '#ab23ff'
    BG_COLOR = '#F5F5F5'

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title('Street Foods')

        self.mainframe = tk.Frame(self.root,background='#F5F5F5')
        self.mainframe.pack(fill='both')
        self.mainframe.columnconfigure(0,weight=1)
        self.mainframe.columnconfigure(1,weight=2)
        self.titleFrame = tk.Frame(self.mainframe,background='#F5F5F5')
        self.titleFrame.grid(row=0,column=0,sticky=tk.W+tk.E,pady=20,padx=20)
        self.titleFrame.columnconfigure(0,pad=30)
        self.textFrame = tk.Frame(self.titleFrame,background='#F5F5F5')
        self.textFrame.grid(row=0,column=0)
        self.titleLabel = tk.Label(self.textFrame,text='Amilasan\'s Streetfoods',font=('Arial',18,'bold'),anchor='nw',background='#F5F5F5')
        self.titleLabel.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.subtitleLabel = tk.Label(self.textFrame,text='POINT OF SALES SYSTEM',font=('Arial',10),anchor='nw')
        self.subtitleLabel.grid(row=1,column=0,sticky=tk.W+tk.E)

        # cart image
        self.cartImage = tk.PhotoImage(file=self.assets("stand.png"),width=336,height=384)
        self.cartImageLabel = tk.Label(self.mainframe,image=self.cartImage,background=self.BG_COLOR,anchor='se')
        self.cartImageLabel.grid(row=1,column=1,sticky=tk.E+tk.S+tk.N,rowspan=2,padx=30)

        #loginbox
        self.loginBox = tk.Frame(self.mainframe,background='#F5F5F5')
        self.loginBox.grid(row=1,column=0,padx=60,pady=30,sticky='w')

        self.loginBoxHeader = tk.Frame(self.loginBox,background=self.BG_COLOR)
        self.loginBoxHeader.grid(row=0,column=0,sticky='w')

        self.cashierImage = tk.PhotoImage(file=self.assets('cashier.png'),width=57,height=57)
        self.cashierImageLabel = tk.Label(self.loginBoxHeader,image=self.cashierImage,background=self.BG_COLOR)
        self.cashierImageLabel.grid(row=0,column=0,rowspan=2)
        self.label1 = tk.Label(self.loginBoxHeader,text='Welcome!',anchor='w',font=('Arial',14,'bold'),background='#F5F5F5')
        self.label1.grid(row=0,column=1,sticky='w',padx=10)

        self.label2 = tk.Label(self.loginBoxHeader,text='Login to start',anchor='w',font=('Arial',14),foreground='#828282',background='#F5F5F5')
        self.label2.grid(row=1,column=1,sticky='w',padx=10)

        #login button
        self.loginBtnImage = tk.PhotoImage(file=self.assets('Button.png'))
        self.loginBtn = tk.Button(self.loginBox, image=self.loginBtnImage,borderwidth=0,highlightthickness=0, relief='flat',background='#F5F5F5',command=self.showDialog)
        self.loginBtn.grid(row=1,column=0,pady=20)

        self.loginFrame = tk.Frame(self.root)
        self.loginFrame.pack(side='left',fill='x',expand=True)

        self.userPin = ""
        self.loginFrame.pack(side='left',fill='x',expand=True)

        self.root.resizable(False,False)
        self.root.mainloop()

    def assets(self,filename):
        return './assets/' + filename
    def showDialog(self):
        loginDialog.Gui(self.root)   
Gui()
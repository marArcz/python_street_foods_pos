import tkinter as tk


#Adding transparent background property
TRANSPARENT_COLOR = '#ab23ff'
BG_COLOR = '#F5F5F5'

# function for getting assets
def assets(filename):
    return './assets/' + filename


def init():
    global BG_COLOR

    root = tk.Tk()
    root.title = 'Milk Tea Shop'
    root.geometry("800x500") # setting window size
    root.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)
    root.configure(background='#F5F5F5')

    mainframe = tk.Frame(root,background='#F5F5F5')
    mainframe.pack(fill='both')

    mainframe.columnconfigure(0,weight=1)
    mainframe.columnconfigure(1,weight=2)

    titleFrame = tk.Frame(mainframe,background='#F5F5F5')
    titleFrame.grid(row=0,column=0,sticky=tk.W+tk.E,pady=20,padx=20)
    titleFrame.columnconfigure(0,pad=30)

    textFrame = tk.Frame(titleFrame,background='#F5F5F5')
    textFrame.grid(row=0,column=0)

    titleLabel = tk.Label(textFrame,text='Street Foods',font=('Arial',18,'bold'),anchor='nw',background='#F5F5F5')
    titleLabel.grid(row=0,column=0,sticky=tk.W+tk.E)
    subtitleLabel = tk.Label(textFrame,text='POINT OF SALES SYSTEM',font=('Arial',10),anchor='nw')
    subtitleLabel.grid(row=1,column=0,sticky=tk.W+tk.E)


    # cart image
    cartImage = tk.PhotoImage(file=assets('stand.png'),width=336,height=384)
    cartImageLabel = tk.Label(mainframe,image=cartImage,background=BG_COLOR,anchor='se')
    cartImageLabel.grid(row=1,column=1,sticky=tk.E+tk.S+tk.N,rowspan=2,padx=30)

    #loginbox
    loginBox = tk.Frame(mainframe,background='#F5F5F5')
    loginBox.grid(row=1,column=0,padx=60,pady=30,sticky='w')

    loginBoxHeader = tk.Frame(loginBox,background=BG_COLOR)
    loginBoxHeader.grid(row=0,column=0,sticky='w')

    cashierImage = tk.PhotoImage(file=assets('cashier.png'),width=57,height=57)
    cashierImageLabel = tk.Label(loginBoxHeader,image=cashierImage,background=BG_COLOR)
    cashierImageLabel.grid(row=0,column=0,rowspan=2)

    label1 = tk.Label(loginBoxHeader,text='Welcome!',anchor='w',font=('Arial',14,'bold'),background='#F5F5F5')
    label1.grid(row=0,column=1,sticky='w',padx=10)

    label2 = tk.Label(loginBoxHeader,text='Login to start',anchor='w',font=('Arial',14),foreground='#828282',background='#F5F5F5')
    label2.grid(row=1,column=1,sticky='w',padx=10)

    #login button
    loginBtnImage = tk.PhotoImage(file=assets('Button.png'))
    loginBtn = tk.Button(loginBox, image=loginBtnImage,borderwidth=0,highlightthickness=0,relief='flat',background='#F5F5F5')
    loginBtn.grid(row=1,column=0,pady=20)

    root.resizable(False,False)
    root.mainloop()
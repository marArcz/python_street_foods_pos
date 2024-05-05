from datetime import date
import tkinter as tk
import datetime
from tkinter import messagebox

class Gui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1212x693")

        self.headerFrame = tk.Frame(self.root,background='#2c91d8')
        self.headerFrame.pack(side='top',fill='x')

        self.logo = tk.PhotoImage(file='./assets/logo-rounded.png',width=73,height=73)
        self.logoLabel = tk.Label(self.headerFrame,image=self.logo,background='#2c91d8')
        self.logoLabel.grid(row=0,column=0,padx=20,pady=20)

        self.headerTextFrame = tk.Frame(self.headerFrame,background='#2c91d8')
        self.headerTextFrame.grid(row=0,column=1)

        self.appNameLabel = tk.Label(self.headerTextFrame,text='Street Foods',font=('Arial',18,'bold'),background='#2c91d8',foreground='white')
        self.appNameLabel.grid(row=0,column=1,sticky='w')

        self.appSubnameLabel = tk.Label(self.headerTextFrame,text='POINT OF SALES SYSTEM',font=('Arial',12),background='#2c91d8',foreground='white')
        self.appSubnameLabel.grid(row=1,column=1,sticky='w')

        self.sidebar = tk.Frame(self.root,background='#5E5E5E',height=693)
        self.sidebar.pack(side='left',fill='y',anchor='nw')

        self.cashierImage = tk.PhotoImage(file='./assets/cashier.png',width=57,height=57)
        self.sidebarLogoLabel = tk.Label(self.sidebar,image=self.cashierImage,background='#5E5E5E')
        self.sidebarLogoLabel.grid(row=0,column=0,pady=30,padx=20)
        self.dateText = datetime.datetime.now().strftime('%A, %B %d, %Y')

        self.dateLabel = tk.Label(self.sidebar,text=self.dateText,font=('Arial',10,'bold'),foreground='white',background='#5E5E5E')
        self.dateLabel.grid(row=1,column=0,padx=10)

        self.mainFrame = tk.Frame(self.root,height=693)
        self.mainFrame.pack(fill='both')

        self.productsFrame = tk.Frame(self.mainFrame)

        self.productsFrame.grid(row=0,column=0,rowspan=3,sticky=tk.W+tk.N+tk.S,padx=10,pady=10)

        # orders section
        self.ordersFrame = tk.Frame(self.mainFrame)
        self.ordersFrame.grid(row=0,column=1,sticky='nwe')

        self.orderLabel = tk.Label(self.ordersFrame,text='Current Order', font=('Arial',14),anchor='w')
        self.orderLabel.grid(row=0,column=0,pady=10,sticky='nwe')
        
        self.clearBtnBg = tk.PhotoImage(file='./assets/clearBtn.png')
        self.ordersFrame.columnconfigure(index=1,weight=2)
        
        self.orders = []

        self.orderListFrame = tk.Frame(self.ordersFrame)
        self.orderListFrame.grid(row=2,column=0,columnspan=3,pady=10,sticky='we')
        
        self.productList = [
            {
                "name" : "Salted Fries",
                "price":"25",
                "image":"salted-fries.png",
            },
            {
                "name" : "Sour Cheese Fries",
                "price":"45",
                "image":"sour-cheese-fries.png",
            },
            {
                "name" : "Kwek Kwek",
                "price":"20",
                "image":"kwek-kwek.png",
            },
            {
                "name" : "Fishball",
                "price":"35",
                "image":"fishball.png",
            },
        
        ]
        self.clearBtn = tk.Button(self.ordersFrame,image=self.clearBtnBg,relief='flat',borderwidth=0)
        self.clearBtn.image = self.clearBtnBg
        self.clearBtn.config(command=self.clearOrders)
        self.clearBtn.grid(row=1,column=2,sticky='ne')
        self.displayProducts()

        self.totalFrame = tk.Frame(self.ordersFrame)
        self.totalFrame.grid(row=3,column=2,sticky='e')

        self.totalTextlabel = tk.Label(self.totalFrame,text='Total:',anchor='w',font=('Arial',12,'bold'))
        self.totalTextlabel.grid(row=0,column=0)

        self.totalLabel = tk.Label(self.totalFrame,text='0',anchor='w',font=('Arial',12,'bold'))
        self.totalLabel.grid(row=0,column=1)

        self.labelFrame = tk.Frame(self.ordersFrame)
        self.labelFrame.grid(row=4,column=0,columnspan=3,sticky='we',pady=10)
        
        self.labelFrame.columnconfigure(0,weight=1,pad=2)
        self.labelFrame.columnconfigure(1,weight=1,pad=2)

        self.payLabel = tk.Label(self.ordersFrame,text='Payment:',anchor='w',font=('Arial',10,'bold'))
        self.payLabel.grid(row=4,column=0,columnspan=3,sticky='we',pady=10)

        self.paymentBox = tk.Entry(self.ordersFrame, font=('Arial',14))
        self.paymentBox.grid(row=5,column=0,columnspan=3,sticky='we')

        self.generateBtnBg = tk.PhotoImage(file='./assets/generateBtn.png')
        self.generateBtn = tk.Button(self.ordersFrame,text='Generate',image=self.generateBtnBg,relief='flat',borderwidth=0)
        self.generateBtn.grid(row=6,column=0,columnspan=3,sticky='we',pady=10)
        self.generateBtn.config(command=self.generateReceipt)
        self.receiptFrame = tk.Frame(self.mainFrame)
        self.receiptFrame.grid(row=0,column=2,sticky='we')
        
        self.receiptBox = tk.Text(self.receiptFrame,width=30)
        self.receiptBox.grid(row=0,column=0,padx=10,pady=10)

        self.printBtnBg = tk.PhotoImage(file='./assets/printBtn.png')
        self.printBtn = tk.Button(self.receiptFrame,relief='flat',borderwidth=0,anchor='center',image=self.printBtnBg)
        self.printBtn.image = self.printBtnBg
        self.printBtn.grid(row=3,column=0,sticky='we')

        self.displayOrders()

        self.root.resizable(False,False)
        self.root.mainloop()

    def generateReceipt(self):
        self.receiptBox.delete('1.0','end')

        self.receiptBox.insert(index='end-1c',chars="\tStreet Foods\n")
        self.receiptBox.insert(index='end-1c',chars="\t"+datetime.datetime.now().strftime('%B %d, %Y')+"\n\n")
        
        for order in self.orders:
            self.receiptBox.insert(index='end-1c',chars="P"+ str(order['price']) + " " + order['name']+" x " + str(order['quantity'])+"\n")
        
        self.receiptBox.insert(index='end-1c',chars="\nTotal:  " + str(self.getTotal()))
        self.receiptBox.insert(index='end-1c',chars="\nPayment:  " + str(self.paymentBox.get()))
        self.receiptBox.insert(index='end-1c',chars="\nChange:  " + str(int(self.paymentBox.get()) - int(self.getTotal()) ))

        self.receiptBox.print
    def printReceipt(self):
        f = open('receipt.txt','wr')
        f.write(self.receiptBox.get())

        win32api.ShellExecute(0, "print", f, None, ".", 0) 
    def clearOrders(self):
        self.orders.clear()
        self.displayOrders()
    def displayProducts(self):
        
        col=0
        row=0
        index=0

        for product in self.productList:
            self.productsFrame.columnconfigure(index=index,weight=1,pad=5)
            productGrid = tk.Frame(self.productsFrame)
            productGrid.grid(row=row,column=col,sticky='wens')

            image = tk.PhotoImage(file='./assets/products/'+product['image'],width=140,height=121)
            productBtn = tk.Button(productGrid,image=image,relief='groove',text=index)
            productBtn.config(command=lambda button=productBtn:self.onProductClicked(button))

            productBtn.image = image
            productBtn.grid(row=0,column=0)
            
            productname = tk.Label(productGrid,text=product['name'],font=('Arial',10))
            productname.grid(row=1,column=0)
            index+=1

            if col == 2:
                col = 0
                row += 1
            else:
                col += 1

    def onProductClicked(self,button):
        # print('product name: ' + button.cget('text'))
        product = self.productList[int(button.cget('text'))]
        exists = False
        for order in self.orders:
            if order['name'] == product['name']:
                order['quantity'] += 1
                self.displayOrders()
                return
        print('dont exists')
        product['quantity'] = 1
        self.orders.append(product)
        print("Orders: " + str(len(self.orders)))
        self.displayOrders()

    def displayOrders(self):
        self.orderListFrame.destroy()
        self.orderListFrame = tk.Frame(self.ordersFrame)
        self.orderListFrame.grid(row=2,column=0,columnspan=3,sticky='w',pady=10)

        self.orderListHeader1 = tk.Label(self.orderListFrame,text='Product',padx=20,anchor='w',border=1,relief='solid',font=('Arial',10,'bold'))
        self.orderListHeader1.grid(row=0,column=0,sticky='we')

        self.orderListHeader2 = tk.Label(self.orderListFrame,text='Price',padx=20,anchor='w',border=1,relief='solid',font=('Arial',10,'bold'))
        self.orderListHeader2.grid(row=0,column=1,sticky='ww')

        self.orderListHeader3 = tk.Label(self.orderListFrame,text='Quantity',padx=20,anchor='w',border=1,relief='solid',font=('Arial',10,'bold'))
        self.orderListHeader3.grid(row=0,column=2)
        
        self.orderListHeader4 = tk.Label(self.orderListFrame,text='',padx=20,anchor='w',border=1,relief='solid',font=('Arial',10,'bold'))
        self.orderListHeader4.grid(row=0,column=3,sticky='we')

        row = 1
        
        for order in self.orders:
            orderNameLabel = tk.Label(self.orderListFrame,text=order['name'],anchor='center',relief='solid',border=1)
            orderNameLabel.grid(row=row,column=0,sticky='nswe')

            orderPriceLabel = tk.Label(self.orderListFrame,text=order['price'],relief='solid',border=1)
            orderPriceLabel.grid(row=row,column=1,sticky='nswe')

            orderQuantityFrame = tk.Frame(self.orderListFrame,relief='solid',border=1)
            orderQuantityFrame.grid(row=row,column=2,sticky='nswe')

            orderQuantityFrame.columnconfigure(0,weight=1)
            orderQuantityFrame.columnconfigure(1,weight=1)
            orderQuantityFrame.columnconfigure(2,weight=1)

            orderQuantityBtnUp = tk.Button(orderQuantityFrame,text='+',font=('Arial',10,'bold'))
            orderQuantityBtnUp.grid(row=0,column=0,sticky='wens')
            orderQuantityBtnUp.config(command=lambda order=order:self.updateQuantity(order,action='up'))
            orderQuantityBtnDown = tk.Button(orderQuantityFrame,text='-',font=('Arial',10,'bold'))
            orderQuantityBtnDown.config(command=lambda order=order:self.updateQuantity(order,action='down'))
            orderQuantityBtnDown.grid(row=0,column=2,sticky='wens')

            orderQuantityLabel = tk.Label(orderQuantityFrame,text=order['quantity'],font=('Arial',12,'bold'))
            orderQuantityLabel.grid(row=0,column=1,sticky='nswe')

            orderRemoveBtnImage = tk.PhotoImage(file='./assets/removeBtn.png')
            orderRemoveBtn = tk.Button(self.orderListFrame,text='x',relief='solid',border=1,image=orderRemoveBtnImage,background='#9E3E3E')
            orderRemoveBtn.config(command=lambda order=order:self.removeOrder(order))
            orderRemoveBtn.image = orderRemoveBtnImage
            orderRemoveBtn.grid(row=row,column=3,sticky='nswe')

            row += 1

        self.computeTotal()
    def updateQuantity(self,order,action):
        index = self.orders.index(order)
        if action == 'up':
            newQuantity = int(order['quantity']) + 1
            self.orders[index]['quantity'] = newQuantity
        else:
            newQuantity = int(order['quantity']) - 1
            if newQuantity == 0:
                self.removeOrder(order)
            self.orders[index]['quantity'] = newQuantity
        self.displayOrders()
    def removeOrder(self,order):
        for o in self.orders:
            if o['name'] == order['name']:
                self.orders.remove(o)
                self.displayOrders()
                return
    def productClicked(self):
        print('hello')
    def getTotal(self):
        total = 0
        for order in self.orders:
            total += int(order['quantity']) * int(order['price'])
        return total
    def computeTotal(self):
        self.totalLabel.config(text=self.getTotal())
Gui()
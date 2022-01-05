from tkinter import *
from tkinter import  filedialog
import tkinter.messagebox as tmsg
import random
from datetime import date
import os
window=Tk()
window.geometry('1500x800')
window.wm_iconbitmap("icon.jpg")
window.title("Billing invoice-by ravi")
date = date.today()

def convertToDigit(n, suffix):
    # if `n` is zero
    if n == 0:
        return EMPTY

    # split `n` if it is more than 19
    if n > 19:
        return Y[n // 10] + X[n % 10] + suffix
    else:
        return X[n] + suffix


# Function to convert a given number (max 9-digits) into words
def convert(n):
    # add digits at ten million and hundred million place
    result = convertToDigit((n // 1000000000) % 100, "Billion, ")

    # add digits at ten million and hundred million place
    result += convertToDigit((n // 10000000) % 100, "Crore, ")

    # add digits at hundred thousand and one million place
    result += convertToDigit(((n // 100000) % 100), "Lakh, ")

    # add digits at thousand and tens thousand place
    result += convertToDigit(((n // 1000) % 100), "Thousand ")

    # add digit at hundred place
    result += convertToDigit(((n // 100) % 10), "Hundred ")

    if n > 100 and n % 100:
        result += "and "

    # add digits at ones and tens place
    result += convertToDigit((n % 100), "")

    return result

EMPTY = ""

X = [EMPTY, "One ", "Two ", "Three ", "Four ", "Five ", "Six ",
         "Seven ", "Eight ", "Nine ", "Ten ", "Eleven ", "Twelve ",
         "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ",
         "Seventeen ", "Eighteen ", "Nineteen "]

Y = [EMPTY, EMPTY, "Twenty ", "Thirty ", "Forty ", "Fifty ",
         "Sixty ", "Seventy ", "Eighty ", "Ninety "]



def savefile():
    file=filedialog.asksaveasfile(initialfile=f'{invoice_no}-{namevar.get()}-{contactvar.get()}',defaultextension='.txt',filetypes=[("Text file",".txt"),("HTML file",".html"),("PDF",".pdf")])
    filetext=str(TextArea.get(1.0,END))
    if file is None:
        return
    file.write(filetext)
    file.close()
def searchfile():
    searchfile=searchvar.get()
    customer_dir="D:\\customer detail"
    customer_list=os.listdir(customer_dir)
    searchcount=0
    for files in customer_list:
        if searchfile in files:
            searchcount=searchcount+1
            f=open(f"D:\\customer detail\\{files}")
            content=f.read()
            TextArea.insert(END,f"{content}\n")
            f.close()
    if searchcount==0 :
        TextArea.insert(END,".........Not found any result..........")

def clearbill():
    TextArea.delete(1.0,END)
invoice_no = random.randint(1000, 9999)

def cus_detail():
    global invoice_no
    invoice_no = random.randint(1000, 9999)
    address = addressvar.get()
    name = namevar.get()
    contact = contactvar.get()
    TextArea.insert(END,
                    f"     Invoice no. {invoice_no}                                                   Date: {date}\n")
    TextArea.insert(END, f"      Ref No.                                                                       \n")
    TextArea.insert(END, f"                                    SANJU FRUIT SHOP                             \n")
    TextArea.insert(END, f"                                        MATHURA                                   \n")
    TextArea.insert(END, f"                                        INVOICE                                   \n")
    TextArea.insert(END,f"                             customer det.-{name}-{contact}-{address}                                          \n")
    TextArea.insert(END, f"                                                                           \n")
    TextArea.insert(END, f"                                                                           \n")
    TextArea.insert(END,f"      SN.        Description of product          Quantity         Rate       Amount                   \n")

SN=0
FINAL_PRICE=0
def AddItem():
    global SN,FINAL_PRICE
    SN=SN+1;
    item = itemvar.get()
    qty = qtyvar.get()
    price = pricevar.get()
    FINAL_PRICE=FINAL_PRICE+(qty*price)
    space=" "
    if len(item) > 0:
     addspace=space*(31-len(item))
    else:
     addspace=space*31
    TextArea.insert(END,f"       {SN}           {item}{addspace}{qty}kg             {price}          {qty*price}                      \n")

def TOTAL():
    global FINAL_PRICE,SN
    amount_word=convert(FINAL_PRICE)
    TextArea.insert(END, f"                       \n")
    TextArea.insert(END,f"                       \n")
    TextArea.insert(END,f"                       \n")
    TextArea.insert(END,f"                       \n")
    TextArea.insert(END,f"                       \n")
    TextArea.insert(END,f"                                Total                                           Rs.{FINAL_PRICE} \n")
    TextArea.insert(END,f"      Amount Chargeable (in words)                                                                      \n")
    TextArea.insert(END,f"      {amount_word}                                                                     \n")
    TextArea.insert(END,f"                                                                           \n")
    TextArea.insert(END,f"      Declaration                                                     for sanju fruits shop                    \n")
    TextArea.insert(END,f"      We declare that this invoice shows the                                                                    \n")
    TextArea.insert(END,f"      actual price of the goods described and                                                                    \n")
    TextArea.insert(END,f"      that all particulars are true and correct                            authorised sign                                        \n")
    TextArea.insert(END,f"                           This is a Computer Generated Invoice                                        \n")
    FINAL_PRICE=0
    SN=0
def openfile():
    filepath=filedialog.askopenfilename()
    f = open(filepath)
    content = f.read()
    TextArea.insert(END, f"{content}\n")
    f.close()



def help():
    a=tmsg.showinfo("Help","Email us on golaravi555@gmail.com")

menubar=Menu(window)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=clearbill)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Print",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=quit)
menubar.add_cascade(label="File",menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Dark Theme")
editmenu.add_command(label="Light Theme")
editmenu.add_separator()
editmenu.add_command(label="TextArea Dark")
editmenu.add_command(label="TextArea Light")
editmenu.add_separator()
editmenu.add_command(label="Reset")
menubar.add_cascade(label="Edit",menu=editmenu)

menubar.add_command(label="Help",command=help)

window.config(menu=menubar)



scrollbar=Scrollbar(window)
scrollbar.pack(side=RIGHT,fill="y")
shop_name=Label(window,text="Sanju Fruit Shop Billing Invoice",font=(None,30,'bold'))
shop_name.pack(pady=0)
f1=Frame(window,padx=10)
f1.pack(side=LEFT)
TextArea=Text(window,width="100",height="100",yscrollcommand=scrollbar.set)
TextArea.pack(side=RIGHT,pady=20,padx=20)
scrollbar.config(command=TextArea.yview)
customer_title=Label(f1,text="Enter your customer detail :",font=(None,18,'bold'))
customer_title.grid(row=1,column=1,pady=10)
namel    = Label(f1,text="Name      :",font=18)
namel.grid(row=2,column=1,pady=10)
contactl = Label(f1,text="Contact   :",font=18)
contactl.grid(row=3,column=1,pady=10)
addressl = Label(f1,text="Address   :",font=18)
addressl.grid(row=4,column=1,pady=10)
ok=Button(f1,text="ok",font=18,command=cus_detail).grid(row=5,column=2,pady=10)
item_title=Label(f1,text="Enter your item detail   :",font=(None,18,'bold'))
item_title.grid(row=6,column=1,pady=10)
iteml    = Label(f1,text="Item Name :",font=18)
iteml.grid(row=7,column=1,pady=10)
quantityl= Label(f1,text="Quantity  :",font=18)
quantityl.grid(row=8,column=1,pady=10)
pricel  = Label(f1,text="Price     :",font=18)
pricel.grid(row=9,column=1,pady=10)
namevar=StringVar()
contactvar=IntVar()
addressvar=StringVar()
itemvar=StringVar()
qtyvar=IntVar()
pricevar=IntVar()
searchvar=StringVar()
nameEntry=Entry(f1,textvariable=namevar,font=18).grid(row=2,column=2)
contactEntry=Entry(f1,textvariable=contactvar,font=18).grid(row=3,column=2)
AddressEntry=Entry(f1,textvariable=addressvar,font=18).grid(row=4,column=2)
itemEntry=Entry(f1,textvariable=itemvar,font=18).grid(row=7,column=2)
qtyEntry=Entry(f1,textvariable=qtyvar,font=18).grid(row=8,column=2)
priceEntry=Entry(f1,textvariable=pricevar,font=18).grid(row=9,column=2)
searchEntry=Entry(f1,textvariable=searchvar,font=18).grid(row=0,column=1)
add_item=Button(f1,text="Add Item",font=18,command=AddItem).grid(row=10,column=2,pady=10)
total=Button(f1,text="Total",font=18,command=TOTAL).grid(row=11,column=1,pady=10)
save=Button(f1,text="Save",font=18,command=savefile).grid(row=11,column=2,pady=10)
search=Button(f1,text="Search",font=18,command=searchfile).grid(row=0,column=2)
clear=Button(f1,text="Clear",font=18,command=clearbill).grid(row=12,column=1)
EXIT=Button(f1,text="EXIT",font=18,command=window.destroy).grid(row=12,column=2)


window.mainloop()

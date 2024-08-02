#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
import tkinter.messagebox as tkmsg

call = Tk()
call.title('Calculator')
call.config(bg='#a4a1a1')
call.geometry('270x350')
call.grid()
call.resizable(0,0)

val = ""
A = 0
oprator =''

def btn1():
    global val
    val = val +"1"
    data.set(val)
def btn2():
    global val
    val = val +"2"
    data.set(val)
def btn3():
    global val
    val = val +"3"
    data.set(val)
def btn4():
    global val
    val = val +"4"
    data.set(val)
def btn5():
    global val
    val = val +"5"
    data.set(val)
def btn6():
    global val
    val = val +"6"
    data.set(val)
def btn7():
    global val
    val = val +"7"
    data.set(val)
def btn8():
    global val
    val = val +"8"
    data.set(val)
def btn9():
    global val
    val = val +"9"
    data.set(val)
def btn0():
    global val
    val = val +"0"
    data.set(val)
    
def btn00():
    global val
    val = val + '00'
    data.set(val)

def btno():
    global val
    val = val +'.'
    data.set(val)
    
def btnadd():
    global A
    global operator
    global val
    A = float(val)
    operator = '+'
    val = val + '+'
    data.set(val)

def btnsub():
    global A
    global operator
    global val
    A = float(val)
    operator = '-'
    val = val + '-'
    data.set(val)
    
def btnmul():
    global A
    global operator
    global val
    A = float(val)
    operator = '*'
    val = val + '*'
    data.set(val)
    
def btndiv():
    global A
    global operator
    global val
    A = float(val)
    operator = '/'
    val = val + '/'
    data.set(val)
    
def btndel():
    global A
    global operator
    global val
    val =''
    A=0
    operator =''
    data.set(val)
    
def result():
    global A
    global operator
    global val
    val2=val
    if operator =='+':
        x = float((val2.split('+')[1]))
        c = A + x
        data.set(c)
        val = float(c)
    elif operator =='-':
        x = float((val2.split('-')[1]))
        c = A - x
        data.set(c)
        val = float(c)
    elif operator =='*':
        x = float((val2.split('*')[1]))
        c = A * x
        data.set(c)
        val = float(c)
        
    elif operator =='/':
        x = float((val2.split('/')[1]))
        if x==0:
            tkmsg.show('Error',"Division by 0 Not Allowed")
            A=""
            val=""
            data.set(val)
        else:
            c = float(A / x)
            data.set(c)
            val = float(c)
            
data = StringVar()

frame = Frame(call,bg='#ffffff')
num_dis=Entry(call,width=20,font=('Tahoma',30,'bold'),textvariable = data).pack(padx=5,pady=10)


buttons1 = Button(call,text='1',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn1).place(x=6,y=100)
buttons2 = Button(call,text='2',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command =btn2).place(x=70,y=100)
buttons3 = Button(call,text='3',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn3).place(x=134,y=100)
buttons4 = Button(call,text='4',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn4).place(x=6,y=150)
buttons5 = Button(call,text='5',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn5).place(x=70,y=150)
buttons6 = Button(call,text='6',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn6).place(x=134,y=150)
buttons7 = Button(call,text='7',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn7).place(x=6,y=200)
buttons8 = Button(call,text='8',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn8).place(x=70,y=200)
buttons9 = Button(call,text='9',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn9).place(x=134,y=200)
buttons0 = Button(call,text='0',font=('Tahoma',15,'bold'),bg='#6c6573',fg='#eee5f8',width=4,command=btn0).place(x=70,y=250)


buttons_add = Button(call,text='+',font=('Tahoma',15,'bold'),bg='#6c6573',
                     fg='#eee5f8',width=4,command=btnadd).place(x=198,y=250)

buttons_sub = Button(call,text='-',font=('Tahoma',15,'bold'),bg='#6c6573',
                     fg='#eee5f8',width=4,command=btnsub).place(x=198,y=200)
buttons_mul = Button(call,text='x',font=('Tahoma',15,'bold'),bg='#6c6573',
                     fg='#eee5f8',width=4,command=btnmul).place(x=198,y=150)
buttons_div = Button(call,text='/',font=('Tahoma',15,'bold'),bg='#6c6573',
                     fg='#eee5f8',width=4,command=btndiv).place(x=198,y=100)
buttons_do = Button(call,text='.',font=('Tahoma',15,'bold'),bg='#6c6573',
                    fg='#eee5f8',width=4,command=btno).place(x=6,y=250)
buttons_de = Button(call,text='C',font=('Tahoma',15,'bold'),bg='#6c6573',
                    fg='#eee5f8',width=4,command=btndel).place(x=6,y=300)
Buttons_pe = Button(call,text='00',font=('Tahoma',15,'bold'),bg='#6c6573',
                    fg='#eee5f8',width=4,command = btn00).place(x=134,y=250)
buttons_eq = Button(call,text='=',font=('Tahoma',15,'bold'),bg='#6c6573',
                    fg='#eee5f8',width=4,command=result).place(x=198,y=300)

call.mainloop()


# In[ ]:





# In[ ]:





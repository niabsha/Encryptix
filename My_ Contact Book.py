#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import*
import tkinter.messagebox as tkmsg
import tkinter.ttk as ttk

con_book=Tk()
con_book.title('Contact Book')
con_book.geometry('900x600')
con_book.config(bg='#c5c5c5')
con_book.style = ttk.Style(con_book)
con_book.style.theme_use('default')
con_book.resizable(False,False)

#title
Label(con_book,text='My" Contact Book',font=('Tahoma',18,'bold'),
      bg='#c5c5c5',fg='#14213d').pack(pady=5)

con_details =Label(con_book,text='Contact Details',font=('Tahoma',15,'bold'),
      bg='#c5c5c5',fg='#14213d').place(x=500,y=50)

#Contact list
frame = Frame(con_book).pack(side = LEFT)

con_list =Label(con_book,text='Contact List',font=('Tahoma',15,'bold'),
      bg='#c5c5c5',fg='#14213d').place(x=50,y=50)


select1 = Listbox(frame,font = ('Tahoma',15),bg='#eef9f9',width =20,borderwidth=3,relief='groove')
select1.place(x=50,y=85)

#Variables
Name = StringVar()
Mob_Number = StringVar()
Tel_Number = StringVar()
E_id = StringVar()
Ad_ress = StringVar()

contact_list=[]

def Selected():
    selection = select1.curselection()
    if selection:
        return int(selection[0])
    else:
        return None

def AddContact():
    if Name.get() !='' and Mob_Number.get() !='' and Tel_Number.get()!='' and E_id.get()!='' and Ad_ress.get()!='':
        contact_list.append([Name.get(),Mob_Number.get(),Tel_Number.get(),E_id.get(),Ad_ress.get()])
        Select_set()
        EntryReset()
        tkmsg.showinfo('Confirmation','Successfully Add New Contact')
    
    else:
        tkmsg.showerror('Error','Please fill the information')
        
def Edit():
    if Name.get() and Mob_Number.get() and Tel_Number.get() and E_id.get() and Ad_ress.get():
        contact_list[Selected()] = [Name.get(),Mob_Number.get(),Tel_Number.get(),E_id.get(),Ad_ress.get()]
        
        tkmsg.showinfo('Confirmation','Successfully Update Contact')
        EntryReset()
        Select_set()
        
    elif not(Name.get()) and not(Mob_Number.get()) and not(Tel_Number.get()) and not(E_id.get()) and not(Ad_ress.get()):
        tkmsg.showerror('Error','Please Select the Name and \n press Edit button')
    else:
        msg1='''To Edit the all information of \n selected row press Edit button\n.'''
        tkmsg.showerror('Error',msg1)
        
def Del():
    if len(select1.curselection())!=0:
        result = tkmsg.askyesno('Confirmation','You want to Delete Contact\n which you selected')
        if result == True:
            del contact_list[Selected()]
            Select_set()
    else:
           tkmsg.showerror('Error','Please select the Contact')
            
def View():
    selected_index = select1.curselection()
    if selected_index:
        index = selected_index[0]
    NAME,MOBILE,TELEPHONE,EMAIL,ADDRESS = contact_list[index]
    Name.set(NAME)
    Mob_Number.set(MOBILE)
    Tel_Number.set(TELEPHONE)
    E_id.set(EMAIL)
    Ad_ress.set(ADDRESS)
    
def Exit():
    con_book.destroy()
    
def Select_set():
    select1.delete(0,END)
    for i, contact in enumerate(contact_list):
        select1.insert(i,contact[0])
        
def EntryReset():
    Name.set('')
    Mob_Number.set('')
    Tel_Number.set('')
    E_id.set('')
    Ad_ress.set('')
    
    
    
#Label
Label(con_book,text = 'Name:',font = ('Tahoma',14,'bold'),bg='#c5c5c5',fg='#14213d').place(x=500,y=100)
Entry(con_book,textvariable = Name,width =25).place(x=700,y=105)
    
            
Label(con_book,text = 'Mobile Number:',font = ('Tahoma',14,'bold'),bg='#c5c5c5',fg='#14213d').place(x=500,y=150)
Entry(con_book,textvariable = Mob_Number,width =25).place(x=700,y=155)

Label(con_book,text = 'Telephone Number:',font = ('Tahoma',14,'bold'),bg='#c5c5c5',fg='#14213d').place(x=500,y=200)
Entry(con_book,textvariable = Tel_Number,width =25).place(x=700,y=205)
    
            
Label(con_book,text = 'Email Id:',font = ('Tahoma',14,'bold'),bg='#c5c5c5',fg='#14213d').place(x=500,y=250)
Entry(con_book,textvariable = E_id,width =25).place(x=700,y=255)

Label(con_book,text = 'Address:',font = ('Tahoma',14,'bold'),bg='#c5c5c5',fg='#14213d').place(x=500,y=300)
Entry(con_book,textvariable = Ad_ress,width =25).place(x=700,y=305)
    

#Buttons

add_btn=Button(con_book,text='Add',relief=FLAT,font=("Tahoma",12,'bold'),bg='#149715',fg='#FFFFFF',command=AddContact)
add_btn.place(x=500,y=500)   

edit_btn=Button(con_book,text='Edit',relief=FLAT,font=("Tahoma",12,'bold'),bg='#149715',fg='#FFFFFF',command=Edit)
edit_btn.place(x=575,y=500)

del_btn=Button(con_book,text='Delete',relief=FLAT,font=("Tahoma",12,'bold'),bg='#FF2525',fg='#FFFFFF',command=Del)
del_btn.place(x=750,y=500)


view_btn=Button(con_book,text='View',relief=FLAT,font=("Tahoma",12,'bold'),bg='#149715',fg='#FFFFFF',command=View)
view_btn.place(x=650,y=500)

exit_btn=Button(con_book,text='Exit',relief=FLAT,font=("Tahoma",12,'bold'),bg='#FF2525',fg='#FFFFFF',command=Exit)
exit_btn.place(x=850,y=500)


con_book.mainloop()


# In[ ]:





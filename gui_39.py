from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
main=tk.Tk()
main.geometry('1200x800')
main.title('Zomato')
main.config(bg="lavender")
#label
l=Label(main,font=('Roboto',20),fg='red',bg="black",text="Create account").place(x=500,y=100)
nl=Label(main,font=('Arial',18),fg='navyblue',bg="white",text="Name").place(x=400,y=200)
pl=Label(main,font=('Arial',18),fg='navyblue',bg="white",text="Password").place(x=400,y=250)


def show():
    name = ne.get()
    pwd = pe.get()
    place=places.get()
    g=gender.get()
    print("Name:", name)
    print("Password:", pwd)
    print("place:",place)
    print("gender:",g)
   
ne=Entry(main)
ne.place(x=600,y=210)#.grid(row=0,column=0)
pe=Entry(main,show='*')#.grid(row=0,column=1)
pe.place(x=600,y=260)

Button(main,text='submit',command=show).place(x=400,y=450)



places=Combobox(main)
places["values"]=("select","tamilnadu","delhi","kerala","karnataka")
places.current(0)
places.place(x=340,y=340)




'''rb=Radiobutton(main,text="male",value=0)
rb.place(x=300,y=400)
rb1=Radiobutton(main,text="female",value=1)
rb1.place(x=400,y=400)'''

gender=StringVar(value="Male")

rb=Radiobutton(main,text="Male",variable=gender,value="Male")
rb.place(x=300,y=400)
rb1=Radiobutton(main,text="Female",variable=gender,value="Female")
rb1.place(x=400,y=400)

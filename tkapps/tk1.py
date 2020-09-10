from tkinter import *
import dicstu
import json 


def search_command():
    list1.delete(0,END)
    for row in dicstu.dict(word.get()):
       list1.insert(END,row)
     

window = Tk()

#window.minsize(600,150)
window.maxsize(600,150)
window.wm_iconbitmap('icon1.ico')
window.wm_title("Tanvi'sDictu")
l= Label(window,text="Word")
l.grid(row=0,column=0)

word= StringVar()
e=Entry(window,textvariable=word)
e.grid(row=0,column=1)

list1=Listbox(window,height=5,width=60)
list1.grid(row=1,column=0,rowspan=6,columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=1,column=3,rowspan=6)

sb2=Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=7,column=1,rowspan=6)

list1.configure(yscrollcommand=sb1.set,xscrollcommand=sb2.set)
sb1.configure(command=list1.yview)
sb2.configure(command=list1.xview)

b1=Button(window,text="Search",width=12,command=search_command)
b1.grid(row=0,column=4)

b2 = Button(window,text="Close",width=12,command=window.destroy)
b2.grid(row=0,column=6)


window.mainloop()
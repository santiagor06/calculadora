from tkinter import *

def calcTotal():
    operacion=texto.get()
    total=eval(operacion)
    texto.delete(0,len(texto.get()))
    texto.insert(len(texto.get()),total)
    
    

window=Tk()
window.title("Calculadora")

texto=Entry(window,font=("arial 20"))
texto.grid(row=0,column=0,columnspan=4,padx=5,pady=5)


sum=Button(window,text="+",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"+"))
sum.grid(row=1,column=0,padx=0,pady=0)

rest=Button(window,text="-",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"-"))
rest.grid(row=1,column=1,padx=1,pady=1)

multi=Button(window,text="*",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"*"))
multi.grid(row=2,column=0,padx=1,pady=1)

deleted=Button(window,text="A/C",width=20,height=2,command=lambda:texto.delete(0,len(texto.get())))
deleted.grid(row=1,column=2,columnspan=2,padx=1,pady=1)



div=Button(window,text="/",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"/"))
div.grid(row=2,column=1,padx=1,pady=1)

box0=Button(window,text="0",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"0"))
box0.grid(row=3,column=0,padx=1,pady=1)

box1=Button(window,text="1",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"1"))
box1.grid(row=3,column=1,padx=1,pady=1)

box2=Button(window,text="2",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"2"))
box2.grid(row=3,column=2,padx=1,pady=1)

box3=Button(window,text="3",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"3"))
box3.grid(row=3,column=3,padx=1,pady=1)

box4=Button(window,text="4",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"4"))
box4.grid(row=4,column=0,padx=1,pady=1)

box5=Button(window,text="5",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"5"))
box5.grid(row=4,column=1,padx=1,pady=1)

box6=Button(window,text="6",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"6"))
box6.grid(row=4,column=2,padx=1,pady=1)

box7=Button(window,text="7",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"7"))
box7.grid(row=4,column=3,padx=1,pady=1)

box8=Button(window,text="8",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"8"))
box8.grid(row=5,column=0,padx=1,pady=1)

box9=Button(window,text="9",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"9"))
box9.grid(row=5,column=1,padx=1,pady=1)
boxp1=Button(window,text="(",width=5,height=2,command=lambda:texto.insert(len(texto.get()),"("))
boxp1.grid(row=5,column=2,padx=1,pady=1)

boxp2=Button(window,text=")",width=5,height=2,command=lambda:texto.insert(len(texto.get()),")"))
boxp2.grid(row=5,column=3,padx=1,pady=1)

total=Button(window,text="=",width=40,height=2,command=lambda:calcTotal())
total.grid(row=6,column=0,columnspan=4,padx=5,pady=5)





window.mainloop()
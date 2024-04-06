from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.title("Translator Project")
root.geometry("740x400")

def show():
    v1=combo_first.get()
    v2=combo_second.get()
    first_lan.config(text=v1)
    second_lang.config(text=v2)
    root.after(1000,show)

def translate():
    trans=Translator()
    trans_lang=trans.translate(input_text.get(1.0,END),src=combo_first.get(),dest=combo_second.get())
    
    output_text.delete(1.0,END)
    output_text.insert(END,trans_lang.text)
       
def clear():
    output_text.delete(1.0,END)
    input_text.delete(1.0,END)

def exit():
    root.destroy()
    
bg_img=PhotoImage(file=r'C:\\Users\\hp\Downloads\\background.png')

lab = Label(root,image=bg_img)
lab.pack()

corr_img = PhotoImage(file=r'C:\\Users\\hp\Downloads\\Convert.png')
clear_img = PhotoImage(file=r'C:\\Users\\hp\Downloads\\cl.png')
exit_img = PhotoImage(file=r'C:\\Users\\hp\Downloads\\exts.png')

first_lan = Label(root,text="English",font=("Engraves",30,"bold"),fg="#5582f9",bg="white")
first_lan.place(x=90,y=30)

second_lang = Label(root,text="Hindi",font=("Engraves",30,"bold"),bg="#5582f9",fg="white")
second_lang.place(x=500,y=30)

language = list(LANGUAGES.values())

combo_first = ttk.Combobox(root,values=language)
combo_first.place(x=90,y=80)
combo_first.set("English")

combo_second = ttk.Combobox(root,values=language)
combo_second.place(x=500,y=80)
combo_second.set("Hindi")

input_text = Text(root,height=10,width=35,bg="#5582f9",fg="white")
input_text.place(x=30,y=100)

output_text = Text(root,height=10,width=35,fg="#5582f9",bg="white")
output_text.place(x=430,y=100)

convert = Button(root,text="convert",image=corr_img,bg="white",bd=0,command=translate)
convert.place(x=43,y=300)

clear=Button(root,text="clear",image=clear_img,bg="#5582f9",bd=0,command=clear)
clear.place(x=300,y=300)

ext=Button(root,text="exit",image=exit_img,bg="#5582f9",bd=0,command=exit)
ext.place(x=530,y=300)
show()

root.mainloop()
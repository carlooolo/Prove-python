from tkinter import *            
from tkinter import messagebox
import time
import tkinter.font as font 

f=Tk()     
f.title('PANNELLO DI CONTROLLO')
f.geometry('1024x600')
f.resizable(0, 0)
photo = PhotoImage(file ="mits.png") #cambiare in base al tuo nome
f.iconphoto(False, photo)
photo2= PhotoImage(file='logo.png') #cambiare in base al tuo nome
label=Label(f, image=photo2)
label.pack()
label2=Label(f, text='                                                                                                                                                      Copyright @Gruppo Fighi                                                                                                                                                      ', 
background='#17202A', fg='#F7F9F9') #un piccolo sacrificio per la bellezza
label2.pack(side=BOTTOM)
myfont= font.Font(size=25, weight='bold')
myfont2= font.Font(size=15, weight='bold')
myfont3= font.Font(size=20, weight='bold')

def tab1():
    def tab2():
        def set_text_by_button():
            sample_text.delete(0,"end")
            sample_text.insert(0, "Macchina in funzione!")
            sample_text['font']= myfont3
        def set_text_by_button1():
            sample_text.delete(0,"end")
            sample_text.insert(0, "Macchina fermata!")
            sample_text['font']= myfont3
        sample_text = Entry(f, background='#d7dde0')
        sample_text['font']= myfont3
        sample_text.pack()
        button_avvio.destroy()
        button_esci.destroy()
        button_start= Button(f, text='START',borderwidth=5, background='#58D68D', activebackground='#78d6ff', command=set_text_by_button)
        button_start.pack(side=LEFT, padx=170)
        button_start['font']= myfont3
        button_stop= Button(f, text='STOP',borderwidth=5, background='#C0392B', activebackground='#78d6ff', command=set_text_by_button1)
        button_stop.pack(side=RIGHT, padx=170)
        button_stop['font']= myfont3
        def back():
            button_start.destroy()
            button_back.destroy()
            button_stop.destroy()
            sample_text.destroy()
            tab1()
        button_back= Button(f, text='INDIETRO',borderwidth=5, background='#b0bbc1', activebackground='#78d6ff', command=back)
        button_back.pack(side=BOTTOM, pady=10)
        button_back['font']= myfont2
    button_avvio= Button(f, text='AVVIO',borderwidth=5, background='#F4D03F', activebackground='#78d6ff', command=tab2)
    button_avvio.pack(side=TOP, pady=100)
    button_avvio['font']= myfont
    button_esci= Button(f, text='ESCI',borderwidth=5, background='#b0bbc1', activebackground='#E74C3C', command=f.quit)
    button_esci.pack(side=BOTTOM, pady=10)
    button_esci['font']= myfont2    
tab1()
f.mainloop()

# aggiungere il copyright in fondo con il background scuro

# fare qualche modifica per le scritte macchine
# scegliere un font migliore

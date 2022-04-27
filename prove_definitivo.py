from tkinter import *
from tkinter import messagebox

f=Tk()
f.title('Pannello di Controllo')
f.geometry('400x350')
photo = PhotoImage(file = "mits.png") #cambiare in base al tuo nome
f.iconphoto(False, photo)
photo2= PhotoImage(file='logo.png') #cambiare in base al tuo nome
label=Label(f, image=photo2)
label.pack(side=TOP)
    
def tab1():
    def tab2():
        def popup_start():
            messagebox.showwarning('Attenzione!', 'Macchina in funzione!')
        def popup_stop():
            messagebox.showwarning('Attenzione!', 'Macchina fermata')
        button_avvio.destroy()
        button_esci.destroy()
        button_start= Button(f, text='START', command=popup_start)
        button_start.pack(side=LEFT, padx=50, pady=30)
        button_stop= Button(f, text='STOP', command=popup_stop)
        button_stop.pack(side=RIGHT, padx=50, pady=30)
        def back():
            button_start.destroy()
            button_back.destroy()
            button_stop.destroy()
            tab1()
        button_back= Button(f, text='INDIETRO', command=back)
        button_back.pack(side=BOTTOM)
    button_avvio= Button(f, text='AVVIO', font=50, command=tab2)
    button_avvio.pack(side=TOP, pady=50)
    button_esci= Button(f, text='ESCI', command=f.quit)
    button_esci.pack(side=BOTTOM)
tab1()
f.mainloop()
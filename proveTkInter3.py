from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
#window.geometry("600x600")
window.title("PROVA")
window.resizable(False,False)
window.configure(background="white")
stato = Label(window, text="non avviato", font=(30))
stato.grid(row=1, column=0,columnspan=2)
photo = PhotoImage(file = "mits.png")
window.iconphoto(False, photo)

def processo_iniziato(): 
    global stato
    stato.destroy()
    stato=Label(text=("INIZIATO"), font=(30))
    stato.grid(row=1, column=0,columnspan=2)

def processo_stop():
    global stato
    stato.destroy()
    stato=Label(text=("FINITO"), font=(30))
    stato.grid(row=1, column=0,columnspan=2)
    
    

my_img=ImageTk.PhotoImage(Image.open("logo.png"))
img=Label(image=my_img)
img.configure(background="white")
img.grid(row=0,column=0,columnspan=2)

start_button = Button(text="INIZIA PROCESSO", bd=5, command=processo_iniziato)
start_button.grid(row=2, column=0)

stop_button = Button(text="FERMA IL PROCESSO", bd=5, command=processo_stop)      #bd per il bordo
stop_button.grid(row=2, column=1)

quit_button = Button(text="esci", command=window.quit)
quit_button.grid(row=3,column=0, columnspan=2)

window.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

window = tk.Tk()
#window.geometry("600x600")
window.title("PROVA")
window.resizable(False,False)
window.configure(background="white")
stato = tk.Label(window, text="non avviato", font=(30))
stato.grid(row=3, column=0,columnspan=2)
photo = tk.PhotoImage(file = "mits.png")
window.iconphoto(False, photo)

def processo_iniziato(): 
    global stato
    stato.destroy()
    stato=tk.Label(text=("INIZIATO"), font=(30))
    stato.grid(row=3, column=0,columnspan=2)
    messagebox.showwarning('','Macchina in funzione!')
    
def processo_stop():
    global stato
    stato.destroy()
    stato=tk.Label(text=("FINITO"), font=(30))
    stato.grid(row=3, column=0,columnspan=2)
    messagebox.showwarning('','Macchina fermata!')
    
    

my_img=ImageTk.PhotoImage(Image.open("logo.png"))
img=tk.Label(image=my_img)
img.configure(background="white")
img.grid(row=0,column=0,columnspan=2)

start_button = tk.Button(text="INIZIA PROCESSO", bd=5, command=processo_iniziato)
start_button.grid(row=1, column=0)

stop_button = tk.Button(text="FERMA IL PROCESSO", bd=5, command=processo_stop)      #bd per il bordo
stop_button.grid(row=1, column=1)

quit_button = tk.Button(text="esci", command=window.quit)
quit_button.grid(row=0,column=2, rowspan=3)

if __name__ == "__main__":
    window.mainloop()
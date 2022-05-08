import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
#window.geometry("600x600")
window.title("PROVA")
#window.resizable(False,False)
window.configure(background="white")
stato = tk.Label(window)

def processo_iniziato(): 
    global stato
    stato.destroy()
    stato=tk.Label(text=("iniziato"))
    stato.grid(row=3, column=0,columnspan=2)
    
def processo_stop():
    global stato
    stato.destroy()
    stato=tk.Label(text=("finito"))
    stato.grid(row=3, column=0,columnspan=2)
    
    

my_img=ImageTk.PhotoImage(Image.open("logo.png"))
img=tk.Label(image=my_img)
img.configure(background="white")
img.pack()

start_button = tk.Button(text="INIZIA PROCESSO", command=processo_iniziato)
start_button.grid(row=1, column=0)

stop_button = tk.Button(text="FERMA IL PROCESSO", command=processo_stop)
stop_button.grid(row=1, column=1)

quit_button = tk.Button(text="esci", command=window.quit)
quit_button.grid(row=0,column=2, rowspan=3)

if __name__ == "__main__":
    window.mainloop()
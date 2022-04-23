import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

window = tk.Tk()
#window.geometry("600x600")
window.title("PROVA")
window.resizable(False,False)
window.configure(background="white")



def processo_iniziato(): 
    stato=tk.Label(window, text=("BUONASERA"), font=(30))
    stato.pack()

stop_button = tk.Button(text="MONDOPIZZA", command=processo_iniziato())
stop_button.pack()

if __name__ == "__main__":
    window.mainloop()
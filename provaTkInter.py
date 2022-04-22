import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
#window.geometry("600x600")
window.title("PROVA")
#window.resizable(False,False)
window.configure(background="white")

my_img=ImageTk.PhotoImage(Image.open("logo.png"))
img=tk.Label(image=my_img)
img.configure(background="white")
img.grid(row=0,column=0)

quit_button = tk.Button(text="esci", command=window.quit)
quit_button.grid(row=0,column=1)

if __name__ == "__main__":
    window.mainloop()
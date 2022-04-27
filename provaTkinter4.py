from tkinter import *           #da tk importa tutto
from tkinter import messagebox
import time

window=Tk()                     #

logoIts=PhotoImage(file='logo.png')  #prendo il logo, disponibile come logoIts

"""PICCOLI APPUNTI PER MIGLIORIE
nelle proprietà dei pulsanti -> acriveforeground e activebackground cambiano il colore del pulsante premuto


"""

def zioPera():
    zp=Tk()
    siu=Label(zp, text=("Zio Pera") )
    siu.pack()
    siu.after(1500, lambda:zp.destroy())
    zp.mainloop()


label = Label(window, text="PROJECT WORK", image=logoIts, font=('Arial',35,'bold'),compound='bottom', bg='pink')   #compound mostra l'immagine nella direzione indicata relativa al testo

label.pack()                                                                                                 #ricordarselo, paccka la label nella window

bt = Button(text='zio pera', command=zioPera)
bt.pack()


window.mainloop()



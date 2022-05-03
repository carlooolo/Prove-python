from tkinter import *            
from tkinter import messagebox
import time
import tkinter.font as font 
import serial
import time

f=Tk()
f.title('Pannello di Controllo')
f.geometry('1024x550')
f.resizable(0, 0)
photo = PhotoImage(file = "mits.png") #cambiare in base al tuo nome
f.iconphoto(False, photo)
photo2= PhotoImage(file='logo.png') #cambiare in base al tuo nome
label=Label(f, text="PROJECT WORK", image=photo2, font=('Arial',35,'bold'),compound='bottom')
label.pack()
stato = Label(text="non avviato", font=(50))
myfont= font.Font(size=25)
myfont2= font.Font(size=15)
myfont3= font.Font(size=20)

#if __name__ == '__main__':
#    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#    ser.reset_input_buffer()

def tab1():
    def tab2():
        def set_text_by_start():
            global stato
            stato.destroy()
            stato=Label(text=("INIZIATO"))
            stato['font']= myfont3
            stato.pack()
            '''ser.write(b"1")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)'''
        def set_text_by_stop():
            global stato
            stato.destroy()
            stato=Label(text=("TERMINATO"), font=(50))
            stato.pack()
            '''ser.write(b"0")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)'''
        stato.pack()
        
        button_avvio.destroy()
        button_esci.destroy()
        button_start= Button(f, text='START', background='#b0bbc1', activebackground='#78d6ff', command=set_text_by_start)
        button_start.pack(side=LEFT, padx=175)
        button_start['font']= myfont3
        button_stop= Button(f, text='STOP', background='#b0bbc1', activebackground='#78d6ff', command=set_text_by_stop)
        button_stop.pack(side=RIGHT, padx=175)
        button_stop['font']= myfont3
        def back():
            button_start.destroy()
            button_back.destroy()
            button_stop.destroy()
            stato.destroy()
            tab1()
        button_back= Button(f, text='INDIETRO', background='#b0bbc1', activebackground='#78d6ff', command=back)
        button_back.pack(side=BOTTOM)
        button_back['font']= myfont2
    button_avvio= Button(f, text='AVVIO', background='#b0bbc1', activebackground='#78d6ff', command=tab2)
    button_avvio.pack(side=TOP, pady=100)
    button_avvio['font']= myfont
    button_esci= Button(f, text='ESCI', background='#b0bbc1', activebackground='#78d6ff', command=f.quit)
    button_esci.pack(side=BOTTOM)
    button_esci['font']= myfont2    
tab1()
f.mainloop()
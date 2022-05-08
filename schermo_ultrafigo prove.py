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
myfont= font.Font(size=25)
myfont2= font.Font(size=15)
myfont3= font.Font(size=20)

if __name__ == '__main__':
    ser = serial.Serial('COM7', 9600, timeout=1)
    ser.reset_input_buffer()

def tab1():
    
    def tab2():
        
        def set_text_by_start():
            sample_text.delete(0,"end")
            sample_text.insert(0, "Macchina in funzione!")
            sample_text['font']= myfont3
            ser.write(b"1")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
            #sample_text.pack(side=TOP, pady=75)
        
        def set_text_by_stop():
            sample_text.delete(0,"end")
            sample_text.insert(0, "Macchina fermata!")
            sample_text['font']= myfont3
            ser.write(b"2")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
        
        sample_text = Entry(f, background='#d7dde0')
        sample_text['font']= myfont3
        sample_text.pack()
        button_avvio.destroy()
        button_esci.destroy()
        button_start= Button(f, text='START', background='#b0bbc1', activebackground='#78d6ff', command=set_text_by_start)
        button_start.pack(side=LEFT, padx=175)
        button_start['font']= myfont3
        button_stop= Button(f, text='STOP', background='#b0bbc1', activebackground='#78d6ff', command=set_text_by_stop)
        button_stop.pack(side=RIGHT, padx=175)
        button_stop['font']= myfont3
        
        def back():
            ser.write(b'2')
            time.sleep(1)

            button_start.destroy()
            button_back.destroy()
            button_stop.destroy()
            sample_text.destroy()
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
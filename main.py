import tkinter as tk
from tkinter import *
from pyStandardGalacticAlphabet import SGA

sga = SGA()

label = None
window = tk.Tk()
window.title("Enchantment Translator")
window.geometry("1800x300")
window.resizable(height=False, width=False)
window['bg'] = '#c976fc'

#Read and translate the input
def printValue():
    global label
    string = en_text.get()
    en_to_sga = sga.encode(string)
    if label != None:
        remove_label()
    label = Label(window, text=f'{en_to_sga}', pady=20, bg='#c976fc', font= ("Arial", 25))
    label.pack()

def remove_label():
   global label
   label.pack_forget()

en_text = Entry(window)
en_text.pack(pady=30)

Button(
    window,
    text="Translate", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

window.mainloop()
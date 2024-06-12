import tkinter as tk
from constantes import style
from screens import *

class Manager(tk.Tk):

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.title("Calculadora Binaria")
        container = tk.Frame(self)
        container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        container.configure(background = style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, binario_octal, binario_decimal):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky = tk.NSEW)
        self.show_frame(Home)
            
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
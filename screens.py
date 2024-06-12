import tkinter as tk
from constantes import style

#Aqui se crean todas la ventanas

class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.calcuMode = tk.StringVar(self, value="Decimal")

        self.init_widgets()

    def move_to_binarioDecimal(self):
        self.controller.show_frame(binario_decimal)
    
    def move_to_binarioOctal(self):
        self.controller.show_frame(binario_octal)

    def move_salir(self):
        self.controller.destroy()
        

    def init_widgets(self):
        tk.Label(self,
                 text="Calculadora Binaria",
                 justify = tk.CENTER,
                 **style.STYLE
                 ).pack(
                     side= tk.TOP,
                     fill= tk.BOTH,
                     expand=True,
                     padx=22,
                     pady=11
                 )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionsFrame,
            text = "Seleccion la operacion que desee",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
                optionsFrame,
                text = "Binario a Decimal" ,
                command = self.move_to_binarioDecimal,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE,
            ).pack(
                side = tk.LEFT,
                fill = tk.X,
                expand=True,
                padx=5,
                pady=5
            )
        tk.Button(
                optionsFrame,
                text = "Binario a Octal" ,
                command = self.move_to_binarioOctal,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE,
            ).pack(
                side = tk.LEFT,
                fill = tk.X,
                expand=True,
                padx=5,
                pady=5
            )
        tk.Button(
                optionsFrame,
                text = "Salir" ,
                command = self.move_salir,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
                **style.STYLE,
            ).pack(
                side = tk.LEFT,
                fill = tk.X,
                expand=True,
                padx=5,
                pady=5
            )
               
            




class binario_decimal(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.resultado_var = tk.StringVar()

        self.init_widgets()

    def validar(self, valor):
        return all(char in '01' for char in valor)
    
    def binario_a_decimal(self):
        binario = self.entry.get()
        if binario:  # Asegurarse de que el campo de entrada no esté vacío
            try:
                decimal = int(binario, 2)
                self.resultado_var.set(f"Decimal: {decimal}")
            except ValueError:
                self.resultado_var.set("Entrada inválida")
        else:
            self.resultado_var.set("Por favor, ingrese un número binario")

    def move_salir(self):
        self.controller.show_frame(Home)
        self.resultado_var.set("")
        self.entry.delete(0, tk.END)
    
    def init_widgets(self):
        tk.Label(self,
                 text="Binario a Decimal",
                 justify = tk.CENTER,
                 **style.STYLE
                 ).pack(
                     side= tk.TOP,
                     fill= tk.BOTH,
                     expand=True,
                     padx=22,
                     pady=11
                 )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionsFrame,
            text = "Ingrese un numero binario",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        vcmd = (self.register(self.validar), '%P')
        self.entry = tk.Entry(
            optionsFrame,
            justify = tk.CENTER,
            **style.STYLE,
            validate="key",
            validatecommand=vcmd
        )
        self.entry.pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            optionsFrame,
            text = "Convertir",
            command = self.binario_a_decimal,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            **style.STYLE,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        tk.Label(
            optionsFrame,
            textvariable=self.resultado_var,
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            optionsFrame,
            text = "Salir",
            command = self.move_salir,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            **style.STYLE,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )
        
        


class binario_octal(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.resultado_var = tk.StringVar()

        self.init_widgets()

    def validar(self, valor):
        return all(char in '01' for char in valor)
    
    def binario_a_octal(self):
        binario = self.entry.get()
        if binario: 
            try:
                decimal = int(binario, 2)
                octal = oct(decimal)[2:] 
                self.resultado_var.set(f"Octal: {octal}")
            except ValueError:
                self.resultado_var.set("Entrada inválida")
        else:
            self.resultado_var.set("Por favor, ingrese un número binario")

    def move_salir(self):
        self.controller.show_frame(Home)
        self.resultado_var.set("")
        self.entry.delete(0, tk.END)
    
    def init_widgets(self):
        tk.Label(self,
                 text="Binario a Octal",
                 justify = tk.CENTER,
                 **style.STYLE
                 ).pack(
                     side= tk.TOP,
                     fill= tk.BOTH,
                     expand=True,
                     padx=22,
                     pady=11
                 )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = style.COMPONENT)
        optionsFrame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=22,
            pady=11
        )
        tk.Label(
            optionsFrame,
            text = "Ingrese un numero binario",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        vcmd = (self.register(self.validar), '%P')
        self.entry = tk.Entry(
            optionsFrame,
            justify = tk.CENTER,
            **style.STYLE,
            validate="key",
            validatecommand=vcmd
        )
        self.entry.pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            optionsFrame,
            text = "Convertir",
            command = self.binario_a_octal,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            **style.STYLE,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )

        tk.Label(
            optionsFrame,
            textvariable=self.resultado_var,
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            optionsFrame,
            text = "Salir",
            command = self.move_salir,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            **style.STYLE,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx=22,
            pady=11
        )


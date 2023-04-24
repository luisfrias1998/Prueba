import tkinter as tk

class FormularioLogin(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        #self.pack()

        self.inicializar_gui()

    def inicializar_gui(self):
        tk.Label(self.master, text='¿Cual es tu nombre?:').grid(row=0, column=0)
        self.nombre = tk.StringVar()
        tk.Entry(self.master, textvariable=self.nombre).grid(row=0, column=1)


        tk.Label(self.master, text='¿Cual es tu primer apellido?:').grid(row=1, column=0)
        self.apellido1 = tk.StringVar()
        tk.Entry(self.master, textvariable=self.apellido1).grid(row=1, column=1)

        tk.Label(self.master, text='¿Cual es tu segundo apellido?:').grid(row=2, column=0)
        self.apellido2 = tk.StringVar()
        tk.Entry(self.master, textvariable=self.apellido2).grid(row=2, column=1)

def main():
    app = tk.Tk()
    app.title('Formulario Login')
    app.geometry('350x250')

    ventana = FormularioLogin(app)
    ventana.mainloop()

if __name__ == "__main__":
    main()
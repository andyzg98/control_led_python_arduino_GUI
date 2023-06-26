import tkinter as tk


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana = tk.Tk()
        self.ventana.title("Control de Luces LED")

        self.estado_luces = []
        self.crear_interfaz()

    def crear_interfaz(self):
        # Código para crear la interfaz gráfica usando Tkinter
        # Esto puede incluir etiquetas, botones y otros elementos de GUI
        # para mostrar y controlar el estado de las luces LED

        # Por ejemplo, puedes utilizar Checkbuttons para permitir al usuario
        # seleccionar qué luces desea encender o apagar
        for i in range(4):
            estado = tk.BooleanVar()
            self.estado_luces.append(estado)
            checkbox = tk.Checkbutton(self.ventana, text=f"Luz {i+1}", variable=estado)
            checkbox.pack()

        boton_encender = tk.Button(self.ventana, text="Encender", command=self.encender_luces)
        boton_encender.pack()

        boton_apagar = tk.Button(self.ventana, text="Apagar", command=self.apagar_luces)
        boton_apagar.pack()

    def encender_luces(self):
        luces_encendidas = [i+1 for i, estado in enumerate(self.estado_luces) if estado.get()]
        self.controlador.encender_luces(luces_encendidas)

    def apagar_luces(self):
        luces_apagadas = [i+1 for i, estado in enumerate(self.estado_luces) if not estado.get()]
        self.controlador.apagar_luces(luces_apagadas)

    def iniciar(self):
        self.ventana.mainloop()

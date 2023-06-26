class Controlador:
    def __init__(self, modelo):
        self.modelo = modelo

    def encender_luces(self, luces):
        for luz in luces:
            self.modelo.encender_luz(luz)

    def apagar_luces(self, luces):
        for luz in luces:
            self.modelo.apagar_luz(luz)

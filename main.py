from vista import Vista
from modelo import Modelo
from controlador import Controlador


if __name__ == "__main__":
    modelo = Modelo()
    controlador = Controlador(modelo)
    vista = Vista(controlador)

    vista.iniciar()

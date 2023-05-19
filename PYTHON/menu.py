import os
from lenguaje import mostrar_lenguaje
from analizar import analizar_cadena, analizar_cadena_pap
from ejemplo import  cadena_ejemplo
import os


menu = """
    1 - Mostrar Lenguaje.
    2 - Analizar Cadena Completa.
    3 - Analizar Cadena Paso a Paso.
    4 - Cadena Ejemplo.
    5 - Salir 
"""

def pause():
    return input("\nPRESIONE UNA TECLA PARA CONTINUAR")

def limpiar_terminal():
    if os.name == "nt":  #WINDOWS
        return os.system("cls")
    else:  # LINUX
        return os.system("clear")


flag = True
while flag:
    print(menu)
    eleccion = input("Elija una ocion: ")

    match eleccion:

        case "1": 
                mostrar_lenguaje()
                pause()
                limpiar_terminal()

        case "2": 
                analizar_cadena()
                pause()
                limpiar_terminal()
                
        case "3": 
                analizar_cadena_pap()
                pause()

        case "4": 
                cadena_ejemplo()
                pause()
                limpiar_terminal()

        case "5": flag = False

        case _: 
              print("Opcion incorrecta, vuelva a elegir")
              limpiar_terminal()


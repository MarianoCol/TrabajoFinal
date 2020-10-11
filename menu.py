from ahorcadoService import AhorcadoSevice

class Menu():
    def __init__(self):
        pass

    def menuAhorcado(self):
        print("\n------AHORCADO-----")
        print("\nCantidad de jugadores")
        print("1 ---> Un jugador")
        print("2 ---> Dos jugadores")
        print("3 ---> Finalizar")
        return int(input("Ingrese una opcion: ")

if __name__ == '__main__':
    menu = Menu()
    bucle = True
    while bucle == True:
        seleccion = menu.menuAhorcado()
        if seleccion == 1:
            service = AhorcadoSevice()
        if seleccion == 2:
            pass
        if seleccion == 3:
            bucle = False


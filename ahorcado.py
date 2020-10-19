from partida import Partida
from servicesPartidas import ServicesPartidas

class Ahorcado():
    pass

    def menuAhorcado(self):
        print("1 ---> Un jugador")
        print("2 ---> Dos jugadores")
        print("3 ---> Salir")
        return int(input("\nElija una opcion: "))

    def un_jugador(self):
        servis = ServicesPartidas()
        nombreJugador = str(input("Ingrese su nombre: "))
        intentosJugador = int(input("Ingrese la dificultad: "))
        p = servis.iniciar_partida(nombreJugador, intentosJugador,'','')
        for i in range(0, p.intentos):
            letra = str(input("\nIngrese una letra para adivinar: "))
            if letra == 'salir':
                return True
            respuesta = servis.intentar_letra(p, letra.upper())
            print(respuesta)
            if respuesta == 'Gano' or respuesta == 'Perdio':
                return True

    def dos_jugadores(self):
        pass

if __name__ == "__main__":
    ahorcado = Ahorcado()
    Bucle = True
    while Bucle == True:
        opcion = ahorcado.menuAhorcado()
        if opcion == 1:
            ahorcado.un_jugador()
            Bucle = True
        if opcion == 2:
            ahorcado.dos_jugadores()
            Bucle = True
        if opcion == 3:
            Bucle = False

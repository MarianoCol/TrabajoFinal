from repositorio import Repositorio
from partida import Partida

class ServicesPartidas():
    pass

    def iniciar_partida(self, nombre, intentos, palabra, tipoPalabra):
        intentosTotales = intentos * len(list(palabra))
        partida = Partida(palabra, tipoPalabra, intentosTotales, nombre)
        return partida

        
class Partida():

    def __init__(self, palabra, tipo_palabra, intentos, nombre_jugador):
        self._palabra = list(palabra.upper())
        self._tipo_palabra = tipo_palabra.upper()
        self._intentos = intentos
        self._nombre_jugador = nombre_jugador.upper()
        self._palabra_aciertos = list()

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, palabra):
        self._palabra = palabra

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        self._tipo_palabra = tipo_palabra

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, intentos):
        self._intentos = intentos

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        self._nombre_jugador = nombre_jugador

"""
    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, palabra, palabra_aciertos):
        for i in range(len(palabra)):
            self._palabra_aciertos = palabra_aciertos.append(None)
"""
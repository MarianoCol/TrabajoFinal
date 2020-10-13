class Partida():

    def __init__(self, palabra='', tipo_palabra='', intentos=0, nombre_jugador='', palabra_aciertos=[None]):
        self.palabra = palabra
        self.tipo_palabra = tipo_palabra.upper()
        self.intentos = intentos
        self.nombre_jugador = nombre_jugador.upper()
        self.palabra_aciertos = palabra_aciertos

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, palabra):
        self._palabra = list(palabra.upper())

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

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, palabra_aciertos):
        self._palabra_aciertos = palabra_aciertos * len(self._palabra)

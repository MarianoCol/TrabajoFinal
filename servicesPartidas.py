import random
from repositorio import Repositorio
from partida import Partida
import json

with open('palabras.json', 'r') as f:
    palabras_json = json.load(f)

#palabras = {0: {'palabra': 'peru', 'tipoPalabra': 'paises'}, 1: {'palabra': 'python', 'tipoPalabra': 'lenguaje de programacion'}, 2: {'palabra': 'dota', 'tipoPalabra': 'videojuegos'}}

class ServicesPartidas():
    pass

    def iniciar_partida(self, nombre, intentos, palabra, tipoPalabra):
        if palabra == '' and tipoPalabra == '':
            if intentos < 1 or intentos > 10:
                raise ValueError
            else:
                key = random.randint(1, len(palabras_json))
                key -= 1
                numPalabra = palabras_json['%s'% key]
                palabra = numPalabra['palabra']
                tipoPalabra = numPalabra['tipoPalabra']
                print("La palabra a adivinar esta relacionada con: ", tipoPalabra, palabra)
                intentosTotales = intentos * len(list(palabra))
                partida = Partida(palabra, tipoPalabra, intentosTotales, nombre)
                print("\nLa palabra tiene ", len(palabra), " letras")
                print("\n", partida.palabra_aciertos)
                return partida
        else:
            print("La palabra a adivinar esta relacionada con: ", tipoPalabra)
            intentosTotales = intentos * len(list(palabra))
            partida = Partida(palabra, tipoPalabra, intentosTotales, nombre)
            print("\nLa palabra tiene ", len(palabra), " letras")
            print("\n", partida.palabra_aciertos)
            return partida

    def get_random_palabra(self):
        key = random.randint(0, len(palabras_json))
        key -= key
        numPalabra = palabras_json['%s'% key]
        return numPalabra

    def intentar_letra(self, partida, letra):
        contador = 0
        a = False
        for l in partida.palabra: 
            if l == letra:
                partida.palabra_aciertos[contador] = letra
                a = True  
            contador += 1
        print(partida.palabra_aciertos) 
        if partida.palabra_aciertos == partida.palabra:
            partida.intentos -= 1
            return "Gano"
        elif a != True:
            partida.intentos -= 1 
            if partida.intentos == 0:
                return "Perdio"
            else:
                return "Continua"
        else:
            partida.intentos -= 1
            return "Continua"        

#if __name__ == "__main__": 
 #       key = random.randint(1, len(palabras_json))
   #     numPalabra = palabras_json
  #      print(numPalabra['%s'% key])
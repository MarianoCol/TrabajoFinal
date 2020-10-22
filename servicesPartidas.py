import random
from repositorio import Repositorio
from partida import Partida
import json

with open('palabras.json', 'r') as f:
    palabras_json = json.load(f)


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
                tipoPalabra = numPalabra['tipo_palabra']
                print("La palabra a adivinar esta relacionada con: ", tipoPalabra, palabra)
                intentosTotales = intentos * len(list(palabra))
                partida = Partida(palabra, intentosTotales, tipoPalabra, nombre)
                print("\nLa palabra tiene ", len(palabra), " letras")
                print("\n", partida._palabra_aciertos)
                return partida
        else:
            print("La palabra a adivinar esta relacionada con: ", tipoPalabra)
            intentosTotales = intentos * len(list(palabra))
            partida = Partida(palabra, intentosTotales, tipoPalabra, nombre)
            print("\nLa palabra tiene ", len(palabra), " letras")
            print("\n", partida._palabra_aciertos)
            return partida

    def get_random_palabra(self):
        key = random.randint(0, len(palabras_json))
        key -= key
        numPalabra = palabras_json['%s'% key]
        return numPalabra

    def intentar_letra(self, partida, letra):
        contador = 0
        a = False
        for l in partida._palabra: 
            if l == letra:
                partida._palabra_aciertos[contador] = letra
                a = True  
            contador += 1
        print(partida._palabra_aciertos) 
        if partida._palabra_aciertos == partida._palabra:
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
            if partida.intentos == 0:
                return "Perdio"
            else:
                return "Continua"        

#if __name__ == "__main__": 
 #       key = random.randint(1, len(palabras_json))
   #     numPalabra = palabras_json
  #      print(numPalabra['%s'% key])
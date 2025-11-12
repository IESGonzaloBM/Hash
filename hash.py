
import hashlib
from sys import argv, exit
import json
import math
import time

def get_param():

    if len(argv) != 3:
        raise Exception("[ERROR]: Formato incorrecto: py hash.py <longitud>")

    if argv[3] not in "0123456789":
        raise Exception("[ERROR]: La longitud debe de ser un numero [0, 9]")


    return int(argv[3])



def metrics(length: int) -> tuple[float, float]:
    # Entropia
    # Combinatoria y Permutaciones => Deberia ser solo combinatoria donde el orden no importa
    # Teoria de conjuntos


    combinatoria = math.factorial(72) / math.factorial(length) * math.factorial(72 - length)
    entropia = length * math.log(72, 2)

    return round(combinatoria, 2), round(entropia, 2)

def password(length: int, ihash): # : hashlib._Hash = hashlib.sha1(b"hola")
    start_time = time.time()

    caracteres = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    numeros = "0123456789"
    caracteres_especiales = "!@?ñ/()%&$"

    total_caracteres = caracteres + numeros + caracteres_especiales # 72 caracteres deberian ser
    total_caracteres = "qrty$"
    correcto = False
    password_list = [total_caracteres[0] for i in range(length)]
    puntero: int = length - 1
    rango_puntero: int = length - 1
    while puntero <= length and correcto == False:
        for caracter in total_caracteres:
            password_list[puntero] = caracter

            password_str = "".join(password_list)
            print(password_str)
            hash = hashlib.sha256(password_str.encode("utf-8"))

            if ihash == hash:
                correcto = True
                break

            if password_list[puntero] == "$" and correcto == False:
                if puntero == rango_puntero: # puntero == enumerate([i for i in range(len(password_list), 0, -1)])     password_list[rango_puntero] == "$"
                    rango_puntero -= 1
                else:
                    puntero -= 1
                puntero -= length - rango_puntero

    end_time = time.time()
    print(f"\nTiempo de ejecución: {end_time - start_time:.5f} segundos")

if __name__ == "__main__":
    password(4, hashlib.sha256("holabuenas".encode("utf-8")).hexdigest())
    try:
        # length = get_param()
        # combinatoria, entropia = metrics(length)
        pass
    except Exception as error:
        print(error)
    except KeyboardInterrupt:
        print("\nSalida por usuario")
        exit(0)

import hashlib
from sys import argv, exit
import json
import math
import time

def get_param() -> tuple[int, str]:
    """
    Comprueba y gestiona los posibles errores en la input por el usuario en terminal

    Returns:
        int: Longitud de la contraseña
    """

    if len(argv) != 3:
        raise Exception("[ERROR]: Formato incorrecto: py/python/python3 hash.py <longitud> <Hash256>")
    elif argv[1] not in "0123456789":
        raise Exception("[ERROR]: La longitud debe de ser un numero [0, 9]")
    # Para saber si el Hash esta en formato AES-256 pasamos a bytes el argumento en hexadecimal y por necesidad debe de ser 32 bytes
    elif len(bytes.fromhex(argv[2])) != 32:
        raise Exception("[ERROR]: Introduzca el Hash en formato AES-256")

    return int(argv[1]), argv[2]


def config() -> str:
    """
    Obtenemos los caracteres en `config.json`. Por comodidad para poder cambiarlos por el usuario los he definido en json.
    He investigado sobre como cargar los datos de un json en internet.

    Returns:
        tuple[hashlib._Hash, str]: Devolvemos el Hash256 a forzar y todos los caracteres que necesitamos
    """

    with open("config.json", "r") as config:
        data = json.load(config)

    total_caracteres = data["caracteres"]["basicos"] + data["caracteres"]["numeros"] + data["caracteres"]["especiales"]

    return total_caracteres


def metrics(length: int) -> tuple[float, float]:
    """
    Imprime en pantalla las posibles permutaciones, entropia y orden de complejidad

    Args:
        length (int): longitud de la palabra
    Returns:
        tuple[float, float]: Devolvemos las permutaciones y la entropia en caso de usarlas
    """

    permutaciones = math.factorial(72) / (math.factorial(length) * math.factorial(72 - length))
    entropia = length * math.log(72, 2)

    print("================================================================================================")
    print(f"||  Permutaciones: {round(permutaciones, 2)}     Entropia: {round(entropia, 2)}     Orden de complejidad exponencial: O(72^{length}))  ||")
    print("================================================================================================\n")

    return round(permutaciones, 2), round(entropia, 2)


def password(ihash: str, length: int, caracteres: str):
    """
    Itera sobre todas las posibilidades ante la longitud de una contraseña y una serie de caracteres hasta dar con ella.
    El crecimiento de esta funcion es exponencial O(72^length)

    Args:
        length (int): Logitud de la contraseña
        ihash: Hash256 dado para romper por brute-force
    """

    def incrementar() -> bool:
        """
        Incremento el cual avanza desde [length, 0] asignando el siguiente carácter posible.

        Args:
            password_list (list): Lista de caracteres que representa la contraseña actual.
            total_caracteres (str): Cadena con todos los caracteres posibles.
        Returns:
            bool: True si se pudo avanzar, False si se agotaron las combinaciones.
        """

        puntero: int = length - 1
        while puntero >= 0:
            index = caracteres.index(password_list[puntero])

            # Si aun hay carácter siguiente, lo asignamos y terminamos
            if index + 1 < len(caracteres):
                password_list[puntero] = caracteres[index + 1]
                return True
            else:
                # Si estamos en el último carácter, lo reiniciamos (vuelve al inicio) y llevamos el puntero a la izquierda
                password_list[puntero] = caracteres[0]
                puntero -= 1
        # Si salimos del while, no hay más combinaciones posibles
        return False

    finish = False
    password_list = [caracteres[0] for i in range(length)]

    start_time = time.time()
    while not finish:
        password_str = "".join(password_list)
        print(f"\rVerificando: {password_str}", end="")

        hash = hashlib.sha256(password_str.encode("utf-8")).hexdigest()

        if ihash == hash:
            print(f"\nEncontrada: {password_str}")
            finish = True
            break # Me ahorro seguir iterando

        # Avanzar el puntero desde la derecha al estilo binario para cubrir todas las posibilidades (0000, 0001, 0010, 0011, 0100, 0101, ...)
        if not incrementar():
            finish = True

    end_time = time.time()
    print(f"\nTiempo de ejecucion: {end_time - start_time:.5f} segundos")

if __name__ == "__main__":
    try:
        length, hash = get_param()
        caracteres = config()
        metrics(length)
        password(hash, length, caracteres)
    except Exception as error:
        print(error)
    except KeyboardInterrupt:
        print("\nSalida por usuario")
        exit(1)

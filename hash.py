
import hashlib
from sys import argv, exit
import json
import math
import time

def get_param() -> int:
    """
    Comprueba y gestiona los posibles errores en la input por el usuario en terminal

    Returns:
        int: Longitud de la contraseña
    """

    if len(argv) != 2:
        raise Exception("[ERROR]: Formato incorrecto: py hash.py <longitud>")

    if argv[1] not in "0123456789":
        raise Exception("[ERROR]: La longitud debe de ser un numero [0, 9]")

    return int(argv[1])


def config() -> tuple[str, str]:
    """
    Obtenemos los datos variables de `config.json`

    Returns:
        tuple[hashlib._Hash, str]: Devolvemos el Hash256 a forzar y todos los caracteres que necesitamos
    """

    with open("config.json", "r") as config:
        data = json.load(config)

    total_caracteres = data["caracteres"]["basicos"] + data["caracteres"]["numeros"] + data["caracteres"]["especiales"] # 72 caracteres => O(r^n) = O(72^length)

    return data["hash"], total_caracteres


def metrics(length: int) -> tuple[float, float]:
    # Entropia
    # Combinatoria y Permutaciones => Deberia ser solo combinatoria donde el orden no importa
    # Teoria de conjuntos

    combinatoria = math.factorial(72) / math.factorial(length) * math.factorial(72 - length)
    entropia = length * math.log(72, 2)

    print("=====================================================================")
    print(f"||  Combinatoria: {round(combinatoria, 2)}     Entropia: {round(entropia, 2)}      ||")
    print("=====================================================================\n")


    return round(combinatoria, 2), round(entropia, 2)


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
                # Si estamos en el último carácter, reiniciamos este y llevamos al de la izquierda
                password_list[puntero] = caracteres[0]
                puntero -= 1
        # si salimos del while, no hay más combinaciones (agotado)
        return False

    finish = False
    password_list = [caracteres[0] for i in range(length)]


    # Bucle principal: itera hasta encontrar o agotar combinaciones
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
    print(f"\nTiempo de ejecución: {end_time - start_time:.5f} segundos")

if __name__ == "__main__":
    length = get_param()
    hash, caracteres = config()
    metrics(length)
    password(hashlib.sha256("n6$h".encode("utf-8")).hexdigest(), length, caracteres)
    try:
        pass
    except Exception as error:
        print(error)
    except KeyboardInterrupt:
        print("\nSalida por usuario")
        exit(1)

# Comprobacion de IP y MAC (Python) — README

> CLI que dada una longitud y Hash256 por terminal en formato: py/python/python3 hash.py <longitud> <Hash256>, comprueba todas las posibles combinaciones en esa longitud
> con los caracteres en `config.json` por si se quieren cambiar y lo transforma a Hash256 comparandolo con el Hash256 que queremos averiguar dado por teminal.

---

## 1) Descripción del módulo

Este proyecto itera sobre cada probabilidad dado los caractere, longitud y Hash hasta dar con el Hash correcto
- El comando sigue el siguiente formato: `py/python/python3 hash.py <longitud> <Hash256>`
- La longitud debe de ser un numero entero
- El Hash debe de estar en formato AES-256
---

## 2) Requisitos

- **Python 3.10 o superior**.
- **Sin dependencias externas obligatorias.**
- Si en algún momento se añaden librerías, se listarán en el archivo **`dependecias.txt`**

---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu (y derivados)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

#### Fedora
```bash
sudo dnf install -y python3 python3-pip python3-virtualenv
python3 --version
python3 -m pip --version
```

#### Arch/Manjaro
```bash
sudo pacman -S --needed python python-pip
python --version
python -m pip --version
```

> **Entorno virtual (opcional recomendado)**
```bash
python3 -m venv .venv
# Activar:
# Linux/macOS:
source .venv/bin/activate
# (Salir: 'deactivate')
```

### 3.2 Windows

#### Opción A — Microsoft Store
1. Abrir **Microsoft Store**, buscar **Python 3.x** (Python Software Foundation).
2. Instalar y verificar:
```powershell
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descargar desde **https://www.python.org/downloads/** el instalador de Python 3.x.
2. **Marcar** “**Add Python to PATH**” durante la instalación.
3. Verificar:
```powershell
py --version
py -m pip --version
```

> **Entorno virtual (opcional)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
# (Salir: 'deactivate')
```

---

## 4) Ejecución del módulo

### Sintaxis general
```bash
python hash.py <longitud> <Hash256>
```
- `hash.py` archivo `.py` donde esta el codigo
- `longitud` longitud de la palabra en numeros enteros

> En Windows puedes usar `py` en lugar de `python`.
> En Linux, si conviven varias versiones, usa `python3`.

### Casos de prueba

```bash
# Linux/macOS
python hash.py 4 7c9e7c1494b2684ab7c19d6aff737e460fa9e98d5a234da1310c97ddf5691834
```
Salida esperada:
```
================================================================================================
||  Combinatoria: 1028790.0     Entropia: 24.68     Orden de complejidad exponencial: O(72^4))  ||
================================================================================================

Verificando: pepe
Encontrada: pepe

Tiempo de ejecucion: <tiempo_varible> segundos
```

## 6) Mensajes de error y códigos de salida

- **Formato en terminal incorrecto** ->
  - Mensaje: `[ERROR]: Formato incorrecto: py/python/python3 hash.py <longitud> <Hash256>`
- **Formato Hash incorrecto** ->
  - Mensaje: `[ERROR]: Introduzca el Hash en formato AES-256` →
- **Formato numero incorrecto** ->
  - Mensaje: `[ERROR]: La longitud debe de ser un numero [0, 9]`
---

## 7) Problemas frecuentes (FAQ)

- **“python: command not found” / “py no se reconoce”** → Instala Python o ajusta el **PATH** (ver sección 3).
- **“pip no se reconoce”** → Usa `python -m pip` (o `py -m pip` en Windows).

---
## 9) Protección y verificación de datos

Podemos observar como en funcion del crecimiento de los caracteres y la longitud el tiempo crece de forma exponencial.
Por lo tanto, podemos decir que el Orden Computacional/Complejidad es exponencial `O(n^r)`. Procedo a definir formalmente las
expresiones matematicas usadas.

- ### Permutacion definicion formal:
  - En el Analisis Combinatorio, las permutacion es una técnica para calcular el número de formas diferentes en que se pueden ordenar los elementos de un conjunto.
  -   ![permutaciones.png](img/permutaciones.png)
  - Una permutacion `n` sobre `r` es igual al factorial de `n` dividido por el factorial de `n - r`, donde `r <= n` tal que `r` y `n` pertenecen a los enteros. Donde en nuestro caso, `n = total de caracteres`y `r = longitud`
- ### Entropia definicion formal:
  - La entropía estadística en conjuntos se refiere a la medida cuantitativa de la incertidumbre, aleatoriedad o desorden en un sistema con múltiples estados posibles
- ### Orden de complejidad (grafica como ejemplo):
![ordenes.png](img/ordenes.png)

## 8) Comentarios
    
- He implementado el calculo de permutaciones y entropia para **"Evidenciar la dificultad y relevancia de la protección y verificación de datos en la comunicación cliente-servidor."**
- He usado JSON para que el usuario pueda cambiar de forma sencilla los caracteres usados y poder jugar con ellos


# Proyecto 3: Katas Python
# Hola Antonio :)
# Ejecutar con:  python katas.py

import math
from functools import reduce


# Kata 1: Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra en la cadena. Los
# espacios no deben ser considerados.
def frecuencia_letras(texto):
    """Devuelve un diccionario con la frecuencia de cada letra del texto."""
    frecuencias = {}
    for caracter in texto.lower():
        # Los espacios no cuentan.
        if caracter != " ":
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias


# Kata 2: Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map().
def doblar_valores(numeros):
    """Devuelve una nueva lista con el doble de cada número."""
    return list(map(lambda numero: numero * 2, numeros))


# Kata 3: Escribe una función que tome una lista de palabras y una palabra
# objetivo como parámetros. La función debe devolver una lista con todas las
# palabras de la lista original que contengan la palabra objetivo.
def buscar_palabras_que_contienen(palabras, objetivo):
    """Devuelve las palabras de la lista que contienen la palabra objetivo."""
    resultado = []
    for palabra in palabras:
        if objetivo.lower() in palabra.lower():
            resultado.append(palabra)
    return resultado


# Kata 4: Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map().
def diferencia_listas(lista1, lista2):
    """Resta posición a posición los valores de lista2 a los de lista1."""
    # zip() une las dos listas en pares: (lista1[0], lista2[0]), ...
    return list(map(lambda par: par[0] - par[1], zip(lista1, lista2)))


# Kata 5: Escribe una función que tome una lista de números como parámetro y un
# valor opcional nota_aprobado (por defecto 5). La función debe calcular la media
# de los números en la lista y determinar si la media es mayor o igual que
# nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario,
# "suspenso". La función debe devolver una tupla que contenga la media y el estado.
def evaluar_notas(notas, nota_aprobado=5):
    """Devuelve una tupla (media, "aprobado"/"suspenso")."""
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return round(media, 2), estado


# Kata 6: Escribe una función que calcule el factorial de un número de manera
# recursiva.
def factorial(numero):
    """Calcula el factorial de un número de forma recursiva."""
    if numero < 0:
        raise ValueError("El factorial no existe para números negativos.")
    # Caso base: 0! y 1! valen 1 y detienen la recursión.
    if numero == 0 or numero == 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return numero * factorial(numero - 1)


# Kata 7: Genera una función que convierta una lista de tuplas a una lista de
# strings. Usa la función map().
def tuplas_a_strings(lista_tuplas):
    """Convierte cada tupla en un string con sus elementos unidos por espacios."""
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))


# Kata 8: Escribe un programa que pida al usuario dos números e intente
# dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por
# cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando
# si la división fue exitosa o no.
def dividir_numeros_usuario():
    """Pide dos números al usuario y los divide controlando los errores."""
    try:
        dividendo = float(input("Introduce el primer número (dividendo): "))
        divisor = float(input("Introduce el segundo número (divisor): "))
        resultado = dividendo / divisor
    except ValueError:
        print("Error: debes introducir valores numéricos. La división no se ha realizado.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero. La división no se ha realizado.")
    else:
        print(f"División exitosa: {dividendo} / {divisor} = {round(resultado, 2)}")


# Kata 9: Escribe una función que tome una lista de nombres de mascotas como
# parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en
# España. La lista de mascotas a excluir es
# ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().
MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


def filtrar_mascotas_permitidas(mascotas):
    """Devuelve la lista de mascotas sin las prohibidas en España."""
    return list(filter(lambda mascota: mascota not in MASCOTAS_PROHIBIDAS, mascotas))


# Kata 10: Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el
# error adecuadamente.
class ListaVaciaError(Exception):
    """Se lanza cuando la lista está vacía."""
    pass


def promedio_con_excepcion(numeros):
    """Calcula el promedio; lanza ListaVaciaError si la lista está vacía."""
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)


# Kata 11: Escribe un programa que pida al usuario que introduzca su edad. Si el
# usuario ingresa un valor no numérico o un valor fuera del rango esperado (por
# ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
class EdadFueraDeRangoError(Exception):
    """Se lanza cuando la edad no está entre 0 y 120."""
    pass


def validar_edad(texto):
    """Convierte el texto en edad y comprueba que esté entre 0 y 120."""
    edad = int(texto)
    if edad < 0 or edad > 120:
        raise EdadFueraDeRangoError(f"La edad {edad} está fuera del rango permitido (0-120).")
    return edad


def pedir_edad_usuario():
    """Pide la edad al usuario hasta que introduzca un valor válido."""
    while True:
        try:
            edad = validar_edad(input("Introduce tu edad: "))
        except ValueError:
            print("Error: la edad debe ser un número entero. Inténtalo de nuevo.")
        except EdadFueraDeRangoError:
            print("Error: la edad debe estar entre 0 y 120. Inténtalo de nuevo.")
        else:
            print(f"Edad registrada correctamente: {edad} años.")
            break


# Kata 12: Genera una función que, al recibir una frase, devuelva una lista con
# la longitud de cada palabra. Usa la función map().
def longitud_palabras(frase):
    """Devuelve la longitud de cada palabra de la frase."""
    return list(map(len, frase.split()))


# Kata 13: Genera una función que, para un conjunto de caracteres, devuelva una
# lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden
# estar repetidas. Usa la función map().
def letras_mayus_minus(caracteres):
    """Devuelve tuplas (MAYÚSCULA, minúscula) sin letras repetidas."""
    # set() elimina las repetidas y sorted() las ordena (un set no tiene orden).
    letras_unicas = sorted(set([c.lower() for c in caracteres if c != " "]))
    return list(map(lambda letra: (letra.upper(), letra), letras_unicas))


# Kata 14: Crea una función que retorne las palabras de una lista que comiencen
# con una letra en específico. Usa la función filter().
def palabras_que_empiezan_por(palabras, letra):
    """Devuelve las palabras que empiezan por la letra indicada."""
    # palabra[0] es el primer carácter (indexación de strings).
    return list(filter(lambda palabra: palabra[0].lower() == letra.lower(), palabras))


# Kata 15: Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# Kata 16: Escribe una función que tome una cadena de texto y un número entero n
# como parámetros y devuelva una lista de todas las palabras que sean más largas
# que n. Usa la función filter().
def palabras_mas_largas_que(texto, n):
    """Devuelve las palabras del texto con más de n caracteres."""
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# Kata 17: Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función
# reduce().
def digitos_a_numero(digitos):
    """Convierte una lista de dígitos en el número que forman."""
    # En cada paso: acumulado * 10 + dígito  ->  5, 57, 572
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


# Kata 18: Escribe un programa en Python que cree una lista de diccionarios con
# información de estudiantes (nombre, edad, calificación) y use filter para
# extraer a los estudiantes con una calificación mayor o igual a 90.
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 78},
    {"nombre": "Marta", "edad": 21, "calificacion": 90},
    {"nombre": "Pedro", "edad": 23, "calificacion": 85},
    {"nombre": "Lucía", "edad": 19, "calificacion": 99},
]


def estudiantes_destacados(lista_estudiantes):
    """Devuelve los estudiantes con calificación mayor o igual a 90."""
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, lista_estudiantes))


# Kata 19: Crea una función lambda que filtre los números impares de una lista
# dada.
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# Kata 20: Para una lista con elementos de tipo integer y string, obtén una nueva
# lista solo con los valores int. Usa la función filter().
def solo_enteros(elementos):
    """Devuelve solo los elementos de tipo int."""
    return list(filter(lambda elemento: type(elemento) == int, elementos))


# Kata 21: Crea una función que calcule el cubo de un número dado mediante una
# función lambda.
def calcular_cubo(numero):
    """Calcula el cubo de un número usando una lambda."""
    cubo = lambda x: x ** 3
    return cubo(numero)


# Kata 22: Dada una lista numérica, obtén el producto total de los valores. Usa
# la función reduce().
def producto_total(numeros):
    """Multiplica todos los valores de la lista."""
    return reduce(lambda a, b: a * b, numeros)


# Kata 23: Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(palabras):
    """Concatena las palabras separándolas por un espacio."""
    return reduce(lambda frase, palabra: frase + " " + palabra, palabras)


# Kata 24: Calcula la diferencia total en los valores de una lista. Usa la
# función reduce().
def diferencia_total(numeros):
    """Resta sucesivamente los valores: numeros[0] - numeros[1] - ..."""
    return reduce(lambda a, b: a - b, numeros)


# Kata 25: Crea una función que cuente el número de caracteres en una cadena de
# texto dada.
def contar_caracteres(texto):
    """Cuenta el número de caracteres del texto."""
    return len(texto)


# Kata 26: Crea una función lambda que calcule el resto de la división entre dos
# números dados.
calcular_resto = lambda dividendo, divisor: dividendo % divisor


# Kata 27: Crea una función que calcule el promedio de una lista de números.
def calcular_promedio(numeros):
    """Calcula el promedio, o None si la lista está vacía."""
    if len(numeros) == 0:
        return None
    total = 0
    for numero in numeros:
        total += numero
    return total / len(numeros)


# Kata 28: Crea una función que busque y devuelva el primer elemento duplicado en
# una lista dada.
def primer_duplicado(elementos):
    """Devuelve el primer elemento repetido, o None si no hay ninguno."""
    # Guardo los ya vistos: el primero que repita es el resultado.
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# Kata 29: Crea una función que convierta una variable en una cadena de texto y
# enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.
def enmascarar(variable):
    """Convierte a texto y oculta con '#' todo menos los 4 últimos caracteres."""
    texto = str(variable)
    mascara = ""
    # Un '#' por cada carácter, menos los 4 últimos.
    for caracter in texto[:-4]:
        mascara += "#"
    return mascara + texto[-4:]


# Kata 30: Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    """Indica si dos palabras son anagramas."""
    p1 = palabra1.lower().replace(" ", "")
    p2 = palabra2.lower().replace(" ", "")
    # Mismas letras ordenadas = anagrama, y deben estar "en diferente orden".
    return sorted(p1) == sorted(p2) and p1 != p2


# Kata 31: Crea una función que solicite al usuario ingresar una lista de nombres
# y luego un nombre para buscar en esa lista. Si el nombre está en la lista,
# imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una
# excepción.
class NombreNoEncontradoError(Exception):
    """Se lanza cuando el nombre no está en la lista."""
    pass


def buscar_nombre(nombres, nombre_buscado):
    """Imprime un mensaje si encuentra el nombre; si no, lanza una excepción."""
    nombres_minusculas = [nombre.lower() for nombre in nombres]
    if nombre_buscado.lower() in nombres_minusculas:
        print(f"El nombre '{nombre_buscado}' ha sido encontrado en la lista.")
    else:
        raise NombreNoEncontradoError(f"El nombre '{nombre_buscado}' no está en la lista.")


def buscar_nombre_usuario():
    """Pide una lista de nombres y un nombre a buscar en ella."""
    texto = input("Introduce una lista de nombres separados por comas: ")
    nombres = [nombre.strip() for nombre in texto.split(",") if nombre.strip() != ""]
    nombre_buscado = input("¿Qué nombre quieres buscar? ").strip()
    buscar_nombre(nombres, nombre_buscado)


# Kata 32: Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre en la lista y devuelva el puesto del empleado si se encuentra;
# de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
empleados = [
    {"nombre": "Ana García López", "puesto": "Desarrolladora"},
    {"nombre": "Luis Martínez Ruiz", "puesto": "Diseñador"},
    {"nombre": "Marta Sánchez Gil", "puesto": "Jefa de proyecto"},
]


def buscar_puesto(nombre_completo, lista_empleados):
    """Devuelve el puesto del empleado, o un mensaje si no trabaja aquí."""
    for empleado in lista_empleados:
        if empleado["nombre"].lower() == nombre_completo.lower():
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


# Kata 33: Crea una función lambda que sume elementos correspondientes de dos
# listas dadas.
sumar_listas = lambda lista1, lista2: list(map(lambda par: par[0] + par[1], zip(lista1, lista2)))


# Kata 34: Crea la clase Arbol
#   - Define un árbol genérico con un tronco y ramas como atributos.
#   - Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama,
#     info_arbol.
#   - Código a seguir:
#       - Inicializar un árbol con un tronco de longitud 1 y una lista vacía de
#         ramas.
#       - Implementar el método crecer_tronco para aumentar la longitud del tronco
#         en una unidad.
#       - Implementar el método nueva_rama para agregar una nueva rama de
#         longitud 1 a la lista de ramas.
#       - Implementar el método crecer_ramas para aumentar en una unidad la
#         longitud de todas las ramas existentes.
#       - Implementar el método quitar_rama para eliminar una rama en una posición
#         específica.
#       - Implementar el método info_arbol para devolver información sobre la
#         longitud del tronco, el número de ramas y sus longitudes.
#   - Caso de uso:
#       a. Crear un árbol.
#       b. Hacer crecer el tronco una unidad.
#       c. Añadir una nueva rama.
#       d. Hacer crecer todas las ramas una unidad.
#       e. Añadir dos nuevas ramas.
#       f. Retirar la rama situada en la posición 2.
#       g. Obtener información sobre el árbol.
class Arbol:
    """Árbol genérico con un tronco y una lista de ramas."""

    def __init__(self):
        """Constructor: tronco de longitud 1 y sin ramas."""
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Añade una nueva rama de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina la rama de la posición indicada."""
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError(f"No existe ninguna rama en la posición {posicion}.")
        self.ramas.pop(posicion)

    def info_arbol(self):
        """Devuelve el tronco, el número de ramas y sus longitudes."""
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy(),
        }


# Kata 35: Crea la clase UsuarioBanco
#   - Representa a un usuario de un banco con su nombre, saldo y si tiene o no
#     cuenta corriente.
#   - Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
#   - Código a seguir:
#       - Inicializar un usuario con nombre, saldo y un indicador (True o False)
#         de cuenta corriente.
#       - Implementar retirar_dinero para sustraer dinero del saldo, lanzando un
#         error si no es posible.
#       - Implementar transferir_dinero para transferir dinero desde otro
#         usuario, lanzando un error en caso de fallo.
#       - Implementar agregar_dinero para aumentar el saldo del usuario.
#   - Caso de uso:
#       a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con
#          saldo inicial de 50, ambos con cuenta corriente.
#       b. Agregar 20 unidades al saldo de Bob.
#       c. Transferir 80 unidades de Bob a Alicia.
#       d. Retirar 50 unidades del saldo de Alicia.
class OperacionBancariaError(Exception):
    """Se lanza cuando una operación bancaria no se puede realizar."""
    pass


class UsuarioBanco:
    """Usuario de un banco con nombre, saldo y cuenta corriente."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        """Constructor: nombre, saldo y si tiene cuenta corriente (True/False)."""
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def comprobar_operacion(self, cantidad):
        """Comprueba que el usuario puede operar con esa cantidad."""
        if self.cuenta_corriente:
            if cantidad <= 0:
                raise OperacionBancariaError("La cantidad debe ser mayor que cero.")
        else:
            raise OperacionBancariaError(f"{self.nombre} no tiene cuenta corriente.")

    def agregar_dinero(self, cantidad):
        """Aumenta el saldo del usuario."""
        self.comprobar_operacion(cantidad)
        self.saldo += cantidad
        print(f"Se han añadido {cantidad} a {self.nombre}. Saldo actual: {self.saldo}")

    def retirar_dinero(self, cantidad):
        """Resta dinero del saldo; error si no hay saldo suficiente."""
        self.comprobar_operacion(cantidad)
        if cantidad > self.saldo:
            raise OperacionBancariaError(
                f"{self.nombre} no tiene saldo suficiente para retirar {cantidad} "
                f"(saldo actual: {self.saldo})."
            )
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro usuario hacia este usuario."""
        # Si el otro usuario no puede enviar, retirar_dinero lanza el error y la
        # transferencia se corta antes de sumar nada.
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)
        print(f"Transferencia de {cantidad} de {otro_usuario.nombre} a {self.nombre} completada.")


# Kata 36: Crea una función llamada procesar_texto
#   - Procesa un texto según la opción especificada: contar_palabras,
#     reemplazar_palabras o eliminar_palabra.
#   - Código a seguir:
#       - Crear una función contar_palabras que cuente el número de veces que
#         aparece cada palabra en el texto y devuelva un diccionario.
#       - Crear una función reemplazar_palabras para sustituir una
#         palabra_original por una palabra_nueva en el texto y devolver el texto
#         modificado.
#       - Crear una función eliminar_palabra que elimine una palabra del texto y
#         devuelva el texto sin ella.
#       - Crear la función procesar_texto que reciba un texto, una opción
#         ("contar", "reemplazar", "eliminar") y un número variable de argumentos
#         según la opción elegida.
#   - Caso de uso:
#       - Verificar el funcionamiento completo de procesar_texto.
def contar_palabras(texto):
    """Cuenta cuántas veces aparece cada palabra en el texto."""
    conteo = {}
    for palabra in texto.lower().split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Sustituye una palabra por otra en el texto."""
    # Trabajo palabra a palabra para no tocar trozos de otras ("sol" vs "soldado").
    resultado = []
    for palabra in texto.split():
        if palabra.lower() == palabra_original.lower():
            resultado.append(palabra_nueva)
        else:
            resultado.append(palabra)
    return " ".join(resultado)


def eliminar_palabra(texto, palabra):
    """Elimina todas las apariciones de una palabra en el texto."""
    resultado = [p for p in texto.split() if p.lower() != palabra.lower()]
    return " ".join(resultado)


def procesar_texto(texto, opcion, *args):
    """Procesa el texto según la opción: "contar", "reemplazar" o "eliminar"."""
    # args es una tupla con los argumentos extra que necesita cada opción.
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción '{opcion}' no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


# Kata 37: Genera un programa que nos indique si es de noche, de día o de tarde
# según la hora proporcionada por el usuario.
def momento_del_dia(hora):
    """Devuelve "día" (6-13), "tarde" (14-20) o "noche" (21-5)."""
    if hora < 0 or hora > 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if hora >= 6 and hora <= 13:
        return "día"
    elif hora >= 14 and hora <= 20:
        return "tarde"
    else:
        return "noche"


def momento_del_dia_usuario():
    """Pide una hora al usuario y dice si es de día, de tarde o de noche."""
    try:
        hora = int(input("Introduce la hora (0-23): "))
        momento = momento_del_dia(hora)
    except ValueError:
        print("Error: debes introducir un número entero entre 0 y 23.")
    else:
        print(f"A las {hora}:00 es de {momento}.")


# Kata 38: Escribe un programa que determine qué calificación en texto tiene un
# alumno según su calificación numérica.
#   - Reglas:
#       0 - 69: insuficiente
#       70 - 79: bien
#       80 - 89: muy bien
#       90 - 100: excelente
def calificacion_texto(nota):
    """Convierte una calificación numérica (0-100) en texto."""
    if nota < 0 or nota > 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


def calificacion_usuario():
    """Pide una calificación al usuario y muestra su equivalente en texto."""
    try:
        nota = float(input("Introduce la calificación del alumno (0-100): "))
        texto = calificacion_texto(nota)
    except ValueError:
        print("Error: debes introducir un número entre 0 y 100.")
    else:
        print(f"Una calificación de {nota} equivale a: {texto}")


# Kata 39: Escribe una función que tome dos parámetros: figura (una cadena que
# puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los
# datos necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    """Calcula el área de un rectángulo, un círculo o un triángulo."""
    figura = figura.lower()
    if figura == "rectangulo":
        base, altura = datos
        area = base * altura
    elif figura == "circulo":
        radio = datos[0]
        area = math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        area = base * altura / 2
    else:
        raise ValueError(f"Figura '{figura}' no válida.")
    return round(float(area), 2)


# Kata 40: Escribe un programa en Python que utilice condicionales para determinar
# el monto final de una compra en una tienda en línea, después de aplicar un
# descuento. El programa debe:
#   a. Solicitar al usuario el precio original de un artículo.
#   b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
#   c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
#   d. Aplicar el descuento al precio original, siempre que el valor del cupón
#      sea válido (mayor a cero).
#   e. Mostrar el precio final de la compra, considerando o no el descuento.
#   f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo
#      las acciones.
def calcular_precio_final(precio, cupon=0):
    """Aplica el cupón al precio si es válido (nunca devuelve negativo)."""
    if cupon <= 0:
        return precio
    elif cupon >= precio:
        return 0.0
    else:
        return round(precio - cupon, 2)


def compra_con_descuento_usuario():
    """Pide el precio y el cupón al usuario y muestra el precio final."""
    try:
        precio = float(input("Introduce el precio original del artículo (€): "))
        respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        if respuesta in ("si", "sí", "s"):
            cupon = float(input("Introduce el valor del cupón (€): "))
            if cupon > 0:
                precio_final = calcular_precio_final(precio, cupon)
                print(f"Cupón de {cupon:.2f} € aplicado.")
            else:
                precio_final = precio
                print("El cupón no es válido (debe ser mayor que cero). No se aplica descuento.")
        elif respuesta in ("no", "n"):
            precio_final = precio
            print("Sin cupón de descuento.")
        else:
            precio_final = precio
            print("Respuesta no reconocida. No se aplica descuento.")
        print(f"Precio final de la compra: {precio_final:.2f} €")
    except ValueError:
        print("Error: debes introducir un valor numérico.")


# =============================================================================
# EJEMPLOS DE USO
# =============================================================================

def main():
    """Ejecuta un ejemplo de cada kata."""
    print("Kata 1:", frecuencia_letras("Hola mundo"))
    print("Kata 2:", doblar_valores([1, 2, 3, 4, 5]))
    print("Kata 3:", buscar_palabras_que_contienen(["casa", "casado", "perro"], "cas"))
    print("Kata 4:", diferencia_listas([10, 20, 30], [1, 5, 10]))
    print("Kata 5:", evaluar_notas([4, 6.5, 7, 3, 8]))
    print("Kata 6:", factorial(5))
    print("Kata 7:", tuplas_a_strings([("Hola", "mundo"), (1, 2, 3)]))
    print("Kata 9:", filtrar_mascotas_permitidas(["Perro", "Tigre", "Gato", "Oso"]))
    print("Kata 10:", promedio_con_excepcion([4, 8, 15, 16, 23, 42]))
    try:
        promedio_con_excepcion([])
    except ListaVaciaError:
        print("Kata 10 (lista vacía): no se puede calcular el promedio de una lista vacía.")
    print("Kata 12:", longitud_palabras("Aprender Python es divertido"))
    print("Kata 13:", letras_mayus_minus("Python"))
    print("Kata 14:", palabras_que_empiezan_por(["Manzana", "pera", "melón"], "m"))
    print("Kata 15:", sumar_tres([1, 5, 10]))
    print("Kata 16:", palabras_mas_largas_que("El lenguaje Python es potente", 4))
    print("Kata 17:", digitos_a_numero([5, 7, 2]))
    print("Kata 18:", estudiantes_destacados(estudiantes))
    print("Kata 19:", filtrar_impares([1, 2, 3, 4, 5, 6]))
    print("Kata 20:", solo_enteros([1, "dos", 3, "cuatro", 5]))
    print("Kata 21:", calcular_cubo(3))
    print("Kata 22:", producto_total([2, 3, 4, 5]))
    print("Kata 23:", concatenar_palabras(["Python", "es", "genial"]))
    print("Kata 24:", diferencia_total([100, 20, 30, 10]))
    print("Kata 25:", contar_caracteres("Hola, Python!"))
    print("Kata 26:", calcular_resto(10, 3))
    print("Kata 27:", calcular_promedio([10, 20, 30, 40, 50]))
    print("Kata 28:", primer_duplicado([3, 5, 1, 5, 3, 2]))
    print("Kata 29:", enmascarar(1234567890123456))
    print("Kata 30:", son_anagramas("Roma", "amor"))

    # Kata 31: la versión interactiva está en ejecutar_interactivas()
    try:
        buscar_nombre(["Ana", "Luis", "Marta"], "Carlos")
    except NombreNoEncontradoError:
        print("Kata 31: el nombre 'Carlos' no está en la lista.")

    print("Kata 32:", buscar_puesto("Luis Martínez Ruiz", empleados))
    print("Kata 33:", sumar_listas([1, 2, 3], [10, 20, 30]))

    # Kata 34: caso de uso del árbol
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)
    print("Kata 34:", arbol.info_arbol())

    # Kata 35: caso de uso del banco (la transferencia falla porque Bob solo
    # tiene 70, y el error se maneja)
    print("Kata 35:")
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    try:
        alicia.transferir_dinero(bob, 80)
    except OperacionBancariaError:
        print("Error en la transferencia: Bob no tiene saldo suficiente para enviar 80.")
    alicia.retirar_dinero(50)

    # Kata 36: caso de uso de procesar_texto
    texto = "el sol sale y el sol se pone"
    print("Kata 36 contar:", procesar_texto(texto, "contar"))
    print("Kata 36 reemplazar:", procesar_texto(texto, "reemplazar", "sol", "astro"))
    print("Kata 36 eliminar:", procesar_texto(texto, "eliminar", "el"))
    try:
        procesar_texto(texto, "traducir")
    except ValueError:
        print("Kata 36 opción no válida: 'traducir' no es una opción permitida.")

    print("Kata 37:", momento_del_dia(16))
    print("Kata 38:", calificacion_texto(85))
    print("Kata 39:", calcular_area("circulo", (3,)))
    print("Kata 40:", calcular_precio_final(50, 10))


def ejecutar_interactivas():
    """Menú para probar las katas que piden datos al usuario."""
    while True:
        print()
        print("Katas interactivas: 8, 11, 31, 37, 38, 40 (Enter para salir)")
        opcion = input("Elige una kata: ").strip()
        if opcion == "":
            break
        elif opcion == "8":
            dividir_numeros_usuario()
        elif opcion == "11":
            pedir_edad_usuario()
        elif opcion == "31":
            try:
                buscar_nombre_usuario()
            except NombreNoEncontradoError:
                print("El nombre no está en la lista.")
        elif opcion == "37":
            momento_del_dia_usuario()
        elif opcion == "38":
            calificacion_usuario()
        elif opcion == "40":
            compra_con_descuento_usuario()
        else:
            print("Opción no válida.")


main()
ejecutar_interactivas()

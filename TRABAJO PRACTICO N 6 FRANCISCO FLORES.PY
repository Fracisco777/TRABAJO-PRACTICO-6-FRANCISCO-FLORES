#1. Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: Si el número es mayor a 3.50,
# devolver el entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior (3)."""

"""def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)
numero_decimal = float(input("Ingrese un número decimal: "))
resultado = redondear(numero_decimal)
print("El resultado del redondeo es:", resultado)"""

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un módulo que esté fuera de ese paquete, 
# cree una función de suma de decimales que redondee el resultado haciendo uso de la función redondear() del paquete recién creado.

"""from redondeo import redondear
def suma_decimales(numero1, numero2):
    suma = numero1 + numero2
    return redondear (suma)
numero1 = 2.75
numero2 = 1.5
resultado = suma_decimales(numero1,numero2)
print(resultado)"""

#3. Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema.

"""import datetime

fecha_hora_actual = datetime.datetime.now()
print("La fecha y hora actual es:", fecha_hora_actual)"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10 
#(pista: para comprobar si se pueden generar todos los números, pruebe ejecutar el programa dentro de un ciclo infinito)."""

"""import random
def numero_par_random():
    return random.randrange(2, 11, 2)
while True:
    numero = numero_par_random()
    print("Número par al azar entre 2 y 10:", numero)"""

# 5. Bola mágica: La bola mágica (Magic 8 ball)

"""import random

def responder(pregunta):
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)
pregunta = input("Hazme una pregunta: ")
respuesta = responder(pregunta)
print("Respuesta:", respuesta)"""

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)

"""import random
import time
def responder(pregunta):
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]
    return random.choice(respuestas)
inicio = time.time()
pregunta = input("Hazme una pregunta: ")
respuesta = responder(pregunta)
print("Respuesta:", respuesta)
tiempo_de_ejecucion = time.time() - inicio
print (tiempo_de_ejecucion)"""



import datetime

def calcular_nacimiento():
    
    fecha_nacimiento = input("Por favor, ingresa tu fecha de nacimiento (formato: DD/MM/AAAA): ")

    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento "%d/%m/%Y").date()

    fecha_actual = datetime.date.today()

    dias_transcurridos = (fecha_actual - fecha_nacimiento).days

    return dias_transcurridos
dias_desde_nacimiento = calcular_nacimiento()
print(dias_desde_nacimiento)


#Modules

"""
Que son los modulos en Python

Son archivos con extension .py o .pyc (Python compilado)
o archivos C que contiene funciones y clases que podemos importar en nuestros
archivos .py

"""

from modules import sum , value

sum(1,2)
value("hola")

import math
print(math.pi)
print(math.e)
print(math.sqrt(9))
print(math.factorial(5))
print(math.floor(3.4))

import random
print(random.randint(1, 10))
print(random.random())
print(random.choice([1, 2, 3, 4, 5]))

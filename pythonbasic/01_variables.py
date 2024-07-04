#que es una variable
# Una variable es un nombre que se refiere a un valor almacenado en el computador. 

"""
Esta función muestra un ejemplo de cómo trabajar con variables en Python.
"""
    
# Asignamos un valor a la variable mi_variable
mi_variable = 10
    
# Imprimimos el valor de la variable
print("El valor de mi_variable es:", mi_variable)
    
# Cambiamos el valor de la variable
mi_variable = 20
    
# Volvemos a imprimir el valor de la variable
print("El nuevo valor de mi_variable es:", mi_variable)

#Tipos de variables segun el tipo de dato
entero = 10
decimal = 3.14
cadena = "Hola Mundo"
booleano = True
nada = None
lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"a": 1, "b": 2}
conjunto = {1, 2, 3}

#Pasar variables separadas por coma con diferentes datos
print(entero, decimal, cadena, booleano, nada, lista, tupla, diccionario, conjunto)

#transformar un tipo de dato
cadena = str(entero)
print(type(cadena))

#algunas funciones de python
print(len(cadena))

#variables en una sola linea
variable1 = variable2 = variable3 = 10
print(variable1, variable2, variable3)

#input
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre)
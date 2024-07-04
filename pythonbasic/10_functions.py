"""
Que es una funcion en python ? 
Una funcion en python es una secuencia de instrucciones que se ejecutan cuando se llama a la funcion.

Definicion de funcion en python :
Una funcion en python es definida por la palabra clave def, seguida de un nombre para la funcion y entre parentesis
se colocan los parametros de entrada de la funcion. Luego se coloca una serie de instrucciones que se ejecutan cuando
se llama a la funcion. La funcion termina con la palabra clave return, que es opcional y que indica el valor de retorno
de la funcion.

Ejemplo de funcion en python :
"""

def my_function(param1, param2):
    # instrucciones de la funcion
    result = param1 + param2
    return result

my_result = my_function(2, 3)
print(my_result) # Output: 5

"""
Ejemplo de funcion en python con un parametro opcional :
"""
print(my_result) # Output: 5


def print_name(name, surname):
    print(f"Hello, {name} {surname}")

print_name(surname="John", name="Smith") # Output: Hello, John Smith

"""
Ejemplo de funcion en python con un parametro opcional y un valor por defecto para el parametro opcional :
"""

def print_name_alias_defaulth(name, surname, alias="IamMlovin"):
    print(f"Hello, {name} {surname} ({alias})")

print_name_alias_defaulth("David", "Mora") # Output: Hello, John Smith (IamMlovin)
print_name_alias_defaulth("John", "Smith", "JS") # Output: Hello, John Smith (JS)

"""
Ejemplo de funcion en python con un parametro que no es opcional :
"""

"""
Ejemplo de funcion en python con un parametro opcional y un valor por defecto para el parametro opcional y
un parametro que no es opcional :
"""

#Funciones por tipo de dato
def print_texts(*text):
    for text in text:
       print(text.upper())


print_texts("Hello", "World") # Output: ('Hello', 'World')
print_texts("Hello", "World", "Python") # Output: ('Hello', 'World', 'Python')




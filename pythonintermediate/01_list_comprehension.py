### List Comprehension ###
"""
List Comprehension en python es una técnica de iteración rápida y concisa para crear listas. 
Es una abreviatura para crear una lista a partir de una otra lista o iterable, aplicando una función a cada elemento de la lista original.

Sintaxis:
[expression for item in list]


"""

my_original_list = [1, 2, 3, 4, 5 , 6 , 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = [i for i in my_range ]
print(my_list)

my_list = [i + 1 for i in my_range ]
print(my_list)

my_list = [i * 2 for i in my_range ]
print(my_list)

my_list = [i * i for i in my_range ]
print(my_list)

# Ejemplo con condicional
my_list = [i for i in my_range if i % 2 == 0]
print(my_list)

my_range = range(8)
print(list(my_range))

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in my_range ]
print(my_list)

print(sum_five(5))
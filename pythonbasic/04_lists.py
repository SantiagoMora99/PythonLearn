#Listas
# Que es una lista en python ?
# Es una secuencia ordenada y mutable de elementos del mismo o diferente tipo.
# Su sintaxis es []

my_list = list() # Crear una lista vacía
my_list = [] # Crear una lista vacía
len(my_list) # Obtener la longitud de la lista
my_list.append(1) # Agregar un elemento al final de la lista
my_list.clear() # Eliminar todos los elementos de la lista
my_list.copy() # Crear una copia de la lista
my_list.count(1) # Contar la cantidad de veces que aparece un elemento en la lista
my_list.extend([2, 3]) # Agregar una secuencia de elementos a la lista
# my_list.index(1) # Devolver el índice de la primera aparición del elemento en la lista
# my_list.insert(0, 1) # Insertar un elemento en la lista en la posición especificada
my_list.pop() # Eliminar y devolver el último elemento de la lista
# my_list.remove(1) # Eliminar la primera aparición del elemento en la lista
my_list.reverse() # Revertir el orden de la lista
my_list.sort() # Ordenar la lista en orden ascendente
my_list.sort(reverse=True) # Ordenar la lista en orden descendente
# Sintaxis para crear una lista con elementos iniciales
my_list = [1, 2, 3, 4, 5]
# Acceder a elementos de la lista
my_list[0] # 1
my_list[-1] # 5
# Sintaxis para crear una lista con elementos de diferentes tipos
my_list = [1, "hola", True, 3.14]
# Iterar sobre una lista
for element in my_list:
    print(element)

print(len(my_list))
print(type(my_list))
print(my_list[0])
print(my_list.count(1))

#Desempaquetado de listas
a, b, c = [1, 2, 3] # a = 1, b = 2, c = 3
a, b = b, a # Intercambio de valores
print(a, b, c)

#Sumar listas
my_list_1 = ["Hola",1, 2, 3]
my_list_2 = [4, 5, 6]
my_list_3 = my_list_1 + my_list_2
print(my_list_3)

my_list_1.append("David")
print(my_list_1)

my_list_1.insert(1,"Mora")
print(my_list_1)

my_list_1.remove("Mora")
print(my_list_1)

print(my_list_1.pop())
print(my_list_1)

print(my_list_1.pop(0))
print(my_list_1)

my_pop_element = my_list_1.pop(2)
print(my_pop_element)
print(my_list_1)

del my_list_1[0]
print(my_list_1)

my_list_1.clear()
print(my_list_1)

my_list_2[0] = "Mundo"  
print(my_list_2)

my_new_list = my_list_2.copy()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

print(my_new_list[1:3])

# my_new_list.sort()
# print(my_new_list)




# my_list = "Hola Python"
# print (my_list)
# print(type(my_list))

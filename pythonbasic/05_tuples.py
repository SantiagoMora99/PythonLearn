# Que es una tupla ?
def explain_tuple():
    """Explica qué es una tupla en Python"""
    print("Una tupla es una secuencia ordenada y inmutable de elementos.")
    print("Es decir, una tupla es similar a una lista, pero no se puede modificar después de crearla.")
    print("Se define como (elemento1, elemento2, elemento3, ...)")

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (1, "Hello", 3.14, True)
my_other_tuple = (1, "Hello", 3.14, True)
print(type(my_tuple))  # <class 'tuple'>
print(my_tuple[0])   # 1
print(my_tuple[-1])  # True
print(my_tuple[-2])  # 3.14

print(my_tuple.count(1))
print(my_tuple.index("Hello"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)  # (1, 'Hello', 3.14, True, 1, 'Hello', 3.14, True)
print(my_sum_tuple[3:7])  # (True, 1, 'Hello', 3.14)

#Convertir tupla en lista
my_tuple = list(my_tuple)
print(type(my_tuple))  # <class 'list'>
my_tuple.insert(1, "World")
print(my_tuple)  # [1, 'World', 'Hello', 3.14, True]

del my_other_tuple
print(my_other_tuple)
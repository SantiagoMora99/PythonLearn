# Que es un set ?
# Un set es una colección desordenada de elementos únicos. Estos elementos pueden ser de cualquier tipo de datos, incluso objetos o estructuras de datos complejas.

# Cómo crear un set en Python ?
# Puedes crear un set utilizando la función set() o colocando elementos entre llaves {}.

# Ejemplo de set
my_set = set()
def esUnSet(cadena):
    """
    Indica si una cadena de caracteres contiene solo caracteres unicos.
    Un set no es una estructura de datos ordenada, por lo que no se mantiene el orden de los elementos.
    UN set no admite elementos duplicados.
    """
    return len(set(cadena)) == len(cadena)

my_set = set()
print(type(my_set))

my_other_set = {'casa', 'auto', 'foo'}
print(type(my_other_set))

print(len(my_other_set)) # 3
print(my_other_set) # Output: {'auto', 'casa', 'foo'}	
my_other_set.add('bar')
print(my_other_set) # Output: {'auto', 'bar', 'casa', 'foo'}

print('foo' in my_other_set) # True
print('baz' in my_other_set) # False

my_other_set.remove('bar')
print(my_other_set) # Output: {'auto', 'casa', 'foo'}

my_other_set.clear()
print(my_other_set) # Output: set()

"""
En Python, un set es una colección desordenada de elementos únicos. Estos elementos pueden ser de cualquier tipo de datos, incluso objetos o estructuras de datos complejas.

Los sets se utilizan cuando se requiere almacenar una colección de elementos únicos y desordenados, como cuando se requiere verificar la existencia de un elemento en el set o eliminar elementos duplicados de una colección.

Estos sets se implementan utilizando una tabla hash interna, lo que significa que los elementos se almacenan de forma eficiente utilizando una complejidad temporal de O(1) para la operación de inserción, búsqueda y eliminación.
"""

my_set = {1, 2, 3}
print(type(my_set)) # Output: <class 'set'>
my_list = list(my_set)
print(type(my_list)) # Output: <class 'list'>
print(my_list[1]) # Output: [1, 2, 3]

set1 = {1, 2, 3}

#Union set
set2 = {3, 4, 5}
print(set1 | set2) # Output: {1, 2, 3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}

#Diferencia set
print(set1 - set2) # Output: {1, 2}
print(set1.difference(set2)) # Output: {1, 2}
print(set2 - set1) # Output: {4, 5}
print(set2.difference(set1)) # Output: {4, 5}

"""
En matemáticas, un set se define como una colección de elementos sin elementos duplicados. Estos elementos pueden ser de cualquier tipo de datos, incluyendo números, cadenas de texto, objetos o estructuras de datos complejas.

Los sets se utilizan cuando se requiere almacenar una colección de elementos únicos y desordenados, como cuando se requiere verificar la existencia de un elemento en el set o eliminar elementos duplicados de una colección.

Los sets se implementan utilizando una tabla hash interna, lo que significa que los elementos se almacenan de forma eficiente utilizando una complejidad temporal de O(1) para la operación de inserción, búsqueda y eliminación.
"""

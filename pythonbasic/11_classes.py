"""
Que es una clase en python
Una clase es una abstracción de un conjunto de objetos que comparten un mismo comportamiento o características.
En Python, una clase es una definición de un objeto que incluye atributos y métodos.
Por ejemplo, una clase de unáleta eléctrica podría definir los atributos como la voltaje, la corriente y el estado
Los nombres de la clases en Mayusculas la primera y todo junto

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_person = Person("John", 30)
print(f"Hola mi nombre es {my_person.name} y mi edad es {my_person.age}")  # Output: John

class Person:
    def __init__(self, name, age):
        self.full_name = f"Hola mi nombre es {name} y tengo {age}"  # Concatena el nombre y la edad

    def walk(self):
        print(f"{self.full_name} está caminando.")

my_person = Person("John", 30)
print(my_person.full_name)  # Output: John
my_person.walk()  # Output: John está caminando.


class Person:
    def __init__(self, name, age , alias = "Mclovin") :
        self.full_name = f"Hola mi nombre es {name} y tengo {age} mi alias es {alias}"  # Concatena el nombre y la edad

    def walk(self):
        print(f"{self.full_name} está caminando.")

my_person = Person("John", 30)
print(my_person.full_name)  # Output: John
my_person.walk()  # Output: John está caminando.

my_other_person = Person("Jane", 25, "Little Johnny")
print(my_other_person.full_name)  # Output: Jane
my_other_person.walk()  # Output: Jane está caminando.
my_other_person.full_name = "Hola mi nombre es David y tengo 25 años mi alias es Little Johnny"
print(my_other_person.full_name)  # Output: Hola mi nombre es David y tengo 25 años mi alias es Little Johnny

# Clase con una propiedad privada

class Person:
    def __init__(self, name, age):
        self._name = name  # Propiedad privada
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# Que es un diccionario en python
'''
Un diccionario es una colección no ordenada de pares clave-valor. Los elementos se almacenan en una tabla hash, 
que permite acceso constante a los elementos por su clave.SI

'''
my_dict = {
    'name': 'David',
    'age': 30,
    'city': 'New York'
}
print(type(my_dict))  # <class 'dict'>

my_other_dict = {
    "name" : "Juan",
    "age" : 23,
    "city" : "New York",
    "lenguajes" : {"Python", "JS", "C"},
    "color":"red"
}

print(my_other_dict,my_dict)

print(len(my_other_dict))  # 4
print(my_other_dict["name"])  # Juan
print(my_other_dict["lenguajes"])  # {'Python', 'JS', 'C'}

my_other_dict["name"] = "Santiago"
print(my_other_dict)

my_other_dict["Calle"] = "Calle David"
print(my_other_dict)

del my_other_dict["Calle"]
print(my_other_dict)

print("Juan" in my_other_dict)  # False
print("name" in my_other_dict)  # True

print(my_other_dict.items())  # dict_items([('name', 'Santiago'), ('age', 23), ('city', 'New York'), ('lenguajes', {'Python', 'JS', 'C'}), ('color', 'red')])
print(my_other_dict.keys())  # dict_keys(['name', 'age', 'city', 'lenguajes', 'color'])
print(my_other_dict.values())  # dict_values(['Santiago', 23, 'New York', {'Python', 'JS', 'C'}, 'red'])
# print(my_other_dict.fromkeys(""))

my_new_dict = dict.fromkeys(my_other_dict)
print(my_new_dict)  # {'name': None, 'age': None, 'city': None, 'lenguajes': None, 'color': None}





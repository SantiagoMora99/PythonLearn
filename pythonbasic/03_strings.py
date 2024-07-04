#Strings
my_string = "Hello, World!"
my_other_string = 'Hello, World 1!'

print(len(my_string))
print(len(my_other_string)) 

#Salto de linea
print("Este es un texto \ncon salto de linea")

#tabulacion
print("\tEste es un texto con tabulacion")

#escapado
print("Este es un texto \\ escapado")

#Formateo
name , lastname , age = "David" , "Mora" , 20
print("Mi nombre es %s %s y tengo %d años" % (name , lastname , age))
print("Mi nombre es {} {} y tengo {} años".format(name, lastname, age))
print(f"Mi nombre es {name} {lastname} y tengo {age} años")
print(f"Mi nombre es {name.upper()} {lastname.upper()} y tengo {age} años")

#Desempaquetado de caracteres
language = "Pythont"
a, b, c, d, e, f ,g = language
print(a, b, c, d, e, f)
print(e)

#Division
language_slice = language[1:3]
print(language_slice)

#Reverse
reversed_language = language[::-1] 
print(reversed_language)

#Funciones
print(language.capitalize())
print(language.count("t"))
print(language.isalnum())
print(language.isalpha())
print("50".isdigit())
print("falso".islower())
print("Falso".isupper())
print(" ".isspace())


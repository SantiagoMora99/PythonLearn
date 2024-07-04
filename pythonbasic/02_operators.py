#Operadores
# + - / * %
# = += -= *= /= %= **=
# == != > < >= <=

print(5+5) #suma
print(5-3) #resta
print(5*3) #multiplicacion
print(5/3) #division
print(5%3) #modulo
print(5**3) #exponente
print(5//3) #division entera
print(5==3) #igualdad
print(5!=3) #desigualdad
print(5>3) #mayor que

# Operar tipos de datos
print("hola" + "mundo") #concatenacion
print("hola"*3) #repetir cadena

#Operar tipos de datos diferentes
print("hola" + str(5)) #convertir a cadena

my_float = 2.5 * 2
print("Resultado:" * int(my_float))

#Operadores Comparativos Numericos
print(3 > 2) # True
print(3 >= 2) # True
print(3 < 2) # False
print(3 <= 2) # False
print(3 == 2) # False
print(3 != 2) # True
print(3 is 2) # False
print(3 is not 2) # True
print(3 in [1, 2, 3]) # True
print(3 not in [1, 2, 3]) # False
print("hola" is "hola") # True
print("hola" is not "hola") # False
print("hola" in ["hola", "mundo"]) # True
print("hola" not in ["hola", "mundo"]) # False

#Operadores Comparativos Textos
print("hola" == "hola") # True
print("hola" != "hola") # False
print("hola" < "mundo") # True
print("hola" > "mundo") # False
print("hola" <= "hola") # True
print("hola" >= "hola") # True
print("hola" in ["hola", "mundo"]) # True
print("hola" not in ["hola", "mundo"]) # False
print("hola" is "hola") # True
print("hola" is not "hola") # False
print("hola" in ["hola", "mundo"]) # True
print("hola" not in ["hola", "mundo"]) # False

#Ordenacion Alfabetica
print("hola" < "mundo") # True
print("hola" > "mundo") # False

#Cuenta caracteres con operadores comparativos
print(len("hola") < len("mundo")) # True

#Operadores Logicos
# Que es el operador logico And ? 
# El operador logico And (&&) se utiliza para combinar dos expresiones booleanas. Se devuelve true solo si ambas expresiones son verdaderas.
# Que es el operador logico Or ?
# El operador logico Or (||) se utiliza para combinar dos expresiones booleanas. Se devuelve true si al menos una de las expresiones es verdadera.
# Que es el operador logico Not ?
# El operador logico Not (!) se aplica a una sola expresión booleana. Devuelve true si la expresión es falsa y viceversa.
print(3 > 2 and 3 > 2) # True
print(3 > 2 and 3 < 2) # False
print(3 > 2 or 3 < 2) # True
print(not(3 > 2)) # False
print(3 > 2 and not(3 < 2)) # True
print(3 > 2 or not(3 < 2)) # True
print(not(3 > 2 and 3 < 2)) # False
print(not(3 > 2 or 3 < 2)) # False
print(3 > 2 and 3 < 2 and 3 == 2) # False
print(3 > 2 or 3 < 2 or 3 == 2) # True
print(not(3 > 2 and 3 < 2 and 3 == 2)) # True
print(not(3 > 2 or 3 < 2 or 3 == 2)) # False

#Tabla de la verdad
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print(not(True)) # False
print(not(False)) # True
print(True and not(False)) # True
print(False and not(True)) # False
print(True or not(False)) # True
print(False or not(True)) # True



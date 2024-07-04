#Que son los condicionales en python
'''
En Python, los condicionales son una herramienta útil para controlar el flujo del programa según ciertas condiciones.
'''
if 5 > 3:
    print("5 es mayor que 3")
'''
Es importante tener en cuenta que la estructura if es la siguiente:
'''

my_conditional = True

if my_conditional:
    print("La condición es verdadera")

my_string = "Hola mundo"
if my_string == "Hola mundo":
    print("Las cadenas coinciden")

'''
En este ejemplo, se imprime un mensaje si la condición es verdadera (my_conditional es True), y si la cadena de texto coincide con "Hola mundo" (my_string).
'''
#Ejemplo
num1 = 10
num2 = 5
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
'''
En este ejemplo, se imprime un mensaje si num1 es mayor que num2.
'''

# Uso de Else
num1 = 5
num2 = 10

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
else:
    print(f"{num1} no es mayor que {num2}")

if num1 > num2 and num1 % 2 == 0:
    print(f"{num1} es mayor que {num2} y es par")
else:
    print(f"{num1} no es mayor que {num2} o no es par")


# If , Elif y Else
num1 = 15
num2 = 10
num3 = 5
if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")

elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor")

else:
    print(f"{num3} es el mayor")

'''
En este ejemplo, se imprime un mensaje diferente según el número mayor entre num1, num2 y num3. Si num1 es el mayor, se imprime un mensaje indicando que es el mayor. Si num2 es el mayor, se imprime un mensaje indicando que es el mayor. Si num3 es el mayor, se imprime un mensaje indicando que es el mayor.
'''

# If not
if not my_conditional:
    print("La condición es falsa")



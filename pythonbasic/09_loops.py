"""
Que son los bucles en python :

Un bucle es una estructura de control que permite repetir un bloque de código varias veces. En Python, existen dos tipos de bucles: los bucles "for" y los bucles "while".

Los bucles "for" se utilizan cuando se conoce el número de repeticiones exactas requeridas. Por ejemplo, si necesitamos imprimir los números del 1 al 10, podemos usar un bucle "for" como muestra el siguiente código:
"""

# Bucle for para imprimir números del 1 al 10
for i in range(1, 11):
    print(i)

"""
Los bucles "while" se utilizan cuando no se conoce el número de repeticiones requeridas. Por ejemplo, si necesitamos imprimir los números pares del 2 al 10, podemos usar un bucle "while" como muestra el siguiente código:
"""
# Bucle while para imprimir números pares del 2 al 10
num = 2
while num <= 10:
    print(num)
    num += 2
else:
    print("Se completó el bucle while.")

"""
En summa, Python ofrece dos tipos de bucles, los bucles "for" y los bucles "while", con la diferencia que los bucles "for" se utilizan cuando se conoce el número de repeticiones exactas requeridas, mientras que los bucles "while" se utilizan cuando no se conoce el número de repeticiones requeridas.
"""

'''

This code demonstrates the use of different types of loops in Python:

1. `for` loop: This loop is used when the number of iterations is known in advance. In the example, we use a `for` loop to iterate over the range of numbers from 1 to 10 and print each number.

2. `while` loop: This loop is used when the number of iterations is not known in advance. In the example, we use a `while` loop to iterate over the even numbers from 2 to 10 and print each number. The `else` statement is used to print a message when the loop completes, indicating that the loop has exited normally.

In both cases, the loop variable (`i` and `num`) is used to control the loop execution. The `break` and `continue` statements can be used within the loop to alter its behavior.

It's important to note that while loops can be used to achieve the same result as `for` loops in certain cases, but `for` loops are more concise and easier to read and maintain. Additionally, you can use other loop constructs (e.g., `enumerate()`) to achieve the same result with different syntax.
'''
my_condition = 0
while my_condition < 20:
    # Code to execute while the condition is true
    print(my_condition)
    my_condition += 1
    if my_condition == 10:
        # To break the loop
        print(my_condition)
        print("Break")
        break

print("La ejecución continúa después del bucle while")

# For
my_list = [1, 2, 3, 4, 5 , "Hola"]
for element in my_list:
    print(element)

my_other_dict = {
    "name" : "Juan",
    "age" : 23,
    "city" : "New York",
    "lenguajes" : {"Python", "JS", "C"},
    "color":"red"
}

for element in my_other_dict: 
    if element == "city":
        break
    print(element)

for element in my_other_dict.values():
    if element == 23:
        continue
    print(element)
else:
    print("El bucle for ha terminado de ejecutarse correctamente.")


"""
Break : El break en los bucles es : Rompe el bucle y no continua ejecutando el código restante.
Continue : El continue en los bucles es : Salta a la siguiente iteración del bucle.
Else : El else en los bucles es : Se ejecuta después del bucle se ha ejecutado correctamente, sin que haya habido un break.
"""

"""
En resumen, los bucles en Python se utilizan para repetir una acción varias veces, either con un número conocido de repeticiones o sin un número conocido de repeticiones. Los bucles "for" se utilizan cuando se conoce el número de repeticiones exactas requeridas, mientras que los bucles "while" se utilizan cuando no se conoce el número de repeticiones requeridas. Los bucles "for" y "while" se diferencian en la sintaxis y en la capacidad de control de flujo, pero ambos se utilizan en casi todas las situaciones en que se requiera repetir una acción varias veces.
"""

"""
This code demonstrates the use of different types of loops in Python:

1. `for` loop: This loop is used when the number of iterations is known in advance. In the example, we use a `for` loop to iterate over the range of numbers from 1 to 10 and print each number.

2. `while` loop: This loop is used when the number of iterations is not known in advance. In the example, we use a `while` loop to iterate over the even numbers from 2 to 10 and print each   
"""

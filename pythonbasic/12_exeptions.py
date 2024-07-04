#Exepciones Handling
"""
Que es el manejo de errores en python :
La manejo de errores en python se realiza a traves de bloques try-except-finally
try: seccion de codigo que se intenta ejecutar
except: seccion de codigo que se ejecuta en caso de que se produzca una excepcion
finally: seccion de codigo que se ejecuta siempre al final, independientemente de si se produjo una excepcion o no
else: seccion de codigo que se ejecuta en caso de que no se produzca una excepcion
"""
def divide_numbers(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except (ValueError, TypeError):
        print("Error: Invalid input")
    else:
        print(f"Result: {result}")
    finally:
        print("Exiting function")

divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "a")


a = 1
b = 2
c = "Hola"

try:
    print(a + b + c)
    print("No se ha producido un error")
except TypeError:
    print("Error: Tipo de datos incorrecto")

"""
Tipós de Errores Except:
IndexError: Error de indice
NameError: Error de nombre
SyntaxError: Error de sintaxis
TypeError: Error de tipo
ValueError: Error de valor
"""

#Captura de la informacion del error

x = 10
y = "Hola"


try:
    result = x / y
    print(f"Result: {result}")
    print("No se ha producido un error")
except ZeroDivisionError as e:
    print(f"Error: Cannot divide by zero. {e}")

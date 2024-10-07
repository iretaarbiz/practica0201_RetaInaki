#Escribir un programa que lea un entero positivo, , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta . 
#La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma = n (n + 1)2

x = int(input("Introduce un entero positivo "))
resultado = x*(x+1)/2
print("La suma de todos los enteros desde el 1 es:", resultado)
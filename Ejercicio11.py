'''Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.'''

deposito = int(input("Cuanto dinero depositas: \n"))
año1 = deposito * 1.04
año2 = año1 * 1.04
año3 = año2 * 1.04
print("El primer año tendrás", round(año1, 2))
print("El segundo año tendrás", round(año2, 2))
print("El segundo año tendrás", round(año3, 2))
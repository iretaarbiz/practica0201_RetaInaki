#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión.

inv = int(input("Dinero que vas a invertir: \n"))
interes = int(input("Cual es el interes anual: \n"))
años = int(input("Años que vas a dejar: \n"))
beneficio = inv
while años > 0:
    beneficio = beneficio * interes
print("El capital es de: ", beneficio)
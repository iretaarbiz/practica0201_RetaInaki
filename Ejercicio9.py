#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión.

inv = int(input("Dinero que vas a invertir: \n"))
interes = float(input("Cual es el interes anual: \n"))
años = int(input("Años que vas a dejar: \n"))
beneficio = inv
avanzar = años
while avanzar > 0:
    beneficio = beneficio * (interes + 1)
    avanzar = avanzar - 1
print("El capital obtenido en la inversión es de: ", beneficio - inv)
'''Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por 
no ser fresca y la ganancia final total.'''

barras_dia = int(input("¿Cuantas barras de pan que son del día se han vendido?\n"))
barras_no_dia = int(input("¿Cuantas barras de pan que no son del día se han vendido?\n"))
print("La barra de pan habitualmente vale 3.49€, si no es del día tiene un descuento del 60%")
ganancia = barras_dia * 3.49 + barras_no_dia * round((3.49 * 0.6), 2)
print("La ganancia total es de: ", ganancia, "€")
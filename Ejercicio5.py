#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas = int(input("Cuantas horas has trabajado?\n"))
cobrahora = int(input("Cuanto cobras la hora?\n"))
print("Te corresponden ", cobrahora*horas,"€",sep="")

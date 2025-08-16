from Clase.Animal import *

P = animal (" Garfield ","2,5 Kg","Camilo","08/08/2020","02/01/2021")

#Usando los métodos GET
print("Nombre: ", P.Nombre)
print("Peso: ", P.Peso)
print("Propietario: ", P.Propietario)
print("Fecha de Cumpleaños: ", P.fecha_cumpleaños)
print("Fecha de Última Vacuna: ", P.fecha_ultima_vacuna)

#Usando los métodos SET
P.Nombre = "Garfield"
P.Peso = "4 Kg"
P.Propietario = "Camilo"
P.fecha_cumpleaños = "08/08/2020"
P.fecha_ultima_vacuna = "05/07/2021"
#Usando los métodos GET nuevamente para verificar los cambios
print("\nDespués de los cambios:")
print("Nombre: ", P.Nombre)
print("Peso: ", P.Peso)
print("Propietario: ", P.Propietario)
print("Fecha de Cumpleaños: ", P.fecha_cumpleaños)
print("Fecha de Última Vacuna: ", P.fecha_ultima_vacuna)

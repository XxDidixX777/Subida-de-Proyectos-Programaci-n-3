#Forma de importar 1
#impor Clases.Persona
#Forma de importar 2
from Clases.Persona import *

p = Persona("Didier","Lopez")

#Asignar valor usando el metodo SET
p.nombre = "Tilin"

#Llamado
print(p._nombre)

print(p._apellido)
class Persona:
    #Constrcutor de la clase
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    #Metodo GET
    @property
    def nombre(self):
        return self._nombre
    
    #Metodo SET
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    #Metodo GET
    @property
    def apellido(self):
        return self._apellido
    
    #Metodo SET
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido
        
class animal:
    def __init__(self,Nombre, Peso, Propietario, fecha_cumpleaños, fecha_ultima_vacuna):
        self._Nombre = Nombre
        self._Peso = Peso
        self._Propietario = Propietario
        self._fecha_cumpleaños = fecha_cumpleaños
        self._fecha_ultima_vacuna = fecha_ultima_vacuna

    #Metodo GET
    @property
    def Nombre(self):
        return self._Nombre
    #Metodo SET
    @Nombre.setter
    def Nombre(self,nuevo_Nombre):
        self._Nombre = nuevo_Nombre
    
    #Metodo GET
    @property
    def Peso(self):
        return self._Peso
    #Metodo SET
    @Peso.setter
    def Peso(self,nuevo_Peso):
        self._Peso = nuevo_Peso
    
    #Metodo GET
    @property
    def Propietario(self):
        return self._Propietario
    #Metodo SET
    @Propietario.setter
    def Propietario(self,nuevo_Propietario):
        self._Propietario = nuevo_Propietario
    
    #Metodo GET
    @property
    def fecha_cumpleaños(self):
        return self._fecha_cumpleaños
    #Metodo SET
    @fecha_cumpleaños.setter
    def fecha_cumpleaños(self,nuevo_fecha_cumpleaños):
        self._fecha_cumpleaños = nuevo_fecha_cumpleaños
    
    #Metodo GET
    @property
    def fecha_ultima_vacuna(self):
        return self._fecha_ultima_vacuna
    #Metodo SET
    @fecha_ultima_vacuna.setter
    def fecha_ultima_vacuna(self,nuevo_fecha_ultima_vacuna):
        self._fecha_ultima_vacuna = nuevo_fecha_ultima_vacuna
    
    


        

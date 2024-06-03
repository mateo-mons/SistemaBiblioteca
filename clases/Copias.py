class Copia:

    def __init__(self, identificador, estado, isbn):
        self.identificador = identificador
        self.estado = estado
        self.isbn = isbn

    # Representación de la clase Copias en forma de cadena

    def __str__(self):
        return f"Identificador: {self.identificador}, Estado: {self.estado}, ISBN: {self.isbn}"
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getIdentificador(self):
        return self.identificador
    
    def getEstado(self):
        return self.estado
    
    def getIsbn(self):
        return self.isbn
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setIdentificador(self, identificador):
        self.identificador = identificador
    
    def setEstado(self, estado):
        self.estado = estado
    
    def setIsbn(self, isbn):
        self.isbn = isbn

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------
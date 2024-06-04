class Copia:

    def __init__(self, identificador, estado, isbn):
        self.identificador = identificador
        self.estado = estado
        self.isbn = isbn

    # Representación de la clase Copias en forma de cadena

    def verCopia(self):
        print(f"Identificador: {self.identificador}\nEstado: {self.estado}\nISBN: {self.isbn}")
    
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
class Copia:
    contador = 0

    def __init__(self, nombre_libro, estado, isbn):
        Copia.contador += 1
        self.identificador = Copia.contador
        self.nombre_libro = nombre_libro
        self.estado = estado
        self.isbn = isbn

    # Representación de la clase Copias en forma de cadena

    def verCopia(self):
        print("-- Detalles --")
        print(f"Copia ID: {self.identificador}\nNombre: {self.nombre_libro}\n Estado: {self.estado}\nISBN: {self.isbn}")
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getIdentificador(self):
        return self.identificador
    
    def getNombreLibro(self):
        return self.nombre_libro
    
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

    
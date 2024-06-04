class Categoria:

    def __init__(self, nombre, id, descripcion, subcategoria=None):
        self.nombre = nombre
        self.id = id
        self.descripcion = descripcion
        self.subcategoria = subcategoria

    # Representación de la clase Categoria en forma de cadena

    def verCategoria(self):
        print(f"Categoria: {self.nombre}\nId: {self.id}\nDescripcion: {self.descripcion}\nSubcategoria: {self.subcategoria}")
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getNombre(self):
        return self.nombre
    
    def getId(self):
        return self.id
    
    def getDescripcion(self):
        return self.descripcion
    
    def getSubcategoria(self):
        return self.subcategoria
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setId(self, id):
        self.id = id
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setSubcategoria(self, subcategoria):
        self.subcategoria = subcategoria

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------
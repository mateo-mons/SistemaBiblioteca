class Categoria:

    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    # Representación de la clase Categoria en forma de cadena

    def verCategoria(self):
        print("-- Detalles --")
        print(f"Id: {self.id}\nCategoria: {self.nombre}\nDescripcion: {self.descripcion}")
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getId(self):
        return self.id
    
    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getSubcategoria(self):
        return self.subcategoria
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setSubcategoria(self, subcategoria):
        self.subcategoria = subcategoria

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def modificarDatos(self, id=None, nombre=None, descripcion=None):
        if id:
            self.setId(id)
        if nombre:
            self.setNombre(nombre)
        if descripcion:
            self.setDescripcion(descripcion)
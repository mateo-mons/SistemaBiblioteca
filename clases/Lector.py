class Lector:

    def __init__(self, nombre, id, telefono, direccion, estado):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
        self.libros_prestados = []
        self.multas = []

    # Representación de la clase Libro en forma de cadena

    def verLector(self):
        print("-- Detalles --")
        print(f"Nombre: {self.nombre}\nID: {self.id}\nTeléfono: {self.telefono}\nDirección: {self.direccion}\nEstado: {self.estado}\nLibros prestados: {len(self.libros_prestados)}\nMultas: {len(self.multas)}")

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getNombre(self):
        return self.nombre
    
    def getId(self):
        return self.id
    
    def getTelefono(self):
        return self.telefono
    
    def getDireccion(self):
        return self.direccion
    
    def getEstado(self):
        return self.estado
    
    def getLibrosPrestados(self):
        return self.libros_prestados
    
    def getMultas(self):
        return self.multas

    # -------------------------------------------------------------- Setters --------------------------------------------------------------

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setId(self, id):
        self.id = id
    
    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setEstado(self, estado):
        self.estado = estado
    
    def setLibrosPrestados(self, libros_prestados):
        self.libros_prestados = libros_prestados
    
    def setMultas(self, multas):
        self.multas = multas

    # -------------------------------------------------------------- Operaciones --------------------------------------------------------------
    
    def agregarLibroPrestado(self, libro):
        if len(self.libros_prestados) < 3:
            self.libros_prestados.append(libro)
    
    def agregarMulta(self, multa):
        self.multas.append(multa)

    def eliminarLibroPrestado(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def levantarMulta(self, multa):
        if multa in self.multas:
            multa.levantarMulta()
            self.multas.remove(multa)

    def modificarDatos(self, nombre, id, telefono, direccion, estado):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.estado = estado
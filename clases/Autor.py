class Autor:

    def __init__(self, nombre, nacionalidad, fecha_nac):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nac = fecha_nac
        self.libros = []

    # Representación de la clase Autor en forma de cadena
    def verAutor(self):
        return f"Nombre del autor: {self.nombre}\nNacionalidad: {self.nacionalidad}\nFecha de nacimiento: {self.fecha_nac}\nCantidad de libros: {len(self.libros)}"

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getNombre(self):
        return self.nombre

    def getNacionalidad(self):
        return self.nacionalidad

    def getFechaNac(self):
        return self.fecha_nac

    def getCantidadLibros(self):
        return len(self.libros)

    def getLibros(self):
        return self.libros

    # -------------------------------------------------------------- Setters --------------------------------------------------------------

    def setNombre(self, nombre):
        self.nombre = nombre

    def setNacionalidad(self, nacionalidad):
        self.nacionalidad = nacionalidad

    def setFechaNac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def setLibros(self, libros):
        self.libros = libros

    # -------------------------------------------------------------- Operaciones --------------------------------------------------------------

    def agregarLibro(self, libro):
        if libro not in self.libros:
            self.libros.append(libro)

    def actualizarDatos(self, nombre=None, nacionalidad=None, fecha_nac=None):
        if nombre:
            self.setNombre(nombre)
        if nacionalidad:
            self.setNacionalidad(nacionalidad)
        if fecha_nac:
            self.setFechaNac(fecha_nac)
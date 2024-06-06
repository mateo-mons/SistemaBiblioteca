from clases.Libro import *

class Autor:

    def __init__(self, id_autor, nombre, nacionalidad, fecha_nac):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nac = fecha_nac
        self.libros = []

    # Representación de la clase Autor en forma de cadena
    def verAutor(self):
        print(f"Nombre del autor: {self.nombre}\nNacionalidad: {self.nacionalidad}\nFecha de nacimiento: {self.fecha_nac}\nCantidad de libros: {len(self.libros)}")

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getIdAutor(self):
        return self.id_autor
    
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

    def setIdAutor(self, id_autor):
        self.id_autor = id_autor

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

    def modificarDatos(self, id_autor=None, nombre=None, nacionalidad=None, fecha_nac=None):
        if id_autor:
            self.setIdAutor(id_autor)
        if nombre:
            self.setNombre(nombre)
        if nacionalidad:
            self.setNacionalidad(nacionalidad)
        if fecha_nac:
            self.setFechaNac(fecha_nac)
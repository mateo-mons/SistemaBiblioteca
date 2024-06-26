from clases.Producto import *
from clases.Copias import *
from clases.Categoria import *

class Libro(Producto):

    def __init__(self, titulo, isbn, edicion, ano_publicacion, editorial, estado, idioma, copias, categoria, autores=None):
        self.titulo = titulo
        self.isbn = isbn
        self.edicion = edicion
        self.ano_publicacion = ano_publicacion
        self.editorial = editorial
        self.estado = estado
        self.idioma = idioma
        self.copias = []
        self.categoria = categoria
        self.autores = autores if autores is not None else []

    # Representación de la clase Libro en forma de cadena

    def verLibro(self):
        print("-- Detalles --")
        autores_str = ', '.join([autor.getNombre() for autor in self.autores])
        print(f"Titulo del libro: {self.titulo}\nISBN: {self.isbn}\nEdición: {self.edicion}\nAño: {self.ano_publicacion}\nEditorial: {self.editorial}\nEstado: {self.estado}\nIdioma: {self.idioma}\nNumero de copias: {self.copias}\nCategoria: {self.categoria}\nAutores: {autores_str}")

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getTitulo(self):
        return self.titulo

    def getIsbn(self):
        return self.isbn

    def getEdicion(self):
        return self.edicion

    def getAnoPublicacion(self):
        return self.ano_publicacion

    def getEditorial(self):
        return self.editorial

    def getEstado(self):
        return self.estado

    def getIdioma(self):
        return self.idioma

    def getNumCopias(self):
        return self.copias
    
    def getCategoria(self):
        return self.categoria

    def getAutores(self):
        return self.autores

    # -------------------------------------------------------------- Setters --------------------------------------------------------------

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setEdicion(self, edicion):
        self.edicion = edicion

    def setAnoPublicacion(self, ano_publicacion):
        self.ano_publicacion = ano_publicacion

    def setEditorial(self, editorial):
        self.editorial = editorial

    def setEstado(self, estado):
        self.estado = estado

    def setIdioma(self, idioma):
        self.idioma = idioma

    def setNumCopias(self, copias):
        self.copias = copias

    def setCategoria(self, categoria):
        self.categoria = categoria

    def setAutores(self, autores):
        self.autores = autores

    # -------------------------------------------------------------- Operaciones --------------------------------------------------------------
    
    def agregarAutor(self, autor):
        if autor not in self.autores:
            self.autores.append(autor)
            autor.agregarLibro(self)

    def agregar_copia(self, copia):
        self.copias.append(copia)

    def buscar_copias_disponibles(self):
        copias_disponibles = [copia for copia in self.copias if copia.estado == "En biblioteca"]
        return copias_disponibles

    def modificarDatos(self, titulo=None, isbn=None, edicion=None, ano_publicacion=None, editorial=None, estado=None, idioma=None, copias=None, categoria=None, autores=None):
        if titulo:
            self.setTitulo(titulo)
        if isbn:
            self.setIsbn(isbn)
        if edicion:
            self.setEdicion(edicion)
        if ano_publicacion:
            self.setAnoPublicacion(ano_publicacion)
        if editorial:
            self.setEditorial(editorial)
        if estado:
            self.setEstado(estado)
        if idioma:
            self.setIdioma(idioma)
        if copias:
            self.setNumCopias(copias)
        if categoria:
            self.setCategoria(categoria)
        if autores:
            self.setAutores(autores)
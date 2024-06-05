from clases.AbstractFactory import *
from clases.Tesis import *
from clases.ArticuloCientifico import *
from clases.Libro import *
from clases.Copias import *

class Factory(AbstractFactory):

    def crear_tesis(self, id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas):
        return Tesis(id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas)

    def crear_articulo(self, titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado):
        return ArticuloCientifico(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado)

    def crear_libro(self, titulo, isbn, edicion, ano_publicacion, editorial, estado, idioma, num_copias, categoria, autores):
        libro = Libro(titulo, isbn, edicion, ano_publicacion, editorial, estado, idioma, num_copias, categoria, autores)
        for i in range(1, num_copias + 1):
            copia = Copia(titulo, "En biblioteca", isbn)
            libro.agregar_copia(copia)
        return libro

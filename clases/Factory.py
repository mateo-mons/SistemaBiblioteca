from clases.AbstractFactory import *
from clases.Tesis import *
from clases.ArticuloCientifico import *
from clases.Libro import *

class Factory(AbstractFactory):

    def crear_tesis(self, id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas):
        return Tesis(id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas)

    def crear_articulo(self, titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado):
        return ArticuloCientifico(titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado)

    def crear_libro(self, titulo, isbn, genero, edicion, ano_publicacion, editorial, estado, idioma, num_copias, autores):
        return Libro(titulo, isbn, genero, edicion, ano_publicacion, editorial, estado, idioma, num_copias, autores)

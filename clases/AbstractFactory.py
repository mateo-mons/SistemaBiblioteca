from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def crear_tesis(self, id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, num_paginas):
        pass

    @abstractmethod
    def crear_articulo(self, titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo, estado, autor):
        pass

    @abstractmethod
    def crear_libro(self, titulo, isbn, edicion, ano_publicacion, editorial, estado, idioma, num_copias, categoria, autores):
        pass

from clases.Producto import *

class ArticuloCientifico(Producto):

    def __init__(self, titulo, doi, editor, fecha_publicacion, periodicidad, volumen, campo_interes, estado):
        self.titulo = titulo
        self.doi = doi
        self.editor = editor
        self.fecha_publicacion = fecha_publicacion
        self.periodicidad = periodicidad
        self.volumen = volumen
        self.campo_interes = campo_interes
        self.estado = estado

    # Representación de la clase Libro en forma de cadena

    def verArticuloCientifico(self):
        print(f"Titulo: {self.titulo}\nDOI: {self.doi}\nEditor: {self.editor}\nFecha de publicación: {self.fecha_publicacion}\nPeriodicidad: {self.periodicidad}\nVolumen: {self.volumen}\nCampo de interés: {self.campo_interes}\nEstado: {self.estado}")

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getTitulo(self):
        return self.titulo
    
    def getDoi(self):
        return self.doi
    
    def getEditor(self):
        return self.editor
    
    def getFechaPublicacion(self):
        return self.fecha_publicacion
    
    def getPeriodicidad(self):
        return self.periodicidad
    
    def getVolumen(self):
        return self.volumen
    
    def getCampoInteres(self):
        return self.campo_interes
    
    def getEstado(self):
        return self.estado

    # -------------------------------------------------------------- Setters --------------------------------------------------------------

    def setTitulo(self, titulo):
        self.titulo = titulo
    
    def setDoi(self, doi):
        self.doi = doi
    
    def setEditor(self, editor):
        self.editor = editor
    
    def setFechaPublicacion(self, fecha_publicacion):
        self.fecha_publicacion = fecha_publicacion
    
    def setPeriodicidad(self, periodicidad):
        self.periodicidad = periodicidad
    
    def setVolumen(self, volumen):
        self.volumen = volumen
    
    def setCampoInteres(self, campo_interes):
        self.campo_interes = campo_interes
    
    def setEstado(self, estado):
        self.estado = estado

    # -------------------------------------------------------------- Operaciones --------------------------------------------------------------

    def modificarDatos(self, titulo=None, doi=None, editor=None, fecha_publicacion=None, periodicidad=None, volumen=None, campo_interes=None, estado=None):
        if titulo:
            self.setTitulo(titulo)
        if doi:
            self.setDoi(doi)
        if editor:
            self.setEditor(editor)
        if fecha_publicacion:
            self.setFechaPublicacion(fecha_publicacion)
        if periodicidad:
            self.setPeriodicidad(periodicidad)
        if volumen:
            self.setVolumen(volumen)
        if campo_interes:
            self.setCampoInteres(campo_interes)
        if estado:
            self.setEstado(estado)
        
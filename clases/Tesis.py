from clases.Autor import *

class Tesis:

    def __init__(self, id_tesis, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas):
        self.id_tesis = id_tesis
        self.autor = autor
        self.institucion = institucion
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo = campo
        self.estado = estado
        self.paginas = paginas

    # Representación de la clase Tesis en forma de cadena

    def verTesis(self):
        print(f"Autor: {self.autor.getNombre()}\nInstitucion: {self.institucion}\nFecha de investigacion: {self.fecha_investigacion}\nFecha de presentacion: {self.fecha_presentacion}\nCampo: {self.campo}\nEstado: {self.estado}\nNumero paginas: {self.paginas}")
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getAutor(self):
        return self.autor
    
    def getInstitucion(self):
        return self.autor
    
    def getFechaInvestigacion(self):
        return self.fecha_investigacion
    
    def getFechaPresentacion(self):
        return self.fecha_presentacion
    
    def getCampo(self):
        return self.campo
    
    def getEstado(self):
        return self.estado
    
    def getPaginas(self):
        return self.paginas
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setAutor(self, autor):
        self.autor = autor
    
    def setInstitucion(self, institucion):
        self.institucion = institucion
    
    def setFechaInvestigacion(self, fecha_investigacion):
        self.fecha_investigacion = fecha_investigacion
    
    def setFechaPresentacion(self, fecha_presentacion):
        self.fecha_presentacion = fecha_presentacion
    
    def setCampo(self, campo):
        self.campo = campo
    
    def setEstado(self, estado):
        self.estado = estado
    
    def setPaginas(self, paginas):
        self.paginas = paginas

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def modificarDatos(self, autor=None, institucion=None, fecha_investigacion=None, fecha_presentacion=None, campo=None, estado=None, paginas=None):
        if autor:
            self.autor(autor)
        if institucion:
            self.setInstitucion(institucion)
        if fecha_investigacion:
            self.setFechaInvestigacion(fecha_investigacion)
        if fecha_presentacion:
            self.setFechaPresentacion(fecha_presentacion)
        if campo:
            self.setCampo(campo)
        if estado:
            self.setEstado(estado)
        if paginas:
            self.setPaginas(paginas)
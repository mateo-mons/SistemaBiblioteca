class Tesis:

    def __init__(self, autor, institucion, fecha_investigacion, fecha_presentacion, campo, estado, paginas):
        self.autor = autor
        self.institucion = institucion
        self.fecha_investigacion = fecha_investigacion
        self.fecha_presentacion = fecha_presentacion
        self.campo = campo
        self.estado = estado
        self.paginas = paginas

    # Representación de la clase Tesis en forma de cadena

    def __str__(self):
        return f"Autor: {self.autor}, Institucion: {self.institucion}, Fecha Investigacion: {self.fecha_investigacion}, Fecha Presentacion: {self.fecha_presentacion}, Campo: {self.campo}, Estado: {self.estado}, Numero paginas: {self.paginas}"
    
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
class ArticuloCientifico:

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

    def __str__(self):
        return f"Titulo: {self.titulo}, DOI: {self.doi}, Editor: {self.editor}, Fecha de publicación: {self.fecha_publicacion}, Periodicidad: {self.periodicidad}, Volumen: {self.volumen}, Campo de interés: {self.campo_interes}, Estado: {self.estado}"

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
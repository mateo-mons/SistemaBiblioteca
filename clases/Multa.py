class Multa:

    def __init__(self, id_multa, id_prestamo, dias_retraso, fecha_entrega, fecha_finalizacion, estado):
        self.id_multa = id_multa
        self.id_prestamo = id_prestamo
        self.dias_retraso = dias_retraso
        self.fecha_entrega = fecha_entrega
        self.fecha_finalizacion = fecha_finalizacion
        self.estado = estado
        self.costo_por_dia = 3000

    # Representación de la clase Libro en forma de cadena

    def verMulta(self):
        print("-- Detalles --")
        print(f"ID multa: {self.id_multa}\nID prestamo: {self.id_prestamo}\nDias de retraso: {self.dias_retraso}\nFecha de entrega: {self.fecha_entrega}\nFecha de finalizacion: {self.fecha_finalizacion}\nEstado: {self.estado}")

    # --------------------------------------------------------------- Getters --------------------------------------------------------------

    def getIdMulta(self):
        return self.id_multa
    
    def getIdPrestamo(self):
        return self.id_prestamo
    
    def getDiasRetraso(self):
        return self.dias_retraso
    
    def getFechaEntrega(self):
        return self.fecha_entrega
    
    def getFechaFinalizacion(self):
        return self.fecha_finalizacion
    
    def getEstado(self):
        return self.estado

    # -------------------------------------------------------------- Setters --------------------------------------------------------------

    def setIdMulta(self, id_multa):
        self.id_multa = id_multa
    
    def setIdPrestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo
    
    def setDiasRetraso(self, dias_retraso):
        self.dias_retraso = dias_retraso
    
    def setFechaEntrega(self, fecha_entrega):
        self.fecha_entrega = fecha_entrega
    
    def setFechaFinalizacion(self, fecha_finalizacion):
        self.fecha_finalizacion = fecha_finalizacion
    
    def setEstado(self, estado):
        self.estado = estado

    # -------------------------------------------------------------- Operaciones --------------------------------------------------------------
    
    def calcularDiasRetraso(self):
        dias_retraso = (self.fecha_finalizacion - self.fecha_entrega).days
        if dias_retraso > 0:
            self.dias_retraso = dias_retraso - 1  # Se cuenta desde el segundo día de retraso
        else:
            self.dias_retraso = 0

    def generarMulta(self):
        self.estado = "activa"
        self.calcularDiasRetraso()
    
    def levantarMulta(self):
        self.estado = "inactiva"
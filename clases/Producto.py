from abc import ABC, abstractmethod

class Producto(ABC):
    
    @abstractmethod
    def verProducto(self):
        pass
from abc import ABC, abstractmethod

class Transacao(ABC):
    @property
    @abstractmethod  
    def valor(self):
        pass  # Propriedade abstrata para obrigar subclasses a implementar

    @abstractmethod
    def registrar(self, conta):
        pass  # Método abstrato para obrigar subclasses a implementar

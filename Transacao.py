from abc import ABC, abstractclassmethod, abstractproperty


class Transacao(ABC):
    @property
    @abstractproperty  
    def valor(self):
        pass
    
    @abstractclassmethod
    def Registrar(self, conta):
        pass 
    
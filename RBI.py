from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def depositAmount(self):
        pass
    @abstractmethod
    def withdrawAmount(self):
        pass
    @abstractmethod
    def checkBalanace(self):
        pass

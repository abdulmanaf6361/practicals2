from abc import ABC, abstractmethod

class Marriage(ABC):
    @abstractmethod
    def perform_marriage(self):
        pass

class IndianMarriage(Marriage):
    def perform_marriage(self):
        print("implemented")

im = IndianMarriage()
im.perform_marriage()
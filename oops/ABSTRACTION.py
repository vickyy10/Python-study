from abc import ABC, abstractmethod

class vehile(ABC):
     def __init__(self,n):
        self.no_tyre=n
        
    @abstractmethod
    def start(self):
        pass

class bike():
    def __init__(self):
        self.no_tyre=2

    def start(self):
        print("start with kick")

class scootye():
    def __init__(self):
        self.no_tyre=2

    def start(self):
        print("start with self")

class car():
    def __init__(self):
        self.no_tyre=4

    def start(self):
        print("start with key")


v=vehile(4)
from abc import ABC, abstractmethod


class Engine(ABC):
    data_frame = None
    
    @abstractmethod
    def read_csv(self, path: str):
        pass
    
    @abstractmethod
    def avg(self, dimensions: (list, str), metrics: (list, str)):
        pass
    
    @abstractmethod
    def filter(self, column, condition):
        pass
    
    @abstractmethod
    def to_dict(self):
        pass

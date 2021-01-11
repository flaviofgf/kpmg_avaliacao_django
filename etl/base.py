from abc import ABC, abstractmethod


class Engine(ABC):
    @property
    def data_frame(self):
        raise NotImplementedError
    
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
    def to_csv(self) -> str:
        pass
    
    @abstractmethod
    def to_json(self) -> str:
        pass

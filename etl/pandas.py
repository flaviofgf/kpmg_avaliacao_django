import pandas as pd

from .base import Engine


class Pandas(Engine):
    data_frame: pd.DataFrame = None
    
    def read_csv(self, path: str):
        self.data_frame = pd.read_csv(path, header=0)
        
        return self
    
    def avg(self, dimensions: (list, str), metrics: (list, str)):
        if isinstance(metrics, str):
            metrics = [metrics]
        
        self.data_frame = self.data_frame.groupby(dimensions)[metrics] \
            .mean() \
            .reset_index() \
            .rename(columns={metric: f'avg({metric})' for metric in metrics})
        
        return self
    
    def filter(self, column, condition):
        self.data_frame = self.data_frame[self.data_frame[column] == condition]
        
        return self
    
    def to_dict(self):
        return self.data_frame.to_dict('records')

import pandas as pd
from pyspark.sql import DataFrame, functions as f, SparkSession

from .base import Engine


class Spark(Engine):
    data_frame: DataFrame = None
    spark: SparkSession = None
    
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName('kpmg_avaliacao_django') \
            .master('spark://spark:7077') \
            .config('spark.submit.deployMode', 'client') \
            .config('spark.executor.memory', '512M') \
            .config('spark.cores.max', 1) \
            .getOrCreate()
    
    def read_csv(self, path: str):
        self.data_frame = self.spark.read.csv(path, header=True, inferSchema=True)
        
        return self
    
    def avg(self, dimensions: (list, str), metrics: (list, str)):
        if isinstance(dimensions, str):
            dimensions = [dimensions]
        
        if isinstance(metrics, str):
            metrics = [metrics]
        
        self.data_frame = self.data_frame \
            .groupby(*dimensions) \
            .avg(*metrics) \
            .sort(dimensions)
        
        return self
    
    def filter(self, column, condition):
        self.data_frame = self.data_frame.filter((f.col(column) == condition))
        
        return self
    
    def to_pandas(self) -> pd.DataFrame:
        return self.data_frame.toPandas()
    
    def to_csv(self):
        return self.to_pandas().to_csv(index=False, float_format='%.0f')
    
    def to_json(self):
        return self.to_pandas().to_json(orient='records', double_precision=0)

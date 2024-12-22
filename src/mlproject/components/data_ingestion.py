## Mysql ----> Train test split 
# Import necessary Libraries
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from src.mlproject.utils import read_sql_data

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Configuration class for dataingestion
@dataclass
class DataIngestionConfig:
    train_data: str = os.path.join('artifacts', 'train_data.csv')
    test_data: str = os.path.join('artifacts', 'test_data.csv')
    raw_data: str = os.path.join('artifacts', 'raw_data.csv')

# Data ingestion class
class DataIngestion:
    # from here, class implementation will begin
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            ## reading the data from mysql database
            df=read_sql_data()
            logging.info("Reading completed mysql database")
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data, index=False,header=True)
            
            train_set,test_set = train_test_split(df,test_size=0.2, random_state=32)
            train_set.to_csv(self.ingestion_config.train_data, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data, index=False,header=True)
            
            logging.info("Data Ingestion is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
        
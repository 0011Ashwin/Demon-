## Import necessary Libraries
from src.mlproject.logger import logging 
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys




 
if __name__=="__main__":
    ## Log the execution start
    logging.info("The execution has started")
    
    try:
        ## Create an instance of DataIngestion
        data_ingestion=DataIngestion()
    
        ## Start the data ingestion process
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        ##Log show error in data ingestion
        logging.error("Error in data ingestion")
        
        ## Raise custom exception with error message details
        raise CustomException(e, sys)
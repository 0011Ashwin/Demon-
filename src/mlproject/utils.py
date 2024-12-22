import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

# Load enviroment variables for .env file ## hold mysql database details
load_dotenv()

# Get database connection details from .env file for databse.
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    ## Log start of SQL reading process.
    logging.info("Reading SQL database started")
    try:
        
        ## Establish connection to mysql database.
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        ## Read data from databse and return as dataframe.
        logging.info("Connection established", mydb)
        ## Read data student table from college database.
        df = pd.read_sql_query('Select * from student', mydb)
        print(df.head())
        return df
        
    except Exception as ex:
        ## Raise custom exception with error details.
        raise CustomException(ex)
    
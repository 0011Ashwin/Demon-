import logging
import os
from datetime import datetime

## Genrate a log file based on current date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

## create the full path for the log file 
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

## create the directory if not exsits
os.makedirs(log_path,exist_ok=True)

##create the full path for log file 
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

## configure the Logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
)

# log all info into textfile
import logging # this is inbuilt # track by logging the process
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"# text file with name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # log file with current working directory
os.makedirs(logs_path,exist_ok=True)# keep appending even if there already exist files

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig( # to overwrite logging we need to alter basic config
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# for testing
# if __name__=='__main__':
#     logging.info("logging has started")
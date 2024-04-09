import os
import sys

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.exception import CustomException
from src.logger import logging
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig
import pandas as pd

from src.components.data_transformation import DataTransformationConfig,DataTransformation

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# dataclass used to create class variables
# read the data from the source and split it into train and test

@dataclass # we can directly define class variable
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") #output path its a path for saving output 
    test_data_path: str =os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

# can create a new folder config entity and give the config class there

class DataIngestion:
    def __init__(self): #constructor
        self.ingestion_config=DataIngestionConfig() #the above 3 paths will be savwd in ingestion_config

    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df=pd.read_csv('src/notebook/dataset/stud.csv') # can be read from other sources as well #here frm the system itself
            logging.info("read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) #to make directories if its present then we can use it #exist_ok=True

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) # raw data is saved here

            logging.info("Train-test-split initiate")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path) #can be directly give to next data transformation to work on train test data
        except Exception as e:
            raise CustomException(e,sys)
        
# for testing
if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr, *_ =data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer=ModelTrainer()
    print(model_trainer.initate_model_trainer(train_arr,test_arr))

# run by --> python -m src.components.data_ingestion


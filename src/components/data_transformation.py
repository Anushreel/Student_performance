# input from data ingestion and do transformation
import os
import sys
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_path: str=os.path.join('artifacts',"preprocessor.pkl") #output path its a path for saving output data

class DataTransformation:
    def __init__(self):
        self.transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self): # we get all pickel file tat will do data transformation
        '''This class is responsible for all data transformation based on different types of data'''
        try:
            numerical_columns=['writing_score','reading_score']
            categorical_columns=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
        
            numerical_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy='median')),
                                        ("scaler",StandardScaler())])
            
            categorical_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy='most_frequent')),
                                                 ("OHE",OneHotEncoder())])
            
            logging.info("numerical and categorical scaling and encoding completed")

            preprocessor=ColumnTransformer([("numerical_pipeline",numerical_pipeline,numerical_columns),
                                            ("categorical_pipeline",categorical_pipeline,categorical_columns)])
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Datatransformation begin")
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            preprocessor_obj=self.get_data_transformer_object()
            logging.info("preprocessor object read")

            target_column_name="math_score"
            numerical_columns=['writing_score','reading_score']

            X_train_df=train_df.drop(columns=[target_column_name],axis=1)
            X_test_df=test_df.drop(columns=[target_column_name],axis=1)
            y_train_df=train_df[target_column_name]
            y_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing dataframe.")

            X_train_arr=preprocessor_obj.fit_transform(X_train_df)
            X_test_arr=preprocessor_obj.transform(X_test_df)

            train_arr=np.c_[
                X_train_arr,np.array(y_train_df)
            ]
            test_arr=np.c_[X_test_arr,np.array(y_test_df)]
            # np.c_: This is a method provided by NumPy for concatenating arrays along the second axis, which effectively means concatenating them column-wise.

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.transformation_config.preprocessor_obj_path,
                obj=preprocessor_obj
            )
            return (train_arr,test_arr,self.transformation_config.preprocessor_obj_path)


        except Exception as e:
            raise CustomException(e,sys)
        



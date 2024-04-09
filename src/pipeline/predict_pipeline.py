# simple web application 
import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass 
    
    def predict(self,feartures):
        try:
            model_path=os.path.join('artifacts','model.pkl')
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            
            logging.info('loaded model and preprocessor')

            data_scaled=preprocessor.transform(feartures)
            predic=model.predict(data_scaled)

            logging.info('prediction done')
            
            return predic
        
        except Exception as e:
            raise CustomException(e,sys)

class CustomData: # responsible to map all the input from front end(html) to backend
    def __init__(self,gender:str,race_ethnicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:int,
                 writing_score:int
                 ):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score


    def get_input_dataframe(self):
        try:
            input_data={"gender":[self.gender],
                        "race_ethnicity":[self.race_ethnicity],
                        "parental_level_of_education":[self.parental_level_of_education],
                        "lunch":[self.lunch],	
                        "test_preparation_course":[self.test_preparation_course],
                    	"reading_score":[self.reading_score],	
                        "writing_score":[self.writing_score]}
            
            return pd.DataFrame(input_data)
        
        except Exception as e:
            raise CustomException(e,sys)

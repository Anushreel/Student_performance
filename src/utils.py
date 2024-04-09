# has common functions that entire project use
import os
import sys

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


from src.exception import CustomException

import dill #helps creating pickle file

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        
        for i in range(len(list(models))):
            regressor = list(models.values())[i] # each model
            parameters=params[list(models.keys())[i]]

            gs=GridSearchCV(estimator=regressor,param_grid=parameters,cv=3)
            gs.fit(X_train,y_train)
            
            regressor.set_params(**gs.best_params_)
            regressor.fit(X_train,y_train)

            y_train_predict=regressor.predict(X_train)
            y_test_predict=regressor.predict(X_test)

            train_model_score=r2_score(y_train,y_train_predict)
            test_model_score=r2_score(y_test,y_test_predict)

            report[list(models.keys())[i]]=test_model_score # appending models

        return report 
    
    except Exception as e:
        raise CustomException(e,sys)
    

def load_object(file_path):
        try:
            with open(file_path,"rb") as file_obj:
                return dill.load(file_obj)
            
        except Exception as e:
            raise CustomException(e,sys)
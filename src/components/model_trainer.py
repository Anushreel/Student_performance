# model training use all the models as we dont know wats  the best
# input from data transformation --> preprocessor
import os
import sys
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
# from xgboost import XGBRegressor
from sklearn.ensemble import AdaBoostRegressor,RandomForestRegressor
from sklearn.svm import SVR

from catboost import CatBoostRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("split training and test input data")

            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={"Linear Regression": LinearRegression(),
            "K- Neighbors Regressor":KNeighborsRegressor(),
            "Decision Tree":DecisionTreeRegressor(),
            "Random Forest":RandomForestRegressor(),
            # "XGBRegressor":XGBRegressor(),
            "Cat Boost":CatBoostRegressor(verbose=False),
            "AdaBoost Regressor":AdaBoostRegressor()}

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            ## best model score  from dictonary
            best_model_score=max(sorted(model_report.values()))

            # to get best model name from dict
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("no best model found")
            logging.info("best model found on both training and testing dataset")

            save_object(file_path=self.model_trainer_config.trained_model_path,
                        obj=best_model)
            
            predicted=best_model.predict(X_test)
            r2_square=r2_score(y_test,predicted)

            return (best_model_name,r2_square)

            
        except Exception as e:
            raise CustomException(e,sys)
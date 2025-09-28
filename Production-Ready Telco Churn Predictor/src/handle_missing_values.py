import groq
import logging
import pandas as pd
from enum import Enum
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel
from abc import ABC, abstractmethod
logging.basicConfig(level=logging.INFO, format=
    '%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()


class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) ->pd.DataFrame:
        pass

class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, critical_columns=[]):  #default value set to empty. we can override this
        self.critical_columns = critical_columns 
        logging.info(f"Dropping rows with missing values in critical columns: {self.critical_columns}")

    def handle(self, df):
        df_cleaned = df.dropna(subset=self.critical_columns)
        n_dropped = len(df) - len(df_cleaned)
        logging.info(f"{n_dropped} has been dropped")
        return df_cleaned


    
class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    """ 
    Missing -> TotalCharges
    """
    def __init__(
                self, 
                method='constant', 
                fill_value=0, 
                relevant_column=None, 
                is_custom_imputer=False,
                custom_imputer=None
                ):
        self.method = method
        self.fill_value = fill_value
        self.relevant_column = relevant_column
        self.is_custom_imputer = is_custom_imputer
        self.custom_imputer = custom_imputer

    def handle(self, df):
        if self.is_custom_imputer:
            return self.custom_imputer.impute(df)
        df[self.relevant_column] = df[self.relevant_column].str.strip().fillna(0)
        logging.info(f'Missing values filled in column {self.relevant_column}.')
        return df
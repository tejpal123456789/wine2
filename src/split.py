import os
from core.config import config_data
from core.logger import Logger
import pandas as pd
from get_data import getdata
from load import load_data
import numpy as np
from sklearn.model_selection import train_test_split
class split_data:
    def __init__(self,logger_name,config_path):
        self.logger_name=logger_name
        self.config_path=config_path
        self.logger=Logger(self.logger_name)

    def split_and_save(self):
        try:
          self.logger.info('start loading and splitting the data')
          c=config_data(self.logger_name,self.config_path)
          params=c.read_params(self.config_path)
          test_data_path=params['split_data']['test_path']
          train_data_path=params['split_data']['train_path']
          random_state=params['base']['random_state']
          split_size=params['split_data']['test_split']
          l=load_data(self.logger_name,self.config_path)
          l.load_and_save()
          raw_dataset_path=params['load_data']['raw_dataset_csv']

          df_data=pd.read_csv(raw_dataset_path,sep=',')
          train,test=train_test_split(df_data,test_size=split_size,
                                               random_state=random_state)

          train.to_csv(train_data_path)
          test.to_csv(test_data_path)

          self.logger.info('ending splitting the data ')

        except Exception:
            self.logger.exception('something has happen wrong while getting data from data source')
            raise Exception
 
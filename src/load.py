import os
from core.config import config_data
from core.logger import Logger
from get_data import getdata

class load_data:
    def __init__(self,logger_name,config_path):
        self.logger_name=logger_name
        self.config_path=config_path
        self.logger=Logger(self.logger_name)

    def load_and_save(self):
        try:
            self.logger.info('Starting loading the data ')
            getds=getdata(self.logger_name,self.config_path)
            
            params,df=getds.get_data()

            new_columns=[col.replace(' ','_') for col in df.columns]
            raw_data_path=params['load_data']['raw_dataset_csv']
            df.to_csv(raw_data_path,sep=',',index=False,header=new_columns)

            self.logger.info('ending the loading the data')
            
        except Exception:
            self.logger.exception('something has happen wrong while getting data from data source')
            raise Exception 
            





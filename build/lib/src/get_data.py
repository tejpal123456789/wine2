import os
from re import L
import yaml
import pandas as pd
import argparse
#print('teju')
import logging
from core.logger import Logger
from core.config import config_data
class getdata:
  def __init__(self,logger_name,config_path):
    self.logger_name=logger_name
    self.config_path=config_path
    self.logger=Logger(self.logger_name) 
    
  def get_data(self):
    try:
        self.logger.info('getting data from the data source')
        c=config_data(self.logger_name,self.config_path)
        params=c.read_params(self.config_path)
        
        data_path=params['data_source']['s3_source']

        df=pd.read_csv(data_path,sep=',',encoding='utf-8')

        self.logger.info('Data has been got sucuusfully')
        return params,df
    except Exception:
        self.logger.exception('something has happen wrong while getting data from data source')
        raise Exception



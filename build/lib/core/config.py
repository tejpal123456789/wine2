import os
import yaml

from core.logger import Logger


class config_data:

    def __init__(self,name,config_path):
        self.config_path=config_path
        self.name=name
        self.logger=Logger(self.name)

  
    def read_params(self,config_path):
      try:
        self.logger.info('start reading params file')
        with open(config_path) as yaml_file:
           config=yaml.safe_load(yaml_file)
        return config

      except Exception:
        self.logger.exception('Having error in reading params.yaml file')
        raise Exception
        
    
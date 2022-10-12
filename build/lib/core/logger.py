import logging

class Logger:
    def __init__(self,logger_name):
        self.logger_name=logger_name
        self.logger=logging.getLogger(self.logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler('logs/train_x' + '.log')
        self.logger.addHandler(file_handler)

    

    def info(self,message):
        self.logger.info(message)

    def exception(self,message):
        self.logger.exception(message)        
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from core.config import config_data
from core.logger import Logger
from split import split_data
import json
import joblib
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
class train:
  def __init__(self,logger_name,config_path):
        self.logger_name=logger_name
        self.config_path=config_path
        self.logger=Logger(self.logger_name)
  def eval_metrics(self,actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

  def train_and_evaluate(self):
    try:
          self.logger.info('start training the data')
          c=config_data(self.logger_name,self.config_path)
          config=c.read_params(self.config_path)
          s=split_data(self.logger_name,self.config_path)
          s.split_and_save()
          test_data_path = config["split_data"]["test_path"]
          train_data_path = config["split_data"]["train_path"]
          random_state = config["base"]["random_state"]
          model_dir = config["model_dir"]

          alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
          l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

          target = [config["base"]["Target_col"]]

          train = pd.read_csv(train_data_path, sep=",")
          test = pd.read_csv(test_data_path, sep=",")

          train_y = train[target]
          test_y = test[target]

          train_x = train.drop(target, axis=1)
          test_x = test.drop(target, axis=1)

          lr = ElasticNet(
           alpha=alpha, 
           l1_ratio=l1_ratio, 
           random_state=random_state)
          lr.fit(train_x,  train_y)

          predicted_qualities = lr.predict(test_x)
    
          (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
          self.logger.info('adding parameters and logging the test resuts')
          self.logger.info("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
          self.logger.info("  RMSE: %s" % rmse)
          self.logger.info("  MAE: %s" % mae)
          self.logger.info("  R2: %s" % r2)

#####################################################
          scores_file = config["report"]["scores"]
          params_file = config["report"]["params"]

          with open(scores_file, "w") as f:
            scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
            json.dump(scores, f, indent=4)

          with open(params_file, "w") as f:
           params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio,
        }
           json.dump(params, f, indent=4)
#####################################################


          os.makedirs(model_dir, exist_ok=True)
          model_path = os.path.join(model_dir, "model.joblib")

          joblib.dump(lr, model_path)

    except Exception:
        self.logger.exception('something has happen wrong while getting data from data source')
        raise Exception

t=train('fgh','params.yaml')

t.train_and_evaluate()
print('musku')
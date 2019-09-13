import xgboost as xgb
import random
import numpy as np

test_data_path = "./data/agaricus.txt.test"

dtest = xgb.DMatrix(test_data_path)

dsample = dtest.slice([random.choice(list(range(dtest.num_row())))])

print(dsample.get_label())

model = xgb.Booster(model_file='./model/xgb.model')

preds = model.predict(dsample)

print(preds)

sample_nd = np.random.rand(1,127)

for i in random.sample(list(range(127)),100):
    sample_nd[0,i] = np.NaN

print(model.predict(xgb.DMatrix(sample_nd)))


# -*- coding: utf-8 -* -
"""
DMatrix 使用
"""
import xgboost as xgb
import random

train_data_path = "./data/agaricus.txt.train"
test_data_path = "./data/agaricus.txt.test"

dtrain = xgb.DMatrix(train_data_path)
dtest = xgb.DMatrix(test_data_path)

print("dtrain.feature_names: ",dtrain.feature_names)
print("dtrain.num_col(): ",dtrain.num_col())
print("dtrain.num_row(): ",dtrain.num_row())
print("dtrain.get_label(): ",dtrain.get_label())
print("dtrain.get_weight(): ",dtrain.get_weight())

print()

sample_num = dtrain.num_row()
ridx = list(range(sample_num))
train_ratio = 0.7
train_num = round(sample_num*train_ratio)

train_ridx = random.sample(ridx,train_num)
eval_ridx = list(set(ridx).difference(set(train_ridx)))

train_dmat = dtrain.slice(train_ridx)
eval_dmat = dtrain.slice(eval_ridx)

print("train_dmat.num_row(): ",train_dmat.num_row())
print("eval_dmat.num_row(): ",eval_dmat.num_row())


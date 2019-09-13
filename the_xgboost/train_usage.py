# -*- coding: utf-8 -* -
import xgboost as xgb

train_data_path = "./data/agaricus.txt.train"
test_data_path = "./data/agaricus.txt.test"

dtrain = xgb.DMatrix(train_data_path)
dtest = xgb.DMatrix(test_data_path)

params = {
    'max_depth':4,
    'eta':0.5,
    'silent':1,
    'objective':'multi:softmax'
}

# specify parameters via map, definition are same as c++ version
param = {'max_depth':2, 'eta':1, 'silent':1, 'objective':'multi:softmax','num_class':2}

# specify validations set to watch performance
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
num_round = 2
bst = xgb.train(param, dtrain, num_round, watchlist)

deval = dtest.slice([11,31,51,71,91,101,102,99,43,57,66])

# this is prediction
preds = bst.predict(deval)
labels = deval.get_label()
print('error=%f' % (sum(1 for i in range(len(preds)) if preds[i] != labels[i]) / float(len(preds))))

print(preds)
print(labels)

bst.save_model('./model/xgb.model')



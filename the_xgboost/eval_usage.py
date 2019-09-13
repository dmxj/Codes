import xgboost as xgb

test_data_path = "./data/agaricus.txt.test"

dtest = xgb.DMatrix(test_data_path)

model = xgb.Booster(model_file='./model/xgb.model')

eval_results = model.eval(dtest)

print(eval_results)

def test(xgb_model,dtest):
    preds = xgb_model.predict(dtest)
    labels = dtest.get_label()

    error = sum(1 for i in range(len(preds)) if preds[i] != labels[i]) / float(len(preds))

    return error

print(test(model,dtest))

import xgboost as xgb
from matplotlib import pyplot

model = xgb.Booster(model_file='./model/xgb.model')

print("feature importance:")

if isinstance(model, xgb.XGBModel):
    importance = model.get_booster().get_score(importance_type="weight")
    print(importance)
elif isinstance(model, xgb.Booster):
    importance = model.get_score(importance_type="weight")
    print(importance)

# print("plt features importance")
#
# xgb.plot_importance(model)
#
# pyplot.show()


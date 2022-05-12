# coding: utf-8

import pandas as pd
import numpy as np 
from mlxtend.preprocessing import minmax_scaling
flank = pd.read_csv("./peaks.csv", index_col=None, header=0,sep = ',',encoding="utf-8")merge_ACTG = pd.concat([flank['T/total'], flank['N20'].str.split('', expand=True),flank['peak_overlap']], axis=1)

merge_ACTG = pd.concat([flank['T/total'], flank['N20'].str.split('', expand=True),flank['avg']], axis=1)
merge_ACTG2 = merge_ACTG.drop(['avg'],axis=1).drop(['T/total'],axis=1)
X_merge_ACTG = pd.get_dummies(merge_ACTG2) 
X_merge_ACTG.head(1)
X_merge_ACTG.dropna()
X_merge_ACTG['avg'] = X_merge_ACTG['avg'].apply(lambda x:x.split('\\')[0])
X_merge_ACTG = X_merge_ACTG[X_merge_ACTG['avg']!='none']
X_merge_ACTG['avg'] = X_merge_ACTG['avg'].astype('float')

from mlxtend.preprocessing import minmax_scaling
X_merge_ACTG['avg'] = minmax_scaling(X_merge_ACTG['avg'], columns=[0])
y = X_merge_ACTG['T/total']
X_merge_ACTG.drop(['T/total'],axis=1, inplace=True)
x = X_merge_ACTG

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0) 
xgbr=xgb.XGBRegressor(n_estimators=500,base_score=0.3,colsample_bylevel=1,colsample_bytree=0.7,gamma=0,learning_rate=0.05,max_delta_step=0,max_depth=5,min_child_weight=2,reg_alpha=0.1,reg_lambda=0.05,subsample=0.7)
xgbr.fit(x_train,y_train)
xgbr_y_predict=xgbr.predict(x_test)

feature_important = xgbr.get_booster().get_score(importance_type='weight')
keys = list(feature_important.keys())
values = list(feature_important.values())
avg_fi = 0
c_sum = 0
for i in zip(keys,values):
    if i[0] == 'avg':
        avg_fi = i[-1]
    c_sum += i[-1]
perentage = avg_fi/c_sum







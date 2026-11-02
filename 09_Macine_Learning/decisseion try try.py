import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\adars\Full_stack_data _Science_with_Ai\Full_stack_data _Science_with_Ai\09_Macine_Learning\POLYNOMIAL REGRESSION\1.POLYNOMIAL REGRESSION\emp_sal.csv")

X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 2].values 

# liner regression model 

from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X,y)

dt_reg_pred = dt_reg.predict([[6.5]])
print(dt_reg_pred)

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=45,random_state=0,max_depth=None,max_samples=5,
                             min_samples_leaf=2)
rf_reg.fit(X,y)
rf_reg_pred = rf_reg.predict([[6.5]])
print(rf_reg_pred)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn

dataset= pd.read_csv(r"C:\Users\adars\Full_stack_data _Science_with_Ai\Full_stack_data _Science_with_Ai\09_Macine_Learning\Multiple_linear_Regration\Investment_check_(Multiple_linear_Regration)\Investment.csv")
x= dataset.iloc[:,:-1]
y= dataset.iloc[:,4]

x =pd.get_dummies(x,dtype=int)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
regressor.fit(x_train,y_train)
print(regressor)



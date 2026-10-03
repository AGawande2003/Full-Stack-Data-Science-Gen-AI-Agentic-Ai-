import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn

dataset= pd.read_csv(r"C:\Users\adars\Full_stack_data _Science_with_Ai\Full_stack_data _Science_with_Ai\09_Macine_Learning\linear_regression_model\Salary_Data.csv")
x= dataset.iloc[:,:-1]
y= dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state =0)

from sklearn.linear_model import LinearRegression
regressor  = LinearRegression()
regressor.fit(x_train,y_train)
print(regressor)

y_pred = regressor.predict(x_test)
print(y_pred)

comparision =pd.DataFrame({'Actual':y_test,'Prediction': y_pred})
print(comparision)

plt.scatter(x_train,y_train,color='Red')
plt.plot(x_train,regressor.predict(x_train),color ='blue')
plt.title('SALArY OF EMPLOYEE BASED ON EXPERIENCE')
plt.xlabel('Expreience')
plt.ylabel('Salary')
plt.show()
 
m_slope = regressor.coef_
print(m_slope)

c_intecept = regressor.intercept_
print(c_intecept)

y_12 = m_slope*12+c_intecept
print(y_12)
bias= regressor.score(x_train,y_train)
print(bias)

variance = regressor.score(x_test,y_test)
print(variance)


dataset.mean()
dataset['Salary'].mean()
dataset.median()
dataset['Salary'].median()
dataset.var()
dataset['Salary'].var()

dataset.std()



#Coifeicent of Varience 

from scipy.stats import variation
variation(dataset.values)
#
#correlation

dataset.corr()

y_mean =np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)


mean_total =np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

r_square= 1-SSR/SST
print(r_square)


import pickle
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

import os
print(os.getcwd())
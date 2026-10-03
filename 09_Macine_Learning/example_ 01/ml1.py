import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\adars\Full_stack_data _Science_with_Ai\Full_stack_data _Science_with_Ai\09_Macine_Learning\Data.csv")
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,:-3].values

from sklearn.impute import SimpleImputer
imputer =SimpleImputer()

imputer = imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform[x:,1:3]

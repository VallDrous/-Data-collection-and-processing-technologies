#Сформувати NumPy-матрицю ознак X = [price,quantity,discount], стандартизувати її (центрування+масштабування), перевірити що середні≈0 і std≈1,
#та повернути результат у Pandas.

import numpy as np
import random
import pandas as pd


print(round(random.random(),2))
X_arr = []
for i in range(15000):
    X_arr.append([round(random.uniform(100,1000),2), round(random.uniform(2,80)), round(random.uniform(0,20))])
   
X = np.array(X_arr)
        
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

X_standart = (X - mean)/std

mean = np.mean(X_standart, axis=0)
std = np.std(X_standart, axis=0)

print(mean, std)
      
df = pd.DataFrame(data=X_standart, columns=['price','quantity','discount'],)

print(df.head())

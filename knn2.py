# -*- coding: utf-8 -*-
"""knn2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i8Tao-zfnzDaY7Oag3u5wcegmFxaCIhm
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

path="/content/Untitled spreadsheet (1).xlsx"
data=pd.read_excel(path)
data.head()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['size']=le.fit_transform(data['size'])
data.head()

x=data[["weight (gm)","intensity(0-10)","size"]].values # Change .value to .values
y=data[["fruite"]].values
print(x,y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
new=np.array([[140,7,2]])
prediction=knn.predict(new)
print(prediction)
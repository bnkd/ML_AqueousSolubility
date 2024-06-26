# -*- coding: utf-8 -*-
"""Solubility.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eiY48b3AZLUou7TjrBlXn0iRA3qnbD35

# ML_Project on Solubility

### Loading the Data
"""

import pandas as pd

df= pd.read_csv('https://raw.githubusercontent.com/bnkd/ML_AqueousSolubility/main/Data.csv')
df

"""### Data Prep"""

y = df['logS']
y

x = df.drop('logS' , axis = 1)
x



"""### Data Splitting

"""

from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(x, y , test_size = .1 , random_state = 63 )

"""## Building Models

### Linear Regression
"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x_train , y_train)



"""#### Training Model"""

y_lr_train_pred = lr.predict(x_train)
y_lr_test_pred = lr.predict(x_test)

"""#### Making Predictions"""

from sklearn.metrics import r2_score

"""####Accuracy Score"""

score = r2_score(y_test , y_lr_test_pred)
print( "The Accuracy of the Predicted Model is : " ,  100 * score)

"""### Random Forest"""

from sklearn.ensemble import RandomForestRegressor

"""####Training Model"""

rf = RandomForestRegressor()
rf.fit(x_train , y_train)

"""#### Making Predictions"""

y_rf_train_pred = rf.predict(x_train)
y_rf_test_pred = rf.predict(x_test)

"""#### Accuracy Score"""

from sklearn.metrics import r2_score

score = r2_score(y_test , y_rf_test_pred)
print( "The Accuracy of the Predicted Model is : " ,  100 * score)


# from sklearn.datasets import load_diabetes
# import numpy as np
# import pandas as pd 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error , mean_squared_error
# import matplotlib.pyplot as plt

# diabetes = load_diabetes()
# df = diabetes.data[:, np.newaxis,2]

# x_train = df[:-30]
# x_test = df[-20 : ]

# y_train = diabetes.target[:-30]
# y_test = diabetes.target[-20:]

# Model= LinearRegression()

# Model.fit(x_train , y_train)
# Y_predicted = Model.predict(x_test)

# print("The mean squared error is :", mean_squared_error(y_test , Y_predicted))
# print("The mean absolute error is :", mean_absolute_error(y_test , Y_predicted))
# print("The weights are :",Model.coef_)
# print("The intercept is :", Model.intercept_)
# plt.figure(figsize=(10,8))
# plt.scatter(x_test, y_test)
# plt.plot(x_test, Y_predicted)
# plt.show()


from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_absolute_error , median_absolute_error
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np 
import pandas as pd

model = LinearRegression()
diabetes = load_diabetes()
df= diabetes.data[:, np.newaxis, 2]

x_train ,x_test , y_train ,y_test,  = df[:-30] , df[-20:], diabetes.target[:-30] , diabetes.target[-20:]

model.fit(x_train, y_train)

predicted = model.predict(x_test)

plt.scatter(x_test, y_test)
plt.plot(x_test, predicted)
plt.show()

def r_squared(actual,predicted):
    actual=list(actual)
    predicted=list(predicted)
    rsqn=0
    rsqd=0
    themean =0
    for i in actual:
        themean+=i
    themean=themean/len(actual)
    for i in range(len(actual)):
        rsqn+= (predicted[i]-themean)**2
        rsqd+= (actual[i]-themean)**2

    return rsqn/rsqd

print("The R_squared value is :",r_squared(y_test,predicted))
# print("The model score :",model.score(y_test.reshape(-1,1),predicted.reshape(-1,1)))

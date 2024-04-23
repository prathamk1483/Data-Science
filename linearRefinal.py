import numpy as np
from sklearn.datasets import load_iris,load_diabetes
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import sklearn.metrics
import seaborn as sns


# iris=load_iris()
# y=pd.DataFrame(data=iris.data,columns=iris.feature_names)
# x=pd.DataFrame(iris.target)

# x_train,x_test,y_train,y_test = train_test_split(y,x,shuffle=False,test_size=0.25)

# model=LogisticRegression()
# model.fit(x_train,y_train)

# y_pred= model.predict(x_test)

 
# print("The accuracy of our model is :",model.score(x_test,y_test)*100)

# plt.scatter(x_train, y_train)
# plt.plot(x_train, y_pred)
# plt.show()









diabetes = load_diabetes()
ddf = diabetes.data[:,np.newaxis, 2]

xtrain=ddf[:101]
xtest=ddf[100:]
ytrain=diabetes.target[:101]
ytest=diabetes.target[100:]


model = LinearRegression()
model.fit(xtrain,ytrain)

y_pred=model.predict(xtest)

print("The mean squared error is :", mean_squared_error(y_pred,ytest))
print("The mean absolute error is :", mean_absolute_error(y_pred,ytest))
print("The weights are :",model.coef_)
print("The intercept is :",model.intercept_)

plt.scatter(xtest,ytest)
plt.plot(xtest,y_pred,color = 'g')
plt.show()










# iris=pd.read_csv("Iris.csv")

# iris['Species']=iris['Species'].map({"Iris-setosa" :0,"Iris-versicolor":1,"Iris-virginica":2})
# Xx=pd.DataFrame(data=iris["SepalLengthCm"])

# x =iris[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].values
# y=iris['Species'].values

# model=LogisticRegression()

# model.fit(x,y)
# y_pred = model.predict(x)

# print("The accuracy of the model is :",model.score(x,y)*100)




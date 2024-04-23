# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import datasets , linear_model
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error ,  mean_squared_error

# model = linear_model.LinearRegression()

# iris = datasets.load_iris()
# # ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']

# iris_df = pd.DataFrame(data= iris.data, columns= iris.feature_names)
# target_df = pd.DataFrame(data= iris.target, columns= ['species'])

# def converter(specie):
#     if specie == 0:
#         return 'setosa'
#     elif specie == 1:
#         return 'versicolor'
#     else:
#         return 'virginica'

# target_df['species'] = target_df['species'].apply(converter)
# iris_df = pd.concat([iris_df, target_df], axis= 1)
# iris_df.drop('species', axis= 1, inplace= True)
# target_df = pd.DataFrame(columns= ['species'], data= iris.target)
# iris_df = pd.concat([iris_df, target_df], axis= 1)

# X= iris_df.drop(labels= 'sepal length (cm)', axis= 1)
# y= iris_df['sepal length (cm)']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.33, random_state= 101)

# model.fit(X_train, y_train)
# pred = model.predict(X_test)


# print('Mean Absolute Error:', mean_absolute_error(y_test, pred))
# print('Mean Squared Error:', mean_squared_error(y_test, pred))
# print('Mean Root Squared Error:', np.sqrt(mean_squared_error(y_test, pred)))










# from sklearn.datasets import load_diabetes
# from sklearn.metrics import mean_absolute_error , mean_squared_error
# from sklearn.linear_model import LinearRegression
# import numpy as np
# import pandas as pd 
# import matplotlib.pyplot as plt

# model = LinearRegression()
# # ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']
# diabetes = load_diabetes()
# Diabetes = diabetes.data

# x_train = Diabetes[:-30]
# x_test =  Diabetes[20:]

# y_train = diabetes.target[:-30]
# y_test =  diabetes.target[20:]


# model.fit(x_train , y_train)
# predicted = model.predict(x_test)

# print("Mean Squared error is :" , mean_squared_error( y_test ,predicted ))
# print("Mean Absolute error is :" , mean_absolute_error( y_test ,predicted ))
# print("Weights :" , model.coef_)
# print("Intercept" , model.intercept_)









# from sklearn.datasets import load_iris
# import numpy as np 
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error , mean_squared_error

# iris = load_iris()

# iris_df = iris.data

# x_train = iris_df[:-20]
# x_test = iris_df[20:]
# y_train = iris.target[:-20]
# y_test = iris.target[20:]

# model = LinearRegression()
# model.fit(x_train , y_train)

# predict = model.predict(x_test)

# print("Mean absolute error is :", mean_absolute_error(y_test , predict ))


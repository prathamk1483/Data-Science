from sklearn.datasets import load_iris
import pandas as pd 
from sklearn.linear_model import LinearRegression

i = load_iris()
idf=pd.DataFrame(data=i.data , columns=i.feature_names)
print(idf)


outcome_df= pd.DataFrame(i.target , columns=['Species'])


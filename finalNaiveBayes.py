# from sklearn.metrics import accuracy_score
# from sklearn.model_selection import train_test_split
# from sklearn.naive_bayes import GaussianNB
# import pandas as pd 
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import confusion_matrix

















                






























from sklearn.metrics import confusion_matrix , accuracy_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report


d=pd.read_csv("diabetes.csv")
print(d.head().to_string())

print(d.isnull().sum())



x= d.drop("Outcome", axis='columns')
y= d["Outcome"]

scaler = StandardScaler()

standardised_data=scaler.fit_transform(x)

x_train , x_test,y_train , y_test =train_test_split(standardised_data,y,shuffle=False,test_size=0.2)

gnb =GaussianNB()

gnb.fit(x_train,y_train)

y_pred =gnb.predict(x_test)


print(y_pred)
print("The accuracy score of our model is :",accuracy_score(y_pred , y_test)*100)

print("The error rate made by our model is :",100-accuracy_score(y_pred , y_test)*100)


cm = confusion_matrix(y_pred,y_test)
print("The confusion matrix is :\n", cm)



print("The classification report is as followe :\n",classification_report(y_test,y_pred))

def converter(value):
    if value ==1:
        return "Yes"
    else :
        return 'No'

expected =pd.DataFrame(list(y_test),columns=['Expected'])
predicted = pd.DataFrame(y_pred, columns=['Predicted'])
result = pd.concat([expected, predicted],axis=1)
result['Expected'] = result['Expected'].apply(converter)
result['Predicted'] = result['Predicted'].apply(converter)

print(result.head())


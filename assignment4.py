# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import MaxAbsScaler
# import numpy as np
# from scipy import stats
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv("Academic_performance.csv")
# df.drop(['Timestamp', 'Email Address'], axis=1, inplace=True)
# print(df.isnull().sum())

# df['MHT_CET_Score'].fillna(method='ffill', inplace=True)
# df['JEE_Main_score'].fillna(method='ffill', inplace=True)
# df['Details_certification'].fillna('None', inplace=True)
# df['Score_of_Online_certification'].fillna(0, inplace=True)
# df['stars_hackerrank'].fillna(0, inplace=True)
# df['stars_codechef'].fillna(0, inplace=True)
# df['No_of_success_problems_codechef'].fillna(0, inplace=True)
# df['No_of_success_problems_hackerrank'].fillna(0, inplace=True)
# df['No_of_success_problems_leetcode'].fillna(0, inplace=True)

# print('-'*120)

# print(df.isnull().sum())

# df['CPPS1_theory_grade'] = df['CPPS1_theory_grade'].replace({'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'F': 0})
# df['CPPS2_theory_grade'] = df['CPPS2_theory_grade'].replace({'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'F': 0})

# df['CPPS1_theory_grade']=df['CPPS1_theory_grade'].astype(int)
# df['CPPS2_theory_grade']=df['CPPS2_theory_grade'].astype(int)
# df['stars_hackerrank']=df['stars_hackerrank'].astype(int)
# df['stars_codechef']=df['stars_codechef'].astype(int)

# for i in df['CPPS1_theory_grade']:
#     a=i
#     if i>=40:
#         i=8
#     elif i>=45:
#         i=9
#     df['CPPS1_theory_grade']=df['CPPS1_theory_grade'].replace({a : i})
# for i in df['CPPS2_theory_grade']:
#     a=i
#     if i>=40:
#         i=8
#     elif i>=45:
#         i=9
#     elif i>=30:
#         i=6
#     elif i>=35:
#         i=7
#     df['CPPS2_theory_grade']=df['CPPS2_theory_grade'].replace({a : i})

# df['CPPS1_theory_grade']=df['CPPS1_theory_grade'].astype(int)
# df['CPPS2_theory_grade']=df['CPPS2_theory_grade'].astype(int)
# df['stars_hackerrank']=df['stars_hackerrank'].astype(int)
# df['stars_codechef']=df['stars_codechef'].astype(int)
# df['Last_Year_CGPA']=df['Last_Year_CGPA'].replace({ '.' : 0})
# df['Last_Year_CGPA']=df['Last_Year_CGPA'].astype(float)

# sns.displot(df['CPPS1_theory_grade'])
# sns.displot(df['CPPS2_theory_grade'])

# Q1=np.percentile(df['Last_Year_CGPA'],25)

# Q3=np.percentile(df['Last_Year_CGPA'],75)
# IQR = Q3 - Q1
# upper=df['Last_Year_CGPA']>=(Q3+1.5*IQR)
# print('-'*200)
# print("Upper bound:",upper)
# print(np.where(upper))
# lower=df['Last_Year_CGPA']<=(Q1-1.5*IQR)
# print('-'*200)
# print("Lower bound:",lower)
# print(np.where(lower))
# plt.show()




import seaborn as sns 
from scipy import stats
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

file= pd.read_csv("Academic_performance.csv")
df=pd.DataFrame(data = file._data)
df.drop(['Timestamp','Email Address'],axis=1 , inplace=True)
# print(df)
# print("*"*150)
# print(df.isnull().sum())
# print("*"*150)

df.fillna(method='ffill',inplace=True)
# print(df.isnull().sum())

# Details_certification                3
# Score_of_Online_certification        4

df['Details_certification'].fillna("unknown",inplace=True)
df['Score_of_Online_certification'].fillna("unknown",inplace=True)


# print("*"*150)
# print("*"*150)
# print(df.isnull().sum())

df['CPPS1_theory_grade'] = df['CPPS1_theory_grade'].replace({
   'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'F': 0})
df['CPPS1_theory_grade'] = df['CPPS1_theory_grade'].astype(int)
for i in df['CPPS1_theory_grade']:
    a=i
    if(i>=40):
        i=8
    elif( i>=45):
        i=9
    elif(i>=30):
        i=6
    elif (i>=35):
        i=7

    df['CPPS1_theory_grade']=df['CPPS1_theory_grade'].replace({a: i})

df['CPPS2_theory_grade'] = df['CPPS2_theory_grade'].replace({
   'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'F': 0})
df['CPPS2_theory_grade'] = df['CPPS2_theory_grade'].astype(int)
df['stars_hackerrank'] = df['stars_hackerrank'].astype(int)
for i in df['CPPS2_theory_grade']:
    a=i
    if(i>=40):
        i=8
    elif( i>=45):
        i=9
    elif(i>=30):
        i=6
    elif (i>=35):
        i=7

    df['CPPS2_theory_grade']=df['CPPS2_theory_grade'].replace({a: i})

sns.displot(df['CPPS1_theory_grade'])
sns.displot(df['CPPS2_theory_grade'])
plt.show()
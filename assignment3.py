# import pandas as pd
# import numpy as np

# anime = pd.read_csv("anime.csv")
# df = pd.DataFrame(data= anime)
# print(df.isnull().sum() , end='\n\n\n\n\n')

# print(df)
# df.fillna(inplace=True , method='ffill')
# df.fillna("unknown",inplace=True)
# print(df.isnull().sum())

# import pandas as pd
# anime= pd.read_csv("anime.csv")
# df = pd.DataFrame(data=anime)
# print(df.isnull().sum())

# print("*"*70)

# df.info()
# print("*"*70)
# df.fillna(method='ffill', inplace=True)
# print(df.isnull().sum())

# df['mediaType']=df['mediaType'].astype(str)
# df['title']=df['title'].astype(str)
# df['eps']=df['eps'].astype(str)
# df['duration']=df['duration'].astype(str)
# df['ongoing']=df['ongoing'].astype(str)

# print("After conversion.")
# print(df.info())




# title           0
# mediaType       0
# eps             0
# duration        1
# ongoing         0
# startYr         0
# finishYr        0
# sznOfRelease    0
# description     0
# studios         0
# tags            0
# contentWarn     0
# watched         0
# watching        0
# wantWatch       0
# dropped         0
# rating          0
# votes           
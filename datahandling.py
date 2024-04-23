import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def converter(astring):
    astring=str(astring)
    return astring

anime = pd.read_csv("anime.csv")
print(anime.isnull().sum())


print("-"*80)
anime.drop(['description','mediaType','contentWarn','wantWatch','watching','votes','dropped','watched'],inplace=True,axis=1)
print(anime.isnull().sum())



anime["eps"].fillna(method='ffill',inplace=True)
anime["duration"].fillna(anime['duration'].mean(),inplace=True)
anime["startYr"].fillna(method='bfill',inplace=True)
anime["finishYr"].fillna(method='ffill',inplace=True)
anime["sznOfRelease"].fillna(method='ffill',inplace=True)
anime['rating'].fillna(anime['rating'].mean(),inplace=True)
print("-"*80)
print(anime.isnull().sum())

scaler = StandardScaler()

anime['rating']=scaler.fit_transform(pd.DataFrame(anime['rating']))

print(anime.info())





anime['eps'] = anime['eps'].astype(int)
anime['startYr'] = anime['startYr'].astype(int)
anime['finishYr'] = anime['finishYr'].astype(int)
anime['tags'] = anime['tags'].astype('str')

print(anime.info())
print("-"*80)
print(anime.isnull().sum())

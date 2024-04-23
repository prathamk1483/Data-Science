import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np

iris = pd.read_csv("Iris.csv")
iris = iris.drop('Id',axis=1)
iris=iris.drop('Species',axis=1)

# SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm         Species
sns.boxplot(iris)
plt.show()

plt.xlabel("SepalLengthCm")
sns.boxplot(iris["SepalLengthCm"])
plt.show()

plt.xlabel("SepalWidthCm")
sns.boxplot(iris["SepalWidthCm"])
plt.show()

plt.xlabel("PetalLengthCm")
sns.boxplot(iris["PetalLengthCm"])
plt.show()

plt.xlabel("PetalWidthCm")
sns.boxplot(iris["PetalWidthCm"])
plt.show()

plt.xlabel("SepalWidthCm")
plt.ylabel("Count")
plt.title("Sepal Width CM Histogram")
data=iris["SepalWidthCm"]
plt.hist(data, bins=20 , color='red',edgecolor='black')
plt.show()

plt.xlabel("SepalLengthCm")
plt.ylabel("Count")
plt.title("Sepal Length CM Histogram")
data=iris["SepalLengthCm"]
plt.hist(data, bins=20 , color='red',edgecolor='black')
plt.show()

plt.xlabel("PetalLengthCm")
plt.ylabel("Count")
plt.title("Petal Length CM Histogram")
data=iris["PetalLengthCm"]
plt.hist(data, bins=20 , color='red',edgecolor='black')
plt.show()

plt.xlabel("PetalWidthCm")
plt.ylabel("Count")
plt.title("Petal Width CM Histogram")
data=iris["PetalWidthCm"]
plt.hist(data, bins=20 , color='red',edgecolor='black')
plt.show()

IRIS = pd.read_csv("Iris.csv")
IRIS= pd.DataFrame(IRIS)
sns.pairplot(IRIS)
plt.show()

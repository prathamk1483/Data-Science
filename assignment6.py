import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file = pd.read_csv("diabetes.csv")
df = pd.DataFrame(data=file)

plt.title("The scatterPlot of Age vs BMI")
sns.scatterplot( data=df, sizes= (2,200), alpha= 0.8, color='violet')
plt.show()

plt.title("Total data lineplot")
plt.plot(df, color='blue')
plt.show()

plt.title("Histogram of Age")
plt.hist(df['Age'], color='blue' , edgecolor='black')
plt.show()

plt.title("The bar plot of Age vs BMI")
plt.bar(df["Age"], df["BMI"], color='yellow', edgecolor='black',width=5)
plt.show()

plt.title("Density plot fo the BMI.")
df.BMI.plot.density(color='blue')
plt.show()

plt.title("LinePlot of the Pregnancies.")
plt.plot(df["Pregnancies"], color='blue')
plt.show()

plt.title("The Heatmap")
plt.imshow(df.head(),cmap='magma',interpolation='nearest')
plt.show()

plt.title("Pie chart for glucose levels of 5 subjects.")
a=df["Glucose"].head()
plt.pie(a,labels=[1,2,3,4,5])
plt.show()

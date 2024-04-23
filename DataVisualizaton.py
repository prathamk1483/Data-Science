import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

iris= pd.read_csv("Iris.csv")

# sns.pairplot(iris,hue='Species')
# irisdf=iris.drop(['Id','Species'],axis=1)
# iris.drop(["Id"],inplace=True)
# plt.xlabel('Sepal Length')
# plt.ylabel('Number of Values')
# plt.title("Sepal Length Histogram")
# plt.hist(irisdf['SepalLengthCm'],color='red', edgecolor='black')
# plt.show()


plt.title("Sepal Length Boxplot")
plt.xlabel("Sepal Length")
plt.ylabel("sldjfsdjf")
sns.boxplot(data=iris['SepalLengthCm'])
plt.boxplot(iris['SepalLengthCm'])
plt.show()

# sns.boxplot(irisdf)
# plt.show()



# plt.bar(irisdf['SepalLengthCm'].head(),irisdf["SepalWidthCm"].head(),width=1.1,edgecolor="black")
# plt.show()


# plt.plot(irisdf["SepalLengthCm"])                                                               #didnt work
# plt.show()

# sns.heatmap(irisdf['SepalLengthCm'].head())
# plt.show()

# sns.heatmap(iris.corr(),cmap='magma',annot=True)
# plt.show()

# plt.pie(irisdf["SepalLengthCm"].head(),labels=[0,1,2,3,4],explode=[0,0.1,0,0,0])
# plt.show()


# sns.scatterplot(data=irisdf,x="SepalLengthCm",y="SepalWidthCm", size=20, sizes=(20, 2000))
# plt.show()







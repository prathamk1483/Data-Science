from sklearn.datasets import load_iris
import numpy as np
import pandas as pd 

iris=load_iris()
iris=pd.DataFrame(data=iris.data,columns=iris.feature_names)

SpL = np.mean(iris['sepal length (cm)'])

print(SpL)

# Null Hypothesis - there is no significant difference in population mean and sample mean Pm=SpL  Sm=5
# Alternate Hypothesis -  there is significant difference in population mean and sample mean

sample_size=20
sample = np.random.choice(iris['sepal length (cm)'],sample_size)

from scipy.stats import ttest_1samp , ttest_ind

ttest,p_val = ttest_1samp(sample,5)
print(p_val)
print("One sample T-test.")
if p_val <0.05:
    print("We are rejecting null hypothesis.")
else:
    print("We are accepting null hypothesis.")


sample = pd.DataFrame(iris[['sepal length (cm)','sepal width (cm)']])
sample= sample[:30]
print(sample)
ttest , p_val=ttest_ind(sample['sepal length (cm)'],sample['sepal width (cm)'])
print(p_val)

print("Two sample T-test(paired).")
if p_val <0.05:
    print("We are rejecting null hypothesis.")
else:
    print("We are accepting null hypothesis.")



# _______________________________CHI2 Test___________________________________________________

from seaborn import load_dataset
from scipy.stats import chi2_contingency
tip = load_dataset('tips')

print(tip)
dataset = pd.crosstab(tip['sex'],tip['smoker'])
stat, p, dof, expected = chi2_contingency(dataset)
print("The observed values are :",dataset.values)
print(stat, p, dof, expected)

alpha =0.05
# _________________________ CHI2 = sum((observed-expected)**2/expected)

if p < 0.05:
    print("We are rejecting null hypothesis.")
else :
    print("We are accepting null hypothesis.")


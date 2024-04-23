#######################################################  THIS FILE DEMONSTRATE THE STATISTICAL ANALYSIS FROM SCRATCH ####################################
def mean(tomean):
    tomean=list(tomean)
    sum=0
    for i in tomean:
        sum+=i
    return sum/len(tomean)




def median(tomedian):
    tomedian=sorted(list(tomedian))
    thelen =len(tomedian)
    if thelen%2==0:
        return (tomedian[int(thelen/2)] + tomedian[int(thelen/2 +1)])/2
    else :
        return tomedian[int((thelen +1)/2)]



def mode(tomode):
    toiter = list(tomode)
    tomode =list(tomode.value_counts())
    max=-1
    for i in tomode:
        if(i > max):
            max=i
    for i in toiter:
        if toiter.count(i)==max:
            return i





def variance(tovar):
    tovar=list(tovar)
    var=0
    for i in tovar:
        var += (i-mean(tovar))**2
    return var/(len(tovar)-1)



def stdex(tostd):
    return variance(tostd)**(0.5)





def quantile(toquantile, whichquantile):
    toquantile = sorted(list(toquantile))
    if whichquantile>=0 and whichquantile<=1:
        return     toquantile[int(whichquantile  * (len(toquantile) +1 )) ]
    else :
        return toquantile[int((whichquantile/100) * (len(toquantile) +1 )) ]




def iqr(toiqr):
    return quantile(toiqr,75) -quantile(toiqr, 25)




def kurtosis(tokurt):
    tokurt=list(tokurt)
    kurt=0
    themean = mean(tokurt)
    for i in tokurt:
        kurt += (i-themean)**4
    return kurt / (len(tokurt) * (stdex(tokurt)**4))




def skew(toskew):
    toskew=list(toskew)
    skew = 0
    n = len(toskew)
    themean=mean(toskew)
    stdev = stdex(toskew)
    for i in toskew:
        skew += ((i-themean)/stdev)**3
    return (n/((n-1) *(n-2))) * skew


def pearson_coef(col1,col2):
    col1=list(col1)
    col2=list(col2)
    Nl ,Dl,Dr=0 , 0,0
    m1,m2=mean(col1),mean(col2)
    if len(col1)!=len(col2):
        return "Irregular sized."
    for i in range(len(col1)):
        Nl+= (col1[i] -m1)* (col2[i] -m2)
        Dl+= (col1[i] -m1)**2
        Dr+= (col2[i] -m1)**2

    return (Nl) / (Dl*Dr)**0.5





def main():
    import pandas as pd
    from sklearn.datasets import load_iris
    # iris=pd.read_csv("Iris.csv")
    iris = load_iris()
    iris = pd.DataFrame(data=iris.data , columns=iris.feature_names)
    # print(iris)
    print("The mean of sepal length is :",mean(iris["sepal length (cm)"]))
    print("The median of sepal length is :",median(iris["sepal length (cm)"]))
    print("The mode of sepal length is :",mode(iris["sepal length (cm)"]))
    print("The variance of sepal length is :",variance(iris["sepal length (cm)"]))
    print("The standard-deviation of sepal length is :",stdex(iris["sepal length (cm)"]))

    print("The 25th quartile of sepal lenght is :", quantile(iris['sepal length (cm)'],25))
    print("The 50th quartile of sepal lenght is :", quantile(iris['sepal length (cm)'],5))
    print("The 75th quartile of sepal lenght is :", quantile(iris['sepal length (cm)'],75))
    print("The 95th quartile of sepal lenght is :", quantile(iris['sepal length (cm)'],95), end='\n\n\n\n')

    print("The 50th quartile of sepal widht is  :", quantile(iris['sepal width (cm)'], 0.5))
    print("The 25th quartile of sepal widht is  :", quantile(iris['sepal width (cm)'], 0.25))
    print("The 75th quartile of sepal widht is  :", quantile(iris['sepal width (cm)'], 0.75))
    print("The 95th quartile of sepal widht is  :", quantile(iris['sepal width (cm)'], 0.95), end='\n\n\n\n')

    print("The kurtosis of sepal lenght is :",kurtosis(iris["sepal length (cm)"]))
    print("The skew of sepal lenght is :",skew(iris["sepal length (cm)"]))
    print("The pearsons coefficient for Sepal Length and Sepal Width is :",pearson_coef(iris["sepal length (cm)"],iris["sepal width (cm)"]))

if __name__=="__main__":
    main()

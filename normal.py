# from scipy.stats import norm 
# import numpy as np 
# import matplotlib.pyplot as plt 
# import random 
# m , sd = 5 , 7
# l , r = m-5*sd ,m+5*sd 
# x = np.linspace(l,r,2000)
# y = norm.pdf(x, loc=m , scale =sd)
# plt.plot(y , color='green')
# plt.show()


# mu , sd = 5 ,10 
# l ,r = mu - 5*sd , mu + 5*sd

# x = np.linspace(1,20,100)
# # print(x)
# y= norm.pdf(x, loc=10 , scale =sd ) 
# print(y)
# plt.plot(y)
# plt.show()

# l= []
# for i in range(21):
#     l.append(random.randint(1,20))

# for i in l:
#     print( i , "occurs " ,l.count(i) , " times")
# import sympy

# froms = int(input("Enter from values :"))
# to = int(input("Enter the to value :"))
# for i in range(froms , to+1):
#     if(i%2==0):
#         print(i)

# odd=[]
# for i in range(froms, to+1):
#     if(i%2!=0):
#         odd.append(i)

# print(odd)
# prime=[]
# for i in odd:
#     if(sympy.isprime(i)):
#         prime.append(i)
# print(prime[:20])

# tup =(1,2,3,4)
# tup = tuple(list(tup[::-1]))

# print(tup)


# dict1 = {
#     "pratham" : "kubetkar",
#     "package": "1.5cr pa",
#     "type" : "best"
# }
# dict2 = {
#     "prathamk" : "kuber",
#     "packagel": "45lpa",
#     "types" : "good"
# }

# dict2.update(dict1)
# print(dict2)



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.stats import norm 

# m , sd = 5 ,7
# l , r = m-3*sd , m+3*sd

# x= np.linspace(l,r , 1000)

# y= norm.pdf(x, loc = m , scale = sd)

# for i in y:
#     print(i,"occurs" , np.count_nonzero(y==i) ," times.")

# plt.plot(y)
# plt.show()


# import sympy

# froms = int(input("Enter starting range :"))
# to = int(input("Enter ending range :"))

# print("The even numbers are :")
# for i in range(froms , to+1):
#     if(i%2==0):
#         print(i , end= " ")

# odd=[]

# for i in range(froms , to+1):
#     if(i%2!=0):
#         odd.append(i)

# print("\nThe odd numbers are :")
# print(odd)

# print("The prime numbers are :")
# prime=[]
# for i in odd:
#     if(sympy.isprime(i)):
#         prime.append(i)

# print(prime[:20])

# import pandas as pd

# thefile = pd.read_csv(input("Please enter the file name :"))
# print(thefile)


# tup = (1,2,3,4,5,6,7,8,9,10)
# tup = tuple(reversed(list(tup)))

# print(tup)

# li=[]
# for i in tup:
#     li.append(i)

# print(li[0],li[1])


# dict1={
#     "pratham" :"kubetkat" ,
#     "pakage" : "1.5 cr",
#     "college" : "pccoe"
# }

# dict2={
#     "name" : "pccoe",
#     "isgood" : "yes" ,
#     "time" : "exam"
# }

# dict1.update(dict2)
# for i ,j in dict1.items():
#     print(i ,":",j)


# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# for i in arr:
#     print(i)

# R=int(input("Enter number of rows :"))
# C=int(input("Enter number of columns :"))

# mat1 = []
# mat2= []

# for i in range(R):
#     c=[]
#     for i in range(C):
#         a=int(input())
#         c.append(a)
#     mat1.append(c)

# for i in range(R):
#     c=[]
#     for i in range(C):
#         a=int(input())
#         c.append(a)
#     mat2.append(c)

# mat1= np.array(mat1)
# mat2=np.array(mat2)

# print(mat1 , mat2 ,sep="\n")

# print("The addition is :",mat1+mat2)
# print("The multiplication is :", mat1*mat2)
# print("The division is :", mat1/mat2)

# print("The inverse of matrix 1 is :", np.linalg.inv(mat1) , "\nThe inverse of the matrix 2 is :",np.linalg.inv(mat2))



# import numpy as np
# mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(np.transpose(mat1))


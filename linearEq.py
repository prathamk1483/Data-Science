
R = int(input("Enter no of rows :"))
C = int(input("Enter no of columns :"))
ans = []

    

def display(mat):
    global R
    global C
    for i in range(R):
        for j in range(C):
            print(mat[i][j],end=" ")
        print('')

def getmatrix():
    global R
    global C
    mat=[]
    for i in range(R):
        rows = []
        for j in range(C):
            print(i + 1, ' ', j + 1, ' =', end='')
            a = int(input())
            rows.append(a)
        mat.append(rows)
    return mat

def addition(mat1,mat2):
    global R
    global C
    global ans
    for i in range(R):
        rows=[]
        for j in range(C):
            a=mat1[i][j] +mat2[i][j]
            rows.append(a)
        ans.append(rows)
    return ans

def main():
    while(True):
        a = input("Enter a choice\n1.For solving a linear equation.\n2.For Matrices operation.\n3.Exit:")
        match a:
            case "1":
                lineareq()
                
            case "2":
                print("1.Enter a matrix 1.\n2.Enter matrix 2\n3.Display matrix.\n4.Addition\n5.Substraction\n6.Multiplication\n7.Exit")
                b=input("Enter a choice :")
                match b:
                    case "1":
                        mat1=getmatrix()
                    case "2":
                        mat2=getmatrix()
                    case "3":
                        print("mat1\n",display(mat1),"\nmat2\n",display(mat2))
                    case "4":
                        mat3=addition(mat1,mat2)
                        display(mat3)
                    case "5":
                        mat4=substraction(mat1,mat2)
                        display(mat4)
                    case "6":
                        mat5 =multiply(mat1,mat2)
                        display(mat5)
                    case "7":
                        exit()
                    case other:
                        print("Entered a invalid choice")
            case "3":
                exit()
            case other:
                print("Enter a wrong choice.")




def substraction(mat1,mat2):
    global R
    global C
    global ans
    for i in range(R):
        rows=[]
        for j in range(C):
            a=mat1[i][j] -mat2[i][j]
            rows.append(a)
        ans.append(rows)
    return ans


def multiply(mat1,mat2):
    global R
    global C
    global ans
    if R!=C:
        return 0
    else :
        for i in range(R):
            for j in range(R):
                rows=[]
                for k in range(R):
                    a = mat1[i][k] * mat2[k][j]
                    rows.append(a)
            ans.append(rows)
    return ans


def getdeterminant(mat):
    return mat[0][0]*( mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1] ) - mat[0][1]*( mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0] )   +mat[0][2]*( mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0] )


def lineareq():
    r1, c1= 3, 3
    r2 ,c2 =3 , 1
    mat1=[]
    mat2=[]
    for i in range(r1):
        print("Enter coefficients of entire equation ",i+1)
        rows=[]
        for j in range(c1):
            a = int(input())
            rows.append(a)
        mat1.append(rows)
        mat2.append(int(input()))
    from copy import deepcopy
    forX , forY ,forZ= deepcopy(mat1) ,deepcopy(mat1),deepcopy(mat1)
    D=getdeterminant(mat1)
    forX[0][0] =mat2[0]
    forX[1][0] =mat2[1]
    forX[2][0] =mat2[2]
    Dx=getdeterminant(forX)
    forY[0][1] = mat2[0]
    forY[1][1] = mat2[1]
    forY[2][1] = mat2[2]
    Dy=getdeterminant(forY)
    forZ[0][2] = mat2[0]
    forZ[1][2] = mat2[1]
    forZ[2][2] = mat2[2]
    Dz=getdeterminant(forZ)
    if(D==0):
        return "Cant show output because D=0."
    print("X=",Dx/D," Y=",Dy/D, " Z=",Dz/D)












   
if __name__=="__main__":
    
    main()
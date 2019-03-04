matrix_1=[[1,2,3],[4,5,6],[1,2,3]]
matrix_2=[[2,7,2],[0,3,1],[1,2,3]]
v=[1,2,3,4]
w=[1,2,3,4]

def my_Vectors_Inner_Product(v,w):
    size=len(v)
    my_result=[]
    result=0
    for i in range(size):
        my_result.append(0)
    for i in range(size):
        my_result[i]=v[i]*w[i]    
        result += my_result[i]
    return result

def my_Vector_Scalar_Product(alpha,v):
    size=len(v)
    my_result=[]
    for i in range(size):
        my_result.append(0)
        my_result[i] = alpha*v[i]
    return my_result

def my_Vector_Substraction(v,w):
    my_result=[]
    for i in range(len(v)):
        my_result.append(0)
        my_result[i]=v[i]-w[i]
    return my_result

def my_Vector_addition(v,w):
    my_result=[]
    for i in range(len(v)):
        my_result.append(0)
        my_result[i]=v[i] + w[i]
    return my_result

def my_matrix_addition(m1,m2):
    result=[]

    for row in range(len(m1)):
        result.append([])
        for column  in range(len(m1[row])):
            #print(m1[row][colum],end=" ")
            result[row].append(m1[row][column]+m2[row][column])
        #print()
    return result

def my_matrix_substraction(m1,m2):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[row])):
            result[row].append(m1[row][column]-m2[row][column])
    return result

def my_matrix_scalar_product(alpha,m1):
    result=[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m1[row])):
            result[row].append(m1[row][column]*alpha)
    return result
def f1 (matris1,i):
    return matris1[i]
def f2 (matris2,j):
    my_j_th_col=[]
    for row in matrix_2:
       for indis in range(len(row)):
           if (indis == j):
               my_j_th_col.append(row[indis])
    return my_j_th_col

def my_matrix_multiply(m1,m2):
    result =[]
    for row in range(len(m1)):
        result.append([])
        for column in range(len(m2[row])):
            rw=f1(m1,row)
            col=f2(m2,column)
            rs=my_Vectors_Inner_Product(rw,col)
         
            result[row].append(rs)
    return result

print(my_Vector_addition(v,w))
print(my_Vector_Substraction(v,w))
print(my_Vector_Scalar_Product(2,v))
print(my_matrix_addition(matrix_1,matrix_2))
print(my_matrix_substraction(matrix_1,matrix_2))
print(my_matrix_scalar_product(2,matrix_1))
print(my_matrix_multiply(matrix_1,matrix_2))

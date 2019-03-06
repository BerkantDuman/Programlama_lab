matrix_1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix_2=[[2,7,0,0],[0,3,4,4],[1,2,3,7],[1,2,4,6]]
matrix_3=[[1,2],[3,4]]
matrix_4=[[1,2,3],[4,5,6],[7,8,9]]
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

def matrix_2x2_det(m1):
    s1=m1[0][0]*m1[1][1]
    s2=m1[0][1]*m1[1][0]
    return s1-s2
     
def delete_row_col_from_matrix(m1,i,j):
    result=[]
    size_1=len(m1) #kaç satır var
    size_2=len(m1[0]) #kaç sutun var
    for a in range(size_1):
        if(i==a):
            continue
        row_1=[]
        for b in range(size_2):
            if(b==j):
                continue
            row_1.append(m1[a][b])
        result.append(row_1)
    return result

def matrix_3x3_det(m4):
    a_1=m4[0][0]
    a_2=delete_row_col_from_matrix(m4,0,0)
    a_3=matrix_2x2_det(a_2)
    a_4=a_1*a_3

    b_1=m4[0][1]
    b_2=delete_row_col_from_matrix(m4,0,1)
    b_3=matrix_2x2_det(b_2)
    b_4=b_1*b_3
    
    c_1=m4[0][2]
    c_2=delete_row_col_from_matrix(m4,0,2)
    c_3=matrix_2x2_det(c_2)
    c_4=c_1*c_3
    
    return a_4 - b_4 + c_4

#def matrix_4x4_det(m1):
#    if(len(m1)==3):
#        return matrix_3x3_det(m1)
#    else:
#        m1=delete_row_col_from_matrix(m1,0,0)
#        return matrix_4x4_det(m1)


#11 mart pazartesi ders saati başlangıcına aşağıdaki formatta çalışmalarınızı teslim ediniz.
#tarih  - konu  - github linki - yükleme zamanı
#arka sayfaya github hesabı linkini hazırlayarak rapor ver
#her haftanın linkini koyucaz

print(my_Vector_addition(v,w))
print(my_Vector_Substraction(v,w))
print(my_Vector_Scalar_Product(2,v))
print(my_matrix_addition(matrix_1,matrix_2))
print(my_matrix_substraction(matrix_1,matrix_2))
print(my_matrix_scalar_product(2,matrix_1))
print(my_matrix_multiply(matrix_1,matrix_2))
print(matrix_2x2_det(matrix_3))
print(delete_row_col_from_matrix(matrix_1,0,0))
print(matrix_3x3_det(matrix_1))
#print(matrix_4x4_det(matrix_2))

"""l1=["hello",8,"mango",46]
print(l1[2])
for i in l1:
    print(i)


#2d list
num=[[1,2,3],[4,5,6],[7,8,9]]
print(num[2])
print(num[2][2])
#number of rows
print(len(num))
#number of colomns
print(len(num[1]))

for i in num:
    print(i)

for i in range(3):
    print()
    for j in range(3):
        print(num[i][j],end=" ")





"""



"""rows=int(input("Enter the number of rows:"))
columns=int(input("Enter the number of columns:"))
matrix=[]
for i in range(rows):
    temp=[]
    for j in range(columns):
        num=int(input("Enter the values"))
        temp.append(num)
    matrix.append(temp)

print(matrix)


"""
#addition of matrixes
m1=[[1,2],[3,4]]
m2=[[5,6],[7,8]]

m0=[[0,0],[0,0]]
for i in range(2):
    for j in range(2):

        m0[i][j]=m1[i][j]+m2[i][j]


print(m0)
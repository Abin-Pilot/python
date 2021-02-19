lst1=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    x=int(input("enter the numbers:"))
    lst1.append(x)
for j in lst1:
    if j >=1:
        print(j,end="")
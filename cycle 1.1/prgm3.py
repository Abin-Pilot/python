lst1=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    x=int(input("enter the numbers:"))
    lst1.append(x)
lst2=[number**2 for number in lst1]
print("squreroot of numbers",lst2)






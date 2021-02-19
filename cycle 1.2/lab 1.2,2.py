lst=[]
n=int(input("enter the limit of the elements"))
for i in range(0,n):
    x=int(input("enter the numbers"))
    if x>100:
        lst.append('over')
    else:
        (lst.append(x))
print(lst)
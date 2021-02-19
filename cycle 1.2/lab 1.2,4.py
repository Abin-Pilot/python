lst1=[1,3,5,7]
lst2=[2,3,6,8]
x=len(lst1)
y=len(lst2)
if(x==y):
    print("length of lists are same")
else:
    print("length of lists are not same ")
a=sum(lst1)
b=sum(lst2)
if(a==b):
    print('sum of lists are same')
else:
    print('sum of lists are not same')
n=any(check in lst2 for check in lst1)
if(n==True):
    print("common value occurs in lists")
    print("common value:",set(lst2).intersection(set(lst1)))
else:
    print("common value not occured in lists")





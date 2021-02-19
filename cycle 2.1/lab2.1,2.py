n1=0
n2=1
count=0
nterms=int(input("how many times:"))
if nterms<=0:
    print("enter a posive integer")
elif nterms==1:
    print("fibonacci series upto:",nterms)
    print(n1)
else:
    print("fibonacci series:")
    while count<nterms:
       print(n1)
       nth=n1+n2
       n1=n2
       n2=nth
       count=count+1


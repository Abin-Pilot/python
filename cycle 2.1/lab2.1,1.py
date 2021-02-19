n=int(input("Enter the number:"))
fact=1
if n<0:
    print("factorial cannot be found")
elif n==0:
    print("factoral of",n,"is",fact)
else:
    for i in range(1,n+1):
        fact=fact*i
print("factorial of",n,"is",fact)
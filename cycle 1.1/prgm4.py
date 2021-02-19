lst1=[]
vowels=['a','e','i','o','u']
s=input("enter the string:")
for i in vowels:
    if(i in s):
        lst1.append(i)
print("vowels present in string",lst1)



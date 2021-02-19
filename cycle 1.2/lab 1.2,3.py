lst1=['abin','abhi','angel','chinnu','ansa']
count=0
for i in lst1:
    for j in i:
        if j=='a':
         count=count+1
print("the total no of 'a' in list is :",count)
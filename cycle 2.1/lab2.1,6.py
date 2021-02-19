dict={}
str=input("enter a string:")
for n in str:
    key=dict.keys()
    if n in key:
        dict[n]=dict[n]+1

    else:
        dict[n]=1
print('character frequency:',dict)

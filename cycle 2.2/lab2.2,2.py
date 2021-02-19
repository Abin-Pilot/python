def longest(lst1):
    max=0
    temp=lst1[0]
    for i in lst1:
        if(len(i)>max):
            max=len(i)
            temp=i
    print("the word with longest length is ",temp,"length",max)
lst1=['aby','abin','ramesh','abhinand']
longest(lst1)
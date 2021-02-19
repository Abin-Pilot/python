
def fun(str):
    if(len(str)>=3):
        if(str[-3:])=='ing':
            str=str+"ly"
        else:
            str=str+str+"ing"
    print("modified",str)
str=input("enter a string")
fun(str)
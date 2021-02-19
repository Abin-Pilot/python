def replace(str):
    first = str[0]
    modified = str[1:].replace(first,"$")
    print(first + modified)
str=input("Enter a String: ")
replace(str)
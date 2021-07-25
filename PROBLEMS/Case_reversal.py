temp=input("Enter some random input string:") 
str=""
for ch in temp:
    if ch.isalpha():
        if ch.isupper():
            str=str+ch.lower()
        else:
            str=str+ch.upper()
    elif ch.isspace():
        str=str+" "
print(len(str))
print(str)
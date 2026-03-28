"""10. Write a program to remove duplicate characters from a string."""
st = input("enter string: ")
result = ""
for ch in st:
    if ch not in result:
        result += ch
print("String after removing duplicates",result)
        

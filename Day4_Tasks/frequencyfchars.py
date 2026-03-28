"""9. Write a program to count the frequency if each character in a string"""
st = input("enter string: ")
char_count = {}
for ch in st:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1
print("Character frequencies: ")
for key in char_count:
    print(key,"-",char_count[key])

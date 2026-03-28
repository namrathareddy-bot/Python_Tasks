"""8. Write a program to check whether a string is a palindrome."""
st = input("enter string: ")
rev = ""
print(st)
for char in st.lower():
    rev = char + rev
if rev == st.lower():
    print("The string is palindrome.")
else:
    print("The string is not a palindrome.")
print(rev)

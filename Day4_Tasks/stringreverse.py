"""7. Write a program to reverse a string."""
st = input("enter string: ")
print("Using negative indexing: ")
print(st[::-1])
print("----------------------------------------\n")
rev = ""
for ch in st:
    rev = ch + rev
print("Reversed string: \n",rev)

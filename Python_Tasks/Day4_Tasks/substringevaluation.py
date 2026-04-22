"""5. Write a program to check whether a substring existss in a string."""
st = input("enter string: ")
sub_string = input("enter substring to check: ")
if sub_string.lower() in st.lower():
    print("Sub string exists!!")
else:
    print("Sorry, No sub string found.")

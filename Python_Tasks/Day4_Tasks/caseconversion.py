"""3. Write a program to convert a string to uppercase and lowercase."""
st = input("enter string: ")
print(st)
t = st.lower()
m = st.upper()
if st == t:
    print("The entered string is in lower case.")
    print("The string after conversion is: ",m)
else:
    print("The entered string is in upper case.")
    print("The string after conversion is: ",t)
    

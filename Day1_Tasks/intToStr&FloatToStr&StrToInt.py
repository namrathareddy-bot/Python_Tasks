"""4. Convert an integer to a string and print it with text.
   5. Take number as input and convert it to an integer.
   6. Convert a float to a string and print it. """

#4. Convert an integer to a string and print it with text.
n = 234
text = str(n)
print(f"The value of n is {n} and its type is: ",type(n))
print(f"The value of text is {text} and its type after casting is: ",type(text))
print("_____________________________________________________________________________\n")

#5. Take number as input and convert it to an integer.
num = input("enter: ")
val = int(num)
print("The nums type is:",type(num))
print(f"After casting the val's value is {val} and type is: ",type(val))
print("_____________________________________________________________________________\n")

#6. Convert a float to a string and print it. 
fl = 10.6
st = str(fl)
print(f"The fl value is {fl} but after type casting the value {st} but its type is:",type(st))
print("_____________________________________________________________________________\n")

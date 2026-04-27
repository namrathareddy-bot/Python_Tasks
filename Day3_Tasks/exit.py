#Write a program to check whether an element exists in a tuple
t1=(1,2,3,4,5,6,7,8,8,8,88,89,9,99)
t=int(input("ENTER A NUMBER TO SEARCH"))
if t in t1:
    print(f"{t} is present in the above Tuple")

else :
    print("NOT FOUND")   

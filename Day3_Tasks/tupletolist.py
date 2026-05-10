#Write a program to convert a tuple to a list and modify the element.
t=(12,3,44,66,7,22,33)
print("This is TUPLE",t)
print("***")
l=list(t)
print("THIS IS A LIST",l)
print("***")
print(" modifing")
l[0]=0
print("AFTER MODIFING THE LIST",l)

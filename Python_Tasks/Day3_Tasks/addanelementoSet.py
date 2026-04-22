"""2. Write a program to add an element to a set."""
elements = {10,20,30,40,50,60,70}
print("The existing set elements are: ",elements)
ele = int(input("enter element to add into set:"))
elements.add(ele)
print(elements)

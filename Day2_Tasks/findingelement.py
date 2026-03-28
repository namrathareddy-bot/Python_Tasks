"""4. Write a program that searches for a number in a list
and breaks the loop when found."""
n = int(input("enter limit: "))
li = []
for i in range(1,n+1):
    num = int(input("enter numbers: "))
    li.append(num)
print("List elements are: ",li)
element = int(input("enter element to find: "))
for ele in li:
    if element == ele:
        print("Element Found")
        break
else:
    print("Not found")

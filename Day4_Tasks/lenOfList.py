"""4. Write a program using the built in function len() to find the length
of a list."""
def length_of_list():
    n = int(input("enter list size: "))
    li = []
    for i in range(n):
        ele = int(input("enter elements to insert: "))
        li.append(ele)
    print("The list elements are: ",li)
    print("The length of the list is: ",len(li))
length_of_list()

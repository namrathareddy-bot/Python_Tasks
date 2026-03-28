"""4. Write a program to check if an element exists in a set."""
se = {12,13,14,15,16,17,4,74,34}
print("Elements in set are: ",se)
ele = int(input("enter element to check: "))
for i in se:
    if ele in se:
        print("Element Exists")
        break
else:
    print("Element Does not exist")

"""8. Write a program to remove duplicate values from a list using a set."""
duplicates_list = [10,20,30,40,50,10,20,60,70,80,100,10,20,40]
print("The duplicate list is: \n",duplicates_list)
unique_list = set(duplicates_list)
print("The unique list is: \n",unique_list)

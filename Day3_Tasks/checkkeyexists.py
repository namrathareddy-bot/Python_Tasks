"""7. Write a program to check whether a key exists in a dictionary."""
d = {"abhimanyu":20,"bhishma":30,"karna":80,"krishna":100}
print("The dictionary is: ",d)
ele = input("enter key to check: ")
for i in d:
    if ele in d:
        print("Key exists")
        break
    else:
        print("Key doest not exist")
        

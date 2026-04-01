# 3. Grocery List Manager A user wants to save grocery items in a file grocery.txt. Write a Python program that takes multiple items from the user and writes them into the file, with each item on a new line.


items=input("Enter items: ")
words=items.split()  # to split the words after each space into list

f=open("Grocery.txt","a")
for word in words:
    f.write(word + '\n')

f=open("Grocery.txt","r")
print("Items are ",'\n',f.read())
f.close()

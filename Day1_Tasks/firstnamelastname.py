"""9. Create variables for first name and last name and combine them."""
first_name = input("enter first name: ")
last_name = input("enter last name: ")
if last_name is "-":
    print("No last name so,Name of the user is:",first_name)
else:
    print("Users name is: ",first_name +"",last_name)

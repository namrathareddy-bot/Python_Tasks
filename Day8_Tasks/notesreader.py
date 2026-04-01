#2. Notes Reader Program
'''A student stores daily notes in a file called notes.txt.
Write a program that opens the file, reads all the contents,
and displays them on the screen.'''
import os
def notes_reader():
    try:
        #checks whether file exists or not.
        #If file is not found, it creates one and appends the content
        
        if not os.path.exists("notes.txt"):
            print("File does not exist!! Creating a file...")
            notes = open("notes.txt",'w')
            text = input("enter content to store in file: ")
            notes.write(text)
            print("------------------------------------------------------\n")
            print("Content added successfully")
            notes.close()

            #reads the content and displays
            notes = open("notes.txt",'r')
            print(notes.read())

            #closes the created file
            notes.close()
            
        else:
            #Opens the file and reads the content
            notes = open("notes.txt",'r')
            content = notes.readlines()

            #Prints the message and content when it reads.
            print("Successfully read the content !!")
            print("".join(content))
            notes.close()
            
    except FileNotFoundError:

        #handles if try block crashes. Displays the cause
        print("File not found!! Please check file name")
        
notes_reader()
        
    

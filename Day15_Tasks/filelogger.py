def file_logger():
    while True:
        action = input("Enter your action: ")

        try:
            # Write log to file 
            with open("file_logger.txt", "a") as f:
                f.write(action + "\n")

            print("Log added successfully")

            # Ask user to continue
            user_input = input("Do you want to continue? (Y/N): ")

            if user_input.lower() != 'y':
                break

        except Exception:
            print("Something went wrong while writing to file")

    # After loop ends
    choice = input("Do you want to view the file? (Yes/No): ")

    if choice.lower() == "yes":
        try:
            with open("file_logger.txt", "r") as f:
                data = f.read()
                print("\n--- File Content ---")
                print(data)
        except FileNotFoundError:
            print("File not found!")
    else:
        print("Okay! Logs are saved successfully.")


file_logger()
            
    

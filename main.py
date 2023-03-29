# Initialize an empty list to store tickets
tickets = []

# Loop until the user decides to exit
while True:
    # Display a menu of options for the user
    print("1. Add a ticket for QA inspection")
    print("2. View tickets for QA inspection")
    print("3. Mark a ticket as completed")
    print("4. Exit")

    # Prompt the user to select an option
    choice = input("Enter your choice: ")

    # Add a ticket for QA inspection
    if choice == '1':
        description = input("Enter description of inspection needed: ")
        tickets.append(description)
        print(f"Inspection for {description} added to the list.")

    # View tickets for QA inspection
    elif choice == '2':
        if not tickets:
            print("No inspections in the list.")
        else:
            print("Inspections needed:")
            for description in tickets:
                print(description)

    # Mark a ticket as completed
    elif choice == '3':
        description = input("Enter description of inspection to mark as completed: ")
        if description in tickets:
            tickets.remove(description)
            print(f"Inspection for {description} marked as completed.")
        else:
            print(f"Inspection for {description} not found.")

    # Exit the program
    elif choice == '4':
        break

    # Handle invalid choices
    else:
        print("Invalid choice. Please try again.")

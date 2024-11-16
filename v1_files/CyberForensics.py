import os

def display_menu():
    print("\n\n***** Menu *****")
    print("1. Run Python File 1 (FileAnalysis.py)")
    print("2. Run Python File 2 (DataEncryptionAnalysis.py)")
    print("3. Run Python File 3 (LogAnalysis.py)")
    print("4. Exit")

# execute the selected Python file
def run_python_file(file_number):
    if file_number == 1:
        os.system("py FileAnalysis.py") 
    elif file_number == 2:
        os.system("py DataEncryptionAnalysis.py")
    elif file_number == 3:
        os.system("py LogAnalysis.py")  

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 4:
            print("Exiting the program.")
            break
        elif choice in [1, 2, 3]:
            run_python_file(choice)
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("Invalid input. Please enter a number.")

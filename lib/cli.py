# lib/cli.py

# from helpers import (
#     exit_program,
#     helper_1
# )


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()

from helpers import (
    space_separator,
    print_blank_spaces,
    get_all_authors
)


# def main_menu():
#     while True:
#         space_separator()
#         print_blank_spaces(2)
#         welcome_menu()
#         print_blank_spaces(2)
#         space_separator()
#         print("1. Option 1")
#         print("2. Option 2")
#         print("0. Exit")
#         choice = input("> ")

#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             option1_menu()
#         elif choice == "2":
#             option2_menu()
#         else:
#             print("Invalid choice")


def main_menu():
    while True:
        space_separator()
        print_blank_spaces(2)
        print("               Welcome!")
        print_blank_spaces(2)
        print("Press A or a for a list of all authors")
        print_blank_spaces(2)
        print("Press B or b for a list of all books")
        print_blank_spaces(2)
        print("Press E or e to exit the program")
        print_blank_spaces(2)
        space_separator()
        choice = input("> ")

        if choice == "E" or choice == "e":
            exit_program()
        elif choice == "A" or choice == "a":
            authors_menu()
        elif choice == "B" or choice == "b":
            books_menu()
        else:
            print("Invalid choice")


def authors_menu():
    space_separator(character="><")
    print_blank_spaces(2)
    print("This is a list of all authors")
    print_blank_spaces()
    get_all_authors()
    print_blank_spaces(2)
    space_separator(character="><")
    input("Press Enter to return to the main menu...")


def books_menu():
    space_separator(character="><")
    print_blank_spaces(2)
    print("This is a list of all books")
    print_blank_spaces(2)
    space_separator()
    input("Press Enter to return to the main menu...")


# def option1_menu():
#     while True:
#         print("Option 1 Menu:")
#         print("1. Suboption 1")
#         print("2. Suboption 2")
#         print("0. Back to Main Menu")
#         choice = input("> ")

#         if choice == "0":
#             break  # Exit this submenu and return to the main menu
#         elif choice == "1":
#             # Implement the functionality for Suboption 1 here
#             print("Suboption 1 selected")
#         elif choice == "2":
#             # Implement the functionality for Suboption 2 here
#             print("Suboption 2 selected")
#         else:
#             print("Invalid choice")


# def option2_menu():
#     # Implement the menu for Option 2 here
#     print("Option 2 Menu is not implemented yet")


def exit_program():
    print("Exiting the program")
    # Add any necessary cleanup or exit code here
    exit()


def main():
    main_menu()


if __name__ == "__main__":
    main()

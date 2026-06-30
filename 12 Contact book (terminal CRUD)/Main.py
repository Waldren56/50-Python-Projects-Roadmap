import json
import sys

FILE_PATH = 'Contacts.json'

def add_contact():
    user_add_contact_name = input('Enter contact\'s name: ')
    user_add_contact_surname = input('Enter contact\'s surname: ')
    user_add_contact_phone = input('Enter contact\'s phone: +')

    data = read_json()

    info = {
        'Name': user_add_contact_name,
        'Surname': user_add_contact_surname,
        'Phone Number': user_add_contact_phone
    }

    data.append(info)

    write_json(data)

def remove_contact():
    user_remove_contact_name = input('Enter contact\'s name to remove: ')
    user_confirm_remove_contact_name = input('Are you sure you want to remove this contact? (y/n): ')

    if user_confirm_remove_contact_name.lower() == 'y':
        data = read_json()

        for contact in data:
            if contact['Name'] == user_remove_contact_name:
                data.remove(contact)
                break
        else:
            print('Contact does not exist!')

        write_json(data)

def edit_contact():
    user_edit_name = input("Enter contact's name to edit: ")
    user_edit_surname = input("Enter contact's surname: ")

    data = read_json()

    found = False

    for contact in data:
        if (
            contact["Name"] == user_edit_name
            and contact["Surname"] == user_edit_surname
        ):
            found = True

            while True:
                try:
                    user_edit_choice = int(input(
                        "Type 1 - Edit the name\n"
                        "Type 2 - Edit the surname\n"
                        "Type 3 - Edit the phone number\n"
                        ":: "
                    ))

                    if user_edit_choice in (1, 2, 3):
                        break

                    print("Enter a valid choice!")

                except ValueError:
                    print("You must insert an integer!")

            if user_edit_choice == 1:
                contact["Name"] = input("Enter the new name: ")

            elif user_edit_choice == 2:
                contact["Surname"] = input("Enter the new surname: ")

            else:
                contact["Phone Number"] = input("Enter the new phone number: +")

            write_json(data)
            print("Contact updated successfully!")
            break

    if not found:
        print("Contact does not exist!")

def show_specific_contact():
    user_show_name = input('Enter contact\'s name to show: ')
    user_show_surname = input("Enter contact's surname: ")

    data = read_json()

    for contact in data:
        if contact['Name'] == user_show_name and contact['Surname'] == user_show_surname:
            show_contact(contact=contact)

def show_all_contacts():
    data = read_json()

    for contact in data:
        show_contact(contact=contact)

def show_contact(contact):
    print(f"\t{contact['Name']} {contact['Surname']} +{contact['Phone Number']}")

def read_json():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        write_json([])
        return []

def write_json(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def print_menu():
    print('\n===       MENU | TERMINAL CRUD     ===\n'
          '=== Type 1 - Add a new contact     ===\n'
          '=== Type 2 - Remove a contact      ===\n'
          '=== Type 3 - Edit a contact        ===\n'
          '=== Type 4 - Search a contact      ===\n'
          '=== Type 5 - Search all contacts   ===\n'
          '=== Type 6 - Quit                  ===\n')

def main():
    while True:
        print_menu()

        while True:
            try:
                user_menu = int(input('Enter your choice: '))
                if user_menu in (1, 2, 3, 4, 5, 6):
                    break
                else:
                    print('Invalid choice. Please try again.')
            except ValueError:
                print('Please enter a number!')

        if user_menu == 1:
            add_contact()
        elif user_menu == 2:
            remove_contact()
        elif user_menu == 3:
            edit_contact()
        elif user_menu == 4:
            show_specific_contact()
        elif user_menu == 5:
            show_all_contacts()
        else:
            sys.exit('Program exited successfully with code 0')


if __name__ == "__main__":
    main()
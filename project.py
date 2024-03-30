#add, edit, delete, search for contacts with python dictionary, file handling, user interaction, error handling


# info = {phone/email: {name, phone, email, additional info}, ...}
contact_info = {
    123: 
        {"name": "John Doe", 
        "phone": 123, 
        "email": "johndoe@email.com", 
        "additional info": "I like cats"},
    234:
        {"name": "Jane Smith", 
         "phone": 234, 
         "email": "janesmith@email.com", 
         "additional info": "I like dogs"}
    }
    
import re

# valid email
def valid_email(email):
    pattern = r'[A-Za-z0-9_%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    if re.match(pattern, email):
        return True
    else:
        return False


# Add new contact with details
def add_contact():
    try:
        input_name = input("Enter name: ")
        input_phone = int(input("Enter phone number: "))
        input_email = input("Enter email: ")
        input_additional_info = input("Enter additional info: ")
    except ValueError:
        print("Please enter a valid phone number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Checking if email is valid
    if not valid_email(input_email):
        print("Please enter a valid email address.\n")
        return
    # Add contact
    contact_info[input_phone] = {"name": input_name, "phone": input_phone, "email": input_email, "additional info": input_additional_info}
    print("Contact added successfully!")


# Edit existing contacts information
def edit_contact():
    try:
        input_name = input("Enter name: ")
        input_phone = int(input("Enter phone number: "))
        input_email = input("Enter email: ")
        input_additional_info = input("Enter additional info: ")
    except ValueError:
        print("Please enter a valid phone number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Checking if email is valid
    if not valid_email(input_email):
        print("Please enter a valid email address.\n")
        return
    # Update contact
    contact_info.update({input_phone: {"name": input_name, "phone": input_phone, "email": input_email, "additional info": input_additional_info}})
    print("Contact updated successfully!")

    
# Delete a contact by phone number
def delete_contact():
    display_all_contacts()
    # input phone number to delete
    try:
        phone = int(input("Enter phone number to delete: "))
    except ValueError:
        print("Please enter a valid phone number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # delete contact
    if contact_info.pop(phone, None) is None:
        print("Contact not found.")
        return
    print("Contact deleted successfully!\n")


# Search for a contact by phone number and display details 
def search_contact():
    try:
        phone = int(input("Enter phone number to search: "))
    except ValueError:
        print("Please enter a valid phone number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # Search for contact by phone number
    contact = contact_info.get(phone, None)
    if contact is None:
        print("Contact not found.")
        return  
    print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAdditional Info: {contact['additional info']}\n")
    
    
# Display all contacts 
def display_all_contacts():
    for phone, contact in contact_info.items():
        print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAdditional Info: {contact['additional info']}\n")
    
    
# Export contacts to a text file in a structured format
def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for phone, contact in contact_info.items():
                file.write(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAdditional Info: {contact['additional info']}\n\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("Contacts exported successfully!\n")
    
    
def menu_action():
    print()
    print("welcome to the Contact Management System!")
    print("Menu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit\n")

    while True:    
        input_option = input("Enter option: ")
        print()

        if input_option == "1":
            add_contact()
        elif input_option == "2":
            edit_contact()
        elif input_option == "3":
            delete_contact()
        elif input_option == "4":
            search_contact()
        elif input_option == "5":
            display_all_contacts()
        elif input_option == "6":
            export_contacts()
        elif input_option == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            continue
        
    
menu_action()
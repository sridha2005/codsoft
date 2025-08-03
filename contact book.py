contacts = []
def add_contact():
    name = input("Enter Name:")
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")
    address = input("Enter Address:")
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print(f"\ncontact for {name} added successfully.\n")
def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\nContact List:")
    print("_" * 50)
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, phone: {contact['phone']}")
    print("_" * 50)
def search_contact():
    serach_term = input("Enter name or phone number to search:")
    found = False
    print("\nSearch Results:")
    print("_" * 50)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("\nEnter new details (leave blank to keep existing value):")
            new_phone = input(f"Phone ({contact['phone']}):") or contact['phone']
            new_email = input(f"Email ({contact['email']}):") or contact['email']
            new_address = input(f"Address ({contact['address']}):") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            print(f"\ncontact for {name} updated successfully.\n")
            return
        print("Contact not found.\n")
def delete_contact():
    name = input("Enter the name of the contact to delete:")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"\ncontact for {name} deleted successfully.\n")
            return
    print("Contact not found.\n")
def menu():
    print("\n===== Contact Manangement System =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
while True:
    menu()
    choice = input("Select an option (1-6):")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("\nExisting Contact Management System. Goodbye!\n")
        break
    else:
        print("\nInvalid option! please choose between 1-6.\n")
    

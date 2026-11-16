# Unit 5 Practical task 
#A Contact book that stores contacts as lists in dictionaries
#Allows users to add, search, view and delete contacts 

#Contacts dictionary list

contacts = [
    #{'name': 'Buhle', 'number': 123, 'email':'bnakupi@icloud.com'},
    #{'name': 'Thato', 'number': 234, 'email': 'trakoti@gmail.com'},
    #{'name': 'Qhama', 'number': 345, 'email': 'qmatyobeni@gmail.com'}
]

#Adding to dictionary function 
def add_student(contact_list, name, number, email):
    new_contact = {
        'name' : name,
        'number': number,
        'email': email,
        'contact_list': contact_list
    }

    contact_list.append(new_contact)
    print(f'Added {name} to the list')


# Search contacts

def search_contact(contact_list, name):

    for contacts in contact_list:
        if contacts ['name'] == name: 
            return contacts 
        return None

# Delete Contact

def delete_contact (contact_list, name):
    for contacts in contact_list:
        if contacts['name'] == name:
            contact_list.remove(contacts)
            print(f'Deleted {name} from contact list') 
            return
        print(f'No contact with name: {name}')

# View contact list

def view_contacts (contact_list):
    if not contact_list:
        print('No Contacts.')
        return
    for contacts in  contact_list:
        print(f'Name: {contacts['name']} | Number: {contacts['number']} | Email: {contacts['email']}')

# user menu 

def menu():
    while True:
        print('\n==== Contact Menu ====')
        print('1. Add Contact')
        print('2. Search for Contact')
        print('3. Delete contact')
        print('4. View Contacts')
        print('5. Exit')

        choice = input("Enter your choice (1-5): ")

        if choice =='1':
            name = str(input('Enter a name: '))
            number = int(input('Enter a contact number: '))
            email = str(input('Enter contact email: '))
            add_student(contacts, name, number, email)

        elif choice == '2':
            name = str(input("Enter Contact name: "))
            result = search_contact(contacts, name)
            if result : 
                print(f'Contact: {result['name']}, Number: {result['number']}, Email: {result['email']}')

            else: 
                print('Contact not found.')

        elif choice == '3':
            name = str(input('Enter Contact name: '))
            delete_contact(contacts, name)

        elif choice == '4':
            view_contacts(contacts)

        elif choice == '5':
            print('Thank you and Goodbye.')
            break

        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

menu()
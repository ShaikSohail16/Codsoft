class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
        else:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone} - {contact.email}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted!")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact found: {contact.name} - {contact.phone} - {contact.email}")
                return
        print(f"Contact '{name}' not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add contact")
        print("2. View contacts")
        print("3. Delete contact")
        print("4. Search contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "4":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
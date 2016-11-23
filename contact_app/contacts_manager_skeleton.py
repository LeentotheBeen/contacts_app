from contact import *

"""
Contacts Manager
This module manages the contacts list which holds instances of the Contact class.
You can view, add, edit, and delete contacts.
Bonus: write contacts to text file and read contacts in from a text file.
"""
contacts_list = [Contact("Eileen", "Hays-Schwantes", "8471295408")]



def add_new_contact(first_name, last_name, mobile_phone):
    contact_new = Contact(first_name, last_name)
    contact_new.mobile_phone = mobile_phone
    contacts_list.append(contact_new)
    return contacts_list

    # handle cases and whitespace for name parameters
    # handle if contact_list is empty
    # iterate contact_list, check if contact already exists, print error
    # instantiate instance of Contact
    # add to contacts_list


def edit_existing_contact(first_name, last_name):
    for contact in contacts_list:
        if first_name.lower() == contact.first_name:
            #tell it to change things 
        elif last_name.lower() == contact.last_name:
            #tell it to change things
        else: 
            print "This is not in your contact list."

def delete_contact():
    pass


def current_contact_list():
    # todo: return a sorted list of objects from contacts_list
    pass


def write_contacts_to_file():
    pass


def read_contacts_from_file():
    pass


def main():
    # test add new contact
    print add_new_contact('Jess','Donald','4156377790') 
    print contacts_list[0].__dict__ 


    # test edit contact
    # test delete contact
    # test show all contacts



if __name__ == '__main__':
    main()



"""
This file is a textual UI layer on top of the contacts manager.
It will allow a user to view, add, edit, and delete contacts.
"""

import contacts_manager_skeleton 


def display_menu():
    pass


def display_contacts():
    pass


def main():
    first_name = "Jess"
    last_name = "Donald"
    contacts_manager_skeleton.add_new_contact(first_name, last_name)


if __name__ == '__main__':
    main()
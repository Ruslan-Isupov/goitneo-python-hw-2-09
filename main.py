# HW 2
# Task 1


from collections import UserDict
import re


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Doesn't exist."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    (name,) = args
    if name in contacts.keys():
        return contacts.get(name)
    else:
        raise KeyError


@input_error
def show_all(contacts):
    info_contacts = ""
    for name, phone in contacts.items():
        info_contacts += f"{name}:{phone}\n"
    if info_contacts:
        return info_contacts.strip()
    else:
        return "We don't have any contacts"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()


# Task 2


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, phone):
        super().__init__(phone)

    def get_validate_phone(self, phone):

        number = re.search("[0-9]{10}$", phone)
        if number and len(phone) == 10:

            return number.group()
        else:
            return "Phone isn't valid"


class Record:

    def __init__(self, name):

        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone.get_validate_phone(self, phone)

        self.phones.append(phone)

    def edit_phone(self, phone, new_phone):

        new_phone = Phone.get_validate_phone(self, new_phone)
        if phone in self.phones:

            self.phones = list(map(lambda x: x.replace(phone, new_phone), self.phones))
        else:
            return "Phone doesn't exist"

    def remove_phone(self, phone):

        if phone in self.phones:
            self.phones.remove(phone)

        else:
            return "Phone doesn't exist"

    def find_phone(self, phone):
        if phone in self.phones:
            return phone
        else:
            return "Phone doesn't exist"

    def __str__(self):

        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"


class AddressBook(UserDict):

    def add_record(self, record):

        self.data[record.name.value] = record

    def find(self, name):

        if self.data.get(name):

            return self.data.get(name)
        else:
            return "Name doesn't exist"

    def delete(self, name):

        if self.data.get(name):

            self.data.pop(name)

        else:
            return "Name doesn't exist"

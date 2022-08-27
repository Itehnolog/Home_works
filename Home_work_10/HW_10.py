from collections import UserDict


class AddressBook(UserDict):
    def add_contact(self, name, phone):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phones = [phone] if phone is not None else[]

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def change_phone(self, old_number, new_number):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            return f"{old_number} does not exist"

    def delete_phone(self, phone):
        self.phone.remove(phone)

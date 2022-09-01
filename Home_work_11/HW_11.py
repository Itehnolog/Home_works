from collections import UserDict
import datetime


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.n = None

    def add_contact(self, name, phone):
        contact = Record(name=name, phone=phone)
        self.data[name.value] = contact

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_by_name(self, name):
        try:
            return self.data[name]
        except KeyError:
            return None

    def find_by_phone(self, phone: str):
        for record in self.data.values():
            if phone in [number.value for number in record.phones]:
                return record
        return None

    def iterator(self, n=2, days=0):
        self.n = n
        index = 1
        print_block = '-' * 50 + '\n'
        for record in self.data.values():
            if days == 0 or (record.birthday.value is not None and record.days_to_birthday(record.birthday) <= days):
                print_block += str(record) + '\n'
                if index < n:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block


class Field:
    def __init__(self, value):
        self.value = value
        self._value = None

    def __repr__(self) -> str:
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Birthday(Field):

    def __init__(self, value) -> None:
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value) -> None:
        if value:
            try:
                datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Incorrect data format, should be DD.MM.YYYY")
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self._value = None
        self.value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, value) -> None:
        value = (
            value.strip()
            .removeprefix("+")
            .replace("-", "")
            .replace(" ", "")
            .replace("(", "")
            .replace(")", "")
        )
        self._value = value


class Record:
    def __init__(self, name, phone=None, birthday=None) -> None:
        self.name = name
        self.phones = [phone] if phone is not None else[]
        self.birthday = birthday

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def change_phone(self, old_number, new_number):
        try:
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            return f"{old_number} does not exist"

    def days_to_birthday(self):
        if self.birthday:
            start = datetime.date.today()
            birthday_date = datetime.strptime(str(self.birthday), '%d.%m.%Y')
            end = datetime.date(
                start.year, birthday_date.month, birthday_date.day)
            count_days = (end - start).days
            if count_days < 0:
                count_days += 365
            return count_days
        else:
            return 'Unknown birthday'

    def delete_phone(self, phone):
        self.phone.remove(phone)

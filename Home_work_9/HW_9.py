import sys

contact_book = {}


def input_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
        except Exception:
            raise SystemExit("Good bye!")
    return wrapper


@input_handler
def add_contact(user_list):
    if contact_book.get(user_list[0]) is not None:
        return "Number is exist"
    else:
        contact_book[user_list[0]] = user_list[1]
        return "Contact's added"


@input_handler
def change_contact(user_list):
    if contact_book.get(user_list[0]) is not None:
        contact_book[user_list[0]] = user_list[1]
        return "Number is changed!"
    else:
        raise KeyError("Contact does not exist")


@input_handler
def get_phone(user_list):
    number = contact_book.get(user_list[0])
    if number is not None:
        return f"User number is {number}"
    else:
        raise ValueError("User does not exist!")


@input_handler
def parse_command(command):
    commands = command.split(" ")
    normalized_command = command.lower().lstrip()
    for cmd in contact_commands.keys():
        if normalized_command.startswith(cmd):
            result = contact_commands.get(cmd)
            return result, commands[1:]
    raise ValueError("Unknown command!")


@input_handler
def say_hello(*args):
    return "How can I help you?"


@input_handler
def say_good_bye(*args):
    raise SystemExit("Good bye!")


@input_handler
def show_all_contacts(*args):
    print("CONTACT BOOK")
    if len(contact_book) > 0:
        for username, phone in contact_book.items():
            return (f"{username} number {phone}")
    else:
        return "Contact book is empty!"


contact_commands = {"hello": say_hello,
                    "add": add_contact,
                    "change": change_contact,
                    "phone": get_phone,
                    "close": say_good_bye,
                    "exit": say_good_bye,
                    "show all": show_all_contacts,
                    "good bye": say_good_bye
                    }


@input_handler
def main():
    while True:
        command = input("Please input command:")
        result = parse_command(command)
        if len(result) != 2:
            print(result)
            continue
        print(result[0](result[1]))


if __name__ == "__main__":
    main()

contacts = dict()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        return "Name not found!"
    else:
        contacts[name] = phone
        return "Contact updated."


def show_phone(arg, contacts):
    name = arg
    if name not in contacts.keys():
        return "Name not found!"
    else:
        return contacts[name]


def show_all(contacts):
    return [f"name: {name}, phone: {phone}" for name, phone in contacts.items()]


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
            print(show_phone(args[0], contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def write_contact(args, contacts, is_change = False):
    if len(args) != 2:
        return f"Bad arguments {args}."
    name, phone = args
    
    if (name in contacts.keys() and not is_change):
        return f"{name} exists."
    elif (name not in contacts.keys() and is_change):
        return f"{name} is not in phonebook."
    
    contacts[name] = phone
    return f"Contact {name} {'changed' if is_change else 'added'}."

def get_phone(args, contacts):
    name = args[0]
    if name not in contacts.keys():
        return f"{name} not found."
    return f"{contacts[name]}"

def print_phonebook(contacts):
    return '\n'.join(['{} {}'.format(k, v) for k,v in contacts.items()])

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
            print(write_contact(args, contacts))
        elif command == "change":
            print(write_contact(args, contacts, True))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(print_phonebook(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
from collections import UserDict

class DefaultExecutionDict(UserDict):
    def __getitem__(self, key):
        if not key in self.data.keys():
            return DEFAULT_METHOD
        else:
            return self.data.get(key)
        

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def write_contact(contacts, args, is_change = False, *_):
    if len(args) != 2:
        return f"Bad arguments {args}."
    name, phone = args
    
    if (name in contacts.keys() and not is_change):
        return f"{name} exists."
    elif (name not in contacts.keys() and is_change):
        return f"{name} is not in phonebook."
    
    contacts[name] = phone
    return f"Contact {name} {'changed' if is_change else 'added'}."


def write_contact_add(contacts, args, *_):
    return write_contact(contacts, args, False)
    
    
def write_contact_change(contacts, args, *_):
    return write_contact(contacts, args, True)
    
    
    
def get_phone(contacts, args, *_):
    name = args[0]
    if name not in contacts.keys():
        return f"{name} not found."
    return f"{contacts[name]}"


def print_phonebook(contacts, *_):
    return '\n'.join(['{} {}'.format(k, v) for k,v in contacts.items()])


def print_goodbye(*_):
    return "Good bye!"


def print_hello(*_):
    return "How can I help you?"


def print_bad(*_):
    return "Invalid command."


OPERATIONS = DefaultExecutionDict({
    "close": print_goodbye,
    "exit": print_goodbye,
    "hello": print_hello,
    "add": write_contact_add,
    "change": write_contact_change,
    "phone": get_phone,
    "all": print_phonebook,
})

DEFAULT_METHOD = print_bad


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        print(OPERATIONS[command](contacts, args, True if command == "change" else False))
        if command in ["close", "exit"]:
            break
        
if __name__ == "__main__":
    main()
    
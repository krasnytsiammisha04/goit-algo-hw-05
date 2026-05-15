def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except TypeError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner






def parse_input(user_input):
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: Give me name and phone please."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        return "Error: Enter user name."
    name = args[0]
    if name in contacts:
       return contacts[name]
    else:
        return f"Error: Contact '{name}' not found."

def show_all(contacts):
   if not contacts:
       return "No contacts saved."

   result = []
   for name, phone in contacts.items():
       result.append(f"{name}: {phone}")
   return "\n".join(result)



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Доступні команди:")
    print("  - add [ім'я] [номер]     (Додати новий контакт)")
    print("  - change [ім'я] [номер]  (Змінити існуючий номер)")
    print("  - phone [ім'я]           (Показати номер за ім'ям)")
    print("  - all                    (Показати всі контакти)")
    print("  - hello / exit / close")
    print("-" * 30)
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

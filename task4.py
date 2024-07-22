
# Функція розбирає введення користувача на команду та аргументи.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):  # Декоратор для обробки помилок введення користувача.
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Not enough arguments, try again: add (name, phone) or phone (name)"
        except IndexError:
            return "Not enough arguments, try again: add (name, phone) or phone (name)"
        except KeyError:
            return "Contact not found"
    return inner


@input_error
def add_contact(args, contacts):  # Додає новий контакт до списку контактів.
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        return "This contact already exists."
    contacts[name] = phone
    return "Contact added."


@input_error
# Змінює існуючий контакт у списку контактів.
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def get_phone(args, contacts):  # Отримує номер телефону за ім'ям контакту.
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]


@input_error
def list_contacts(args, contacts):  # Повертає список всіх контактів.
    if args:
        raise ValueError
    if not contacts:
        return 'Contacts are empty.'
    result = ''
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result.strip()


def main():  # Головна функція для запуску бота-помічника.
    contacts = {}
    print('Welcome! Available commands: add (name, phone), phone (name), change (name, phone) all, exit')

    while True:
        user_input = input('Enter a command: ')
        command, args = parse_input(user_input)

        if command == 'exit':
            print('Good bye!')
            break

        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_phone(args, contacts))
        elif command == 'all':
            print(list_contacts(args, contacts))
        else:
            print(
                'Invalid command. Available commands: add (name, phone), change (name, phone), phone (name), all, exit.')


if __name__ == '__main__':
    main()

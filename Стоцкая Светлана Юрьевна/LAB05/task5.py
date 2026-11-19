import argparse
import random
import string

MIN_PASSWORD = 8
MAX_PASSWORD = 64

def generate_password(length, pass_count, digit, special_symbols):
    """
    Генерирует набор паролей для пользователя.
    :param length: Длина пароля.
    :param pass_count: Количество паролей.
    :param digit: Параметр, запрещающий цифры в пароле.
    :param special_symbols: Параметр, запрещающий специальные символы в пароле.
    :return: Список сгенерированных паролей.
    """
    passwords = []
    for i in range(pass_count):
        if digit:
            if special_symbols:
                symbols = string.ascii_letters
            else:
                symbols = string.ascii_letters + string.punctuation
        else:
            if special_symbols:
                symbols = string.ascii_letters + string.digits
            else:
                symbols = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(symbols, length))
        passwords.append(password)
    return passwords

def save_passwords(pass_list, output_file, save_file):
    """
    Сохраняет список паролей в файл.
    :param pass_list: Список паролей.
    :param output_file: Путь к файлу для записи.
    :param save_file: Флаг сохранения в файл.
    :return: None
    """
    if save_file:
        with open(output_file, "w") as file:
            for password in pass_list:
                file.write(password + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = "password_generator", description = "Программа для генерации паролей", epilog = "Все пароли сгенерированы!")
    parser.add_argument("length", type = int, help = "Длина пароля")
    parser.add_argument("pass_count", type = int, help = "Количество создаваемых паролей")
    parser.add_argument("-d", "--digit", help = "Флаг исключения цифр из пароля")
    parser.add_argument("-s", "--special_symbols", help = "Флаг исключения специальных символов из пароля")
    parser.add_argument("-f", "--file", default = None, type = str, help = "Запись паролей в файл")
    args = parser.parse_args()
    if args.length < MIN_PASSWORD or args.length > MAX_PASSWORD:
        raise argparse.ArgumentError(args.length, "Пароль должен быть другой длины!")
    else:
        passes = generate_password(args.length, args.pass_count, args.digit, args.special_symbols)
    if args.file:
        save_passwords(passes, args.file, args.file)

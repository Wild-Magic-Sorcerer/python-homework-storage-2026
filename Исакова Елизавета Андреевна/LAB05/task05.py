import argparse #для работы с аргументами командной строки
import random #для случайных символов
import string #модуль в котором уже готовы наборы символов, чтоб не прописывать их вручную
import os #для проверки существования файла

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Генератор паролей') #создаем парсер с описанием

    parser.add_argument('length', type=int, help='Длина пароля (от 8 до 64)')
    parser.add_argument('count', type=int, help='Количество паролей')
    parser.add_argument('--no-number', action='store_true', help='Исключить цифры') #если написать то парль будет без цифр
    parser.add_argument('--no-special', action='store_true', help='Исключить спецсимволы') #то пароль без специальных символов
    parser.add_argument('--output', help='Файл для сохранения паролей') #если пользователь напишет --output то пароль мы сохраним в файл, если нет то просто выведем в терминал

    args = parser.parse_args() #превращаем писанину пользователя в удобный объект аргс (парсинг)

    if args.length > 64 or args.length < 8:
        parser.error('Длина пароля должна быть от 8 до 64!')

    symbols = string.ascii_letters #кладем сюда все буквы английского алфавита, это базовый набор, который всегда будет в пароле

    if not args.no_number: #если пользователь не написал флаг нонамберс, то добавляем цифры 0-9
        symbols += string.digits

    if not args.no_special: #то же самое только со спец символами
        symbols += string.punctuation

    if len(symbols) == 0:
        parser.error('Нельзя сгенерировать пароль!')

    passwords = []
    for _ in range(args.count): #цикл, который повторяется столько раз, сколько паролей запросит пользователь
        password = ''.join(random.choice(symbols) for _ in range(args.length)) #сама генерация пароля
        passwords.append(password)

    if args.output: #проверяем написал ли пользователь --output, если да, то сохраняем в файл
        if os.path.exists(args.output): #если этот файл уже сущ, то это защита от перезаписи
            parser.error(f'Файл "{args.output}" уже существует!')

        with open(args.output, 'w', encoding='utf-8') as f: #открываем файл для записи паролей с новой строчки
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f'Пароли записаны в "{args.output}"')
    else:
        for pwd in passwords: #если файл не указан то мы просто записываем пароли в терминал
            print(pwd)

import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Утилита для копирования и обработки файлов')
    parser.add_argument('--input', required=True, help='Входной файл') #-- чтобы можно было писать в любом порядке и не было ошибки
    parser.add_argument('--output', required=True, help='Выходной файл') #тру потому что инпут и аутпут на самом деле обязательны, хоть и с --, если пользователь не напишет их то будет ошибка
    parser.add_argument('--replace', help='Замена в формате OLD=NEW')
    parser.add_argument('--append-footer', help='Строка для добавления в конец')
    parser.add_argument('--rewrite', action='store_true', help='Разрешить перезапись выходного файла') #стортру это просто переключатель, если я напишу в терминале --реврайт, то файл перезапишется, если не напишу - нет

    args = parser.parse_args() #парсинг - разбиение на составние части
#проверка безопасности, если пользователь захочет перезаписать файл, то надо проверить что он сущ и что перезапись возможна
    if not os.path.exists(args.input): #если файл такой-то такой не существует:
        parser.error(f'Входной файл "{args.input}" не найден!') #код ошибки 2
    if os.path.exists(args.output) and not args.rewrite: #если выходной файл сущ и пользователь не разрешил перезапись (не написал в терминаое --rewrite)
        parser.error(f'Файл "{args.output}" уже существует!') #защита от случайной перезаписи существующих файлов

    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read() #открываем файл для чтения, раскодировка ютф8 чтоб не было каракулей

    count_replace = 0 #счетчик перестановок
    if args.replace: #если пользователь написал --replace
        old, new = args.replace.split('=', 1) #разрезает строку по первому = (поэтому 1, если бы я написала а=б=в, то программа бы сломалась, то что до первого = становится old, после - new)
        count_replace = content.count(old) #считаем сколько раз слово олд встречается в файле до того как мы его заменили
        content = content.replace(old, new) #меняем и записываем в контент (содержимое)

    if args.append_footer: #проверяем написал ли пользователь флаг --append-footer
        content += '\n' + args.append_footer #с новой строки записываем строчку которую укажет пользователь

    with open(args.output, 'w', encoding='utf-8') as f: #открываем выходной файл для записи
        f.write(content) #записываем в файл

    print(f'Выполнено замен: {count_replace}')
    print(f'Результат сохранён в "{args.output}"')

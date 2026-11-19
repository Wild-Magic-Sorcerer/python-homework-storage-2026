import argparse
def copy_file(input_file, output_file, replace_string, footer, rewrite):
    """
    Копирует содержимое одного файла в другой файл с небольшими изменениями.
    :param input_file: Путь до читаемого файла.
    :param output_file: Путь до файла, в который записывается результат.
    :param replace_string: Аргумент замены одной подстроки на другую.
    :param footer: Добавляемая в конец строка.
    :param rewrite: Флаг перезаписи файла.
    :return: Количество заменённых подстрок в файле.
    """
    try:
        with open(input_file, "r") as file_1:
            content = file_1.read()
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден, выберите существующий!")
    re_count = 0
    if replace_string:
        if "=" in replace_string:
            old_and_new = replace_string.split("=")
        else:
            raise ValueError("Строка replace должна быть в формате OLD=NEW")
        re_count = content.count(old_and_new[0])
        result = content.replace(old_and_new[0], old_and_new[1])
    else:
        result = content
    if rewrite == "no":
        with open(output_file, "a") as file_2:
            file_2.write(result)
            if footer:
                file_2.write(footer)
    else:
            with open(output_file, "w") as file_2:
                if footer:
                    file_2.write(result + "\n" + footer)
                else:
                    file_2.write(result)
    return re_count

if "__main__" == __name__:
    parser = argparse.ArgumentParser(prog = "copy_file", description = "Скрипт, переносящий содержимое одного файла в другой с небольшими изменениями.", epilog = "Все флаги учтены.")
    parser.add_argument("-i", "--input", type = str, help = "Путь до читаемого файла")
    parser.add_argument("-o", "--output", type = str, help = "Путь до файла для записи")
    parser.add_argument("-r", "--replace", type = str, help = "Строка замены одной подстроки на другую в формате OLD=NEW")
    parser.add_argument("-a", "--append-footer", type = str, default = None, help = "Строка для добавления в конец файла")
    parser.add_argument("-w", "--writing", type = str, default = "no", choices = ["yes", "no"], help = "Аргумент для перезаписи файла вместо записи в конец")
    args = parser.parse_args()
    number = copy_file(args.input, args.output, args.replace, args.append_footer, args.writing)
    if number != 0:
        print(f"Выполнено {number} замен.")

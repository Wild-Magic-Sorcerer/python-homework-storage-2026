if __name__ == "__main__":
    str_list= input("Введите несколько строк через запятую\n").split(",")
    list_total_length = 0 #суммарная длина всех строк
    for st in str_list:
        list_total_length += len(st)
    list_el_lenght = len(str_list) #количество строк
    average_length = list_total_length / list_el_lenght #средняя длина
    result = []
    for st in  str_list:
        if len(st) > average_length:
            result.append(st)

    print(f"Список строк, длиннее среднего значения {average_length} :\n{result}")


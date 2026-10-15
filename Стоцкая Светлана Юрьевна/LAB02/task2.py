def increase(number_seq):
    for value in range(len(number_seq)):
        number_seq[value] = int(number_seq[value])
    decrease = input("Если хотите сортировку в порядке возрастания, введите 1,"
                     "если в порядке убывания, введите 0 ")
    if decrease == "1":
        number_seq.sort()
        return number_seq
    elif decrease == "0":
        number_seq.sort()
        number_seq.reverse()
        return number_seq
    else:
        return "Вы ввели неподходящее значение!"


if __name__ == '__main__':
    numb_list = input("Введите набор чисел, разделённых пробелами ").split()
    print(increase(numb_list))

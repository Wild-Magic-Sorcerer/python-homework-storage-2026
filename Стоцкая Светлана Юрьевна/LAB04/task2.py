class BankAccount:
    """
    Класс для банковского счёта.
    """
    def __init__(self, owner, balance, history):
        """
        Метод-конструктор класса BankAccount.
        :param owner: Владелец банковского счёта.
        :param balance: Баланс на счету.
        :param history: История транзакций банковского счёта.
        :return: None
        """
        self._owner = owner
        self._balance = balance
        self._history = history

    @property
    def owner(self):
        """
        Метод, возвращающий имя владельца счёта.
        :return: Имя владельца счёта.
        """
        return self._owner

    @property
    def balance(self):
        """
        Метод, возвращающий баланс на счету.
        :return: Баланс на счету.
        """
        return self._balance

    def profit(self, number):
        """
        Метод, позволяющий добавить деньги на счёт.
        :param number: Число денег, добавляемых на счёт.
        :return: None
        """
        if number > 0:
            self._balance += number
            self._history.append(f"Было получено {number} рублей!")
        else:
            raise ValueError("Пополнение денег может быть только на положительную сумму!")

    def decrease(self, number):
        """
        Метод, позволяющий снять деньги со счёта.
        :param number: Число денег, снимаемых со счёта.
        :return: None
        """
        if number > 0:
            if number < self._balance:
                self._balance -= number
                self._history.append(f"Было успешно снято {number} рублей!")
            else:
                raise ValueError("Недостаточно денег на счёте для снятия такой суммы!")
        else:
            raise ValueError("Снятие денег может быть только на положительную сумму!")

    def get_history(self):
        """
        Метод, возвращающий копию истории транзакций.
        :return: Копия истории транзакций.
        """
        return self._history.copy()

    @classmethod
    def create(cls, some_dict):
        """
        Классовый метод, создающий объект из словаря.
        :param some_dict: Словарь, описывающий объект, который должен быть создан.
        :return: Новый объект класса BankAccount.
        """
        owner = some_dict.get("owner", 0)
        balance = some_dict.get("balance", 0)
        history = some_dict.get("history", [])
        return cls(owner, balance, history)

class SavingsAccount(BankAccount):
    """
    Класс для сберегательного счёта. Наследует характеристики класса BankAccount.
    """
    def __init__(self, owner, balance, history, percent):
        """
        Метод-конструктор класса SavingsAccount.
        :param owner: Владелец сберегательного счёта.
        :param balance: Баланс на счету.
        :param history: История транзакций сберегательного счёта.
        :param percent: Процент, начисляемый на имеющуюся сумму денег.
        :return: None
        """
        super().__init__(owner, balance, history)
        self._percent = percent

    def get_percent(self):
        """
        Метод, начисляющий проценты на текущий баланс.
        :return: None
        :raises ValueError: Если процент меньше или равен 0.
        """
        if self._percent > 0:
            self._balance = self._balance * (100 - self._percent) / 100
        else:
            raise ValueError("Мы тратим деньги, процент должен быть больше 0!")

    def decrease(self, number):
        """
        Метод, позволяющий снять деньги со счёта, но не более 50% баланса.
        :param number: Число денег, снимаемых со счёта.
        :return: None
        """
        if number > 0:
            if number * 2 > self._balance:
                raise ValueError("Нельзя снять больше половины денег со счёта!")
            else:
                self._balance -= number
        else:
            raise ValueError("Снятие денег может быть только на положительную сумму!")


if __name__ == '__main__':
    my_acc = BankAccount.create({"owner":"Sveta", "balance":12000})
    my_acc.profit(550)
    my_acc.decrease(3000)
    print("Баланс после проведения операций:", my_acc.balance)
    try:
        my_acc.profit(-10)
    except ValueError:
        print("Нельзя отрицательное значение вводить!")
    try:
        my_acc.decrease(15000)
    except ValueError:
        print("На балансе денег недостаточно!")
    print("История операций:", my_acc.get_history())
    try:
        my_acc.balance = 0
    except AttributeError:
        print("Новый баланс так просто не установить!")
    second_acc = SavingsAccount("Someone", 7000, [], 8)
    print("Снятие денег с разных счетов:")
    my_acc.decrease(500)
    print("На обычном счету всё прошло нормально.")
    try:
        second_acc.decrease(4000)
    except ValueError:
        print("Нельзя так много снимать с этого счёта!")

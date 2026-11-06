#!/usr/bin/env python3


PERCENT_NUMBER = 0.5


class BankAccount:
    """
    Родительский класс для создания банковского счета и выполнения денежных операций.
    """
    def __init__(self, cardholder, balance):
        """
        Базовый конструктор класса BankAccount.

        :param cardholder: Владелец банковского счета.

        :param balance: Начальный баланс счета.
        """
        if self.check_string(cardholder):
            self._cardholder = cardholder
        else:
            raise ValueError('Кто ты, воин?')

        if self.check_value(balance) and balance >= 0:
            self._balance = balance
        else:
            raise ValueError('Баланс должен быть равен ХОТЯ БЫ 0..')

        self._history = []


    @staticmethod
    def check_value(value):
        """
        Метод для проверки числового значения.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) in (int, float)


    @staticmethod
    def check_string(value):
        """
        Метод для проверки строкового значения.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) == str and bool(value.strip())


    @property
    def cardholder(self):
        """
        Метод, который позволяет прочитать имя владельца счета.

        :return: Владелец банковского счета.
        """
        return self._cardholder


    @property
    def balance(self):
        """
        Метод, который позволяет прочитать баланс счета.

        :return: Текущий баланс счета.
        """
        return self._balance


    @staticmethod
    def validate_amount(amount):
        """
        Метод для проверки суммы денежной операции.

        :param amount: Сумма операции.

        :raises ValueError: Если сумма имеет неверный тип
            или меньше либо равна 0.
        """
        if type(amount) not in (int, float) or amount <= 0:
            raise ValueError('Сумма операции должна быть положительным числом')


    def top_up(self, amount):
        """
        Метод для пополнения банковского счета.

        :param amount: Сумма пополнения.

        :return: Новый баланс счета.
        """
        self.validate_amount(amount)
        self._balance += amount
        self._history.append(f'Денежка пополняется на: +{amount}')

        return self._balance


    def spend(self, amount):
        """
        Метод для снятия денежки с банковского счета.

        :param amount: Сумма снятия.

        :return: Новый баланс счета.

        :raises ValueError: Если сумма превышает текущий баланс.
        """
        self.validate_amount(amount)

        if amount > self._balance:
            raise ValueError('Недостаточно средств на счете')

        self._balance -= amount
        self._history.append(f'Снятие денежки на: -{amount}')

        return self._balance


    def get_history(self):
        """
        Метод, который возвращает копию истории операций.

        :return: Копия списка истории операций.
        """
        return self._history.copy()


    @classmethod
    def from_dict(cls, dictionary):
        """
        Метод, который создает объект класса из словаря.

        :param dictionary: Словарь с данными банковского счета.

        :return: Новый объект класса.
        """
        cardholder = dictionary.get('cardholder')
        balance = dictionary.get('balance')

        if not cls.check_string(cardholder):
            raise ValueError('Некорректное имя владельца')

        if not cls.check_value(balance) or balance < 0:
            raise ValueError('Некорректное значение баланса')

        return cls(**dictionary)


    def __str__(self):
        """
        Метод, который возвращает основные данные счета.

        :return: Строка с владельцем и балансом счета.
        """
        return f'Владелец: {self._cardholder}, 'f'баланс: {self._balance}'


class SavingsAccount(BankAccount):
    """
    Дочерний класс для создания сберегательного счета, который наследует класс BankAccount.
    """
    def __init__(self, cardholder, balance, interest_rate):
        """
        Базовый конструктор класса SavingsAccount.

        :param cardholder: Владелец банковского счета.

        :param balance: Начальный баланс счета.

        :param interest_rate: Процентная ставка.
        """
        super().__init__(cardholder=cardholder, balance=balance)

        if self.check_value(interest_rate) and interest_rate > 0:
            self._interest_rate = interest_rate
        else:
            raise ValueError('Процентная ставка должна быть положительной')


    @property
    def interest_rate(self):
        """
        Метод, который позволяет прочитать процентную ставку.

        :return: Процентная ставка сберегательного счета.
        """
        return self._interest_rate


    def add_interest(self):
        """
        Метод для начисления процентов на текущий баланс.

        :return: Новый баланс после начисления процентов.
        """
        interest = (self._balance * self._interest_rate / 100)
        self._balance += interest
        self._history.append(f'Начисление процентиков: +{interest}')

        return self._balance


    def spend(self, amount):
        """
        Переопределенный метод для снятия денежки.

        :param amount: Сумма снятия.

        :return: Новый баланс счета.

        :raises ValueError: Если сумма превышает 50 процентов текущего баланса.
        """
        self.validate_amount(amount)

        if self._balance * PERCENT_NUMBER < amount <= self._balance:
            raise ValueError('Нельзя снять более 50% баланса! Отказано!')

        return super().spend(amount)


    def __str__(self):
        """
        Метод, который возвращает основные данные сберегательного счета.

        :return: Строка с характеристиками счета.
        """
        return f'{super().__str__()}, 'f'процентная ставка: {self._interest_rate}%'


if __name__ == '__main__':
    account_1 = BankAccount(cardholder='Машуня', balance=5600)  #создание объекта через конструктор

    account_2 = BankAccount.from_dict({'cardholder': 'Леруся', 'balance': 3600})  #через классовый метод

    result_1 = account_1.top_up(500)  #пополнение
    print(result_1)

    result_2 = account_1.spend(300)  #снятие
    print(result_2)

    try:
        account_1.top_up(-100)  #ошибка при отрицательной сумме
    except ValueError as error:
        print(error)

    try:
        account_1.spend(10000)  #при превышении баланса
    except ValueError as error:
        print(error)

    try:
        account_1.balance = 10000  #невозможность изменить баланс напрямую
    except AttributeError as error:
        print("Нет setter'а - не меняем баланс напрямую, увы")

    history_1 = account_1.get_history()  #вывод истории операций
    print(history_1)

    account_3 = BankAccount(cardholder='Мистер X', balance=1000)  #полиморфный вызов

    savings_1 = SavingsAccount(cardholder='Мистер N', balance=500, interest_rate=5)

    accounts = (account_3, savings_1)

    for account in accounts:
        try:
            result_3 = account.spend(300)
            print(result_3)
        except ValueError as error:
            print(error)
            

#!/usr/bin/env python3

class BankAccount:
    """
    Базовый класс банковского счёта

    Хранит приватные переменные баланса, владельца и истории транзакции
    """

    def __init__(self, owner, initial_balance = 0.0):
        """
        Инициализирует банковский счет
        :param owner: Имя владельца счёта
        :param initial_balance: Начальный баланс
        :return: Ничего не возвращает, создает объект счета с заданными параметрами
        """
        self.__owner = owner
        self.__balance = 0.0
        self.__history = []

        if initial_balance > 0:
            self.deposit(initial_balance, "Начальный взнос")

    @property
    def balance(self):
        """
        Возвращает текущий баланс счета
        :return: Текущий баланс счета
        """
        return self.__balance

    @property
    def owner(self):
        """
        Возвращает имя владельца счет
        :return: Имя владельца счета
        """
        return self.__owner

    @property
    def history(self):
        """
        Возвращает копию истории транзакции
        :return: Копия списка словарей с историей операций
        """
        return self.__history.copy()

    def deposit(self, amount, description = "Пополнение"):
        """
        Пополняет счет на указанную сумму и записывает операцию в историю
        :param amount: Сумма пополнения
        :param description: Текстовое описание операции
        :return: Ничего не возвращает, увеличивает баланс и добавляет запись в историю
        """
        if not isinstance(amount, float|int):
            raise TypeError (f"Сумма внесения должна быть числом!!! Было получено: {type(amount).__name__}")
        if amount <= 0:
            raise ValueError ("Сумма должна быть положительной!")
        self.__balance += amount
        self.add_to_history("Пополнение", amount, description)
        print(f"Было выполнено пополнение: +{amount}руб. (баланс: {self.__balance}руб.)")

    def conclusion(self, amount, description = "Снятие"):
        """
        Снимает указанную сумму со счёта и записывает операцию в историю
        :param amount: Сумма снятия
        :param description: Текстовое описание операции
        :return: Ничего не возвращает, уменьшает баланс и добавляет запись в историю
        """
        if not isinstance(amount, float|int):
            raise TypeError(f"Сумма должна быть числом! Было получено: {type(amount).__name__}")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError(f"Ошибка! У Вас нет столько денег! Было запрошено: {amount}, баланс: {self.__balance}")

        self.__balance -= amount
        self.add_to_history("Снятие", amount, description)

        print(f"Снятие: {amount}руб. (баланс: {self.__balance}руб.)")

    def add_to_history(self, operation_type, amount, description):
        """
        Добавляет запись об успешной операции во внутренний список истории
        :param operation_type: Тип операции
        :param amount: Сумма операции
        :param description: Описание операции
        :return: Ничего не возвращает, добавляет словарь с данными операциями в историю
        """
        record ={
            "type" : operation_type,
            "amount" : amount   ,
            "description" : description,
            "balans_after": self.__balance
        }
        self.__history.append(record)

    @classmethod
    def create_account(cls, owner, initial_balance = 0.0):
        """
        Публичный метод для создания банковского счета
        :param owner: Имя владельца счета
        :param initial_balance: Начальный баланс
        :return: Новый объект банковского счета
        """
        return cls(owner, initial_balance)

    def __str__(self):
        """
        Возвращает описание объекта
        :return: Строка, содержащая информацию об имени владельца и баланса
        """
        return f"BankAccount( owner = {self.owner}, balance = {self.balance}руб.)"

class SavingAccount(BankAccount):
    """
    Сберегательный счет. Наследует BankAccount и добавляет процентную ставку
    Со счета нельзя снимать более 50% текущего баланса
    """
    def __init__(self, owner, initial_balance = 0.0, interest_rate = 0.0):
        """
        Инициализирует сберегательный счет
        :param owner: Имя владельца счета
        :param initial_balance: Начальный баланс
        :param interest_rate: Годовая процентная ставка в процентах
        :return: Ничего не возвращает, создаёт объект сберегательного счета
        """
        super().__init__(owner, initial_balance)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        """
        Возвращает текущую процентную ставку
        :return: Процентная ставка
        """
        return self.__interest_rate

    def add_interest(self):
        """
        Начисляет процент на текущий баланс согласно ставке и записывает это в историю
        :return: Сумма начисленных процентов
        """
        interest_amount = self.balance * (self.interest_rate / 100)
        if interest_amount > 0:
            self.deposit(interest_amount, f" Начисление процентов ({self.interest_rate})")
        return interest_amount

    def conclusion(self, amount, description = "Снятие" ):
        """
        Снимает сумму со счета с проверкой лимита
        :param amount: Сумма снятия
        :param description: Описание операции
        :return: Ничего не возвращает, уменьшает баланс и добавляет запись в историю
        """
        max_conclusion = self.balance * 0.5
        if amount > max_conclusion:
            raise ValueError("Нельзя снимать более 50% баланса")
        super().conclusion(amount, description)

    @classmethod
    def create_account(cls, owner, initial_balance = 0.0, interest_rate = 0.0):
        """
        Публичный метод для создания сберегательного счета
        :param owner: Имя владельца счета
        :param initial_balance: Начальный баланс
        :param interest_rate: Годовая процентная ставка в процентах
        :return: Новый объект сберегательного счета
        """
        return cls(owner, initial_balance, interest_rate)

if __name__ == "__main__":
    account1 = BankAccount.create_account("Иванов Валера", 1000.0)
    account2 = SavingAccount.create_account("Сидоров Иван", 5000.0, 5.0)

    account1.deposit(500.0, "Зарплата")
    account1.conclusion(200.0, "Покупки")
    account2.conclusion(500.0, "Оплата ЖКХ")

    try:
        account1.deposit(-100)
    except ValueError as e:
        print(e)

    try:
        account2.conclusion(3000)
    except ValueError as e:
        print(e)

    try:
        account1.balance = 999999.9
    except AttributeError as e:
        print(e)

    for record in account1.history:
        print(f"{record['type']}: {record['amount']}руб. ({record['description']}) -> баланс: {record['balans_after']}руб.")

    accounts = [
        BankAccount.create_account("Тест1", 1000.0),
        SavingAccount.create_account("Тест2", 1000.0, 3.0)

    ]
    for account in accounts:
        try:
            account.conclusion(600.0, "Тестовое снятие")
        except ValueError as e:
            print(e)

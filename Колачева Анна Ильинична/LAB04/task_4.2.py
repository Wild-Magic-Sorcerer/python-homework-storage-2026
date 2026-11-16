#!/usr/bin/env python3

import math


class BankAccount:
    """
    Основной класс банковского счёта
    """

    def __init__(self, owner, balance=0):
        """
        Конструктор банковского счёта

        :param owner: владелец счёта
        :param balance: начальный баланс
        """
        self.__owner = owner
        self.__balance = 0
        self.__history = []

        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Что за инопланетянин?")

        self.__owner = owner.strip()
        self.__balance = self._check_money(balance, allow_zero=True)

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return self.get_history()

    @staticmethod
    def _check_money(value, allow_zero=False):
        """
        Проверяет корректность денежной суммы

        :param value: денежная сумма
        :return: проверенная сумма
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Сумма должна быть числом!")

        if not math.isfinite(value):
            raise ValueError("Сумма должна быть конечным числом!")

        if value < 0 or (not allow_zero and value == 0):
            raise ValueError("Сумма должна быть положительной!")

        return value

    @classmethod
    def create_account(cls, owner, balance=0):
        """
        Создаёт новый банковский счёт

        :param owner: владелец счёта
        :param balance: начальный баланс
        :return: новый объект банковского счёта
        """
        return cls(owner, balance)

    def get_history(self):
        """
        Возвращает копию истории операций

        :return: список транзакций
        """
        return [transaction.copy() for transaction in self.__history]

    def _save_transaction(self, operation, amount):
        """
        Записывает операцию в историю
        """
        self.__history.append({
            "operation": operation,
            "amount": amount,
            "balance_after": self.__balance
        })

    def _increase_balance(self, amount, operation):
        """
        Увеличивает баланс и записывает операцию
        """
        self.__balance += amount
        self._save_transaction(operation, amount)

    def _decrease_balance(self, amount, operation):
        """
        Уменьшает баланс и записывает операцию
        """
        self.__balance -= amount
        self._save_transaction(operation, amount)

    def deposit(self, amount):
        """
        Пополняет банковский счёт

        :param amount: сумма пополнения
        :return: новый баланс
        """
        amount = self._check_money(amount)

        self._increase_balance(amount, "Пополнение")
        return self.balance

    def withdraw(self, amount):
        """
        Снимает деньги с банковского счёта

        :param amount: сумма снятия
        :return: новый баланс
        """
        amount = self._check_money(amount)

        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте!")

        self._decrease_balance(amount, "Снятие")
        return self.balance


class SavingsAccount(BankAccount):
    """
    Класс сберегательного счёта
    """

    def __init__(self, owner, balance=0, interest_rate=0):
        """
        Конструктор сберегательного счёта
        """
        super().__init__(owner, balance)

        self.__interest_rate = self._check_money(
            interest_rate, allow_zero=True
        )

    @property
    def interest_rate(self):
        return self.__interest_rate

    @classmethod
    def create_account(cls, owner, balance=0, interest_rate=0):
        """
        Создаёт новый сберегательный счёт
        """
        return cls(owner, balance, interest_rate)

    def add_interest(self):
        """
        Начисляет проценты на текущий баланс

        :return: размер начисленных процентов
        """
        interest = self.balance * self.interest_rate / 100

        if interest > 0:
            self._increase_balance(interest, "Начисление процентов")

        return interest

    def withdraw(self, amount):
        """
        Снимает деньги, но не более 50% баланса.

        :param amount: сумма снятия
        :return: новый баланс
        """
        amount = self._check_money(amount)

        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте!")

        if amount > self.balance * 0.5:
            raise ValueError("Нельзя снять более 50% баланса!")

        return super().withdraw(amount)


if __name__ == "__main__":

    # 1 Создание банковского счёта
    account = BankAccount.create_account("Анна", 1000)

    # 2 Пополнение и снятие
    account.deposit(500)
    account.withdraw(200)

    print("Баланс обычного счёта:", account.balance)

    # 3 Проверка отрицательной суммы
    try:
        account.deposit(-100)
    except ValueError as e:
        print("Ошибка:", e)

    # 4 Проверка превышения баланса
    try:
        account.withdraw(5000)
    except ValueError as e:
        print("Ошибка:", e)

    # 5 Попытка изменить баланс напрямую
    try:
        account.balance = 10000
    except AttributeError:
        print("Баланс нельзя изменить напрямую!")

    # 6 Создание сберегательного счёта
    savings = SavingsAccount.create_account("Мария", 1000, 5)

    savings.deposit(200)
    savings.withdraw(500)

    # 7 Начисление процентов
    interest = savings.add_interest()
    print("Начислено процентов:", interest)
    print("Баланс сберегательного счёта:", savings.balance)

    # 8 Полиморфный вызов метода снятия
    accounts = [account, savings]

    for acc in accounts:
        print(f"Владелец: {acc.owner}\n")

        try:
            acc.withdraw(400)
            print("Снятие успешно:", acc.balance)
        except ValueError as e:
            print("Ошибка:", e)

    # 9 Вывод истории операций
    print("История обычного счёта:\n")
    for operation in account.get_history():
        print(operation)

    print("История сберегательного счёта:\n")
    for operation in savings.get_history():
        print(operation)
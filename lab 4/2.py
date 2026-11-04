#!/usr/bin/env python3

start_balance = 0
min_transaction = 1
max_withdraw_percent = 0.5


class BankAccount:
    """Банковский счет."""

    def __init__(self, owner, balance=start_balance):
        """Инициализация счета."""
        self.__owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def owner(self):
        """Возвращает имя владельца."""
        return self.__owner

    @property
    def balance(self):
        """Возвращает текущий баланс."""
        return self.__balance

    def get_history(self):
        """Возвращает копию истории транзакций."""
        return self.__history.copy()

    def deposit(self, amount):
        """Пополнение счета."""
        if amount < min_transaction:
            raise ValueError("сумма пополнения слишком мала")
        self.__balance += amount
        self.__history.append(f"пополнение: +{amount}")

    def withdraw(self, amount):
        """Снятие со счета."""
        if amount < min_transaction:
            raise ValueError("сумма снятия слишком мала")
        if amount > self.__balance:
            raise ValueError("недостаточно средств")
        self.__balance -= amount
        self.__history.append(f"снятие: -{amount}")

    @classmethod
    def create_account(cls, owner):
        """Публичный метод для создания счета."""
        return cls(owner)


class SavingsAccount(BankAccount):
    """Сберегательный счет."""

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """Начисляет проценты на баланс."""
        self.deposit(self.balance * self.interest_rate)

    def withdraw(self, amount):
        """Снятие с ограничением 50% от баланса."""
        max_allowed = self.balance * max_withdraw_percent
        if amount > max_allowed:
            raise ValueError("нельзя снять больше 50% баланса")
        super().withdraw(amount)


if __name__ == "__main__":
    schet = BankAccount.create_account("Иван")
    schet.deposit(1000)
    schet.withdraw(300)

    print(f"баланс после операций: {schet.balance}")

    print("ошибки")
    try:
        schet.deposit(-50)
    except ValueError as oshibka:
        print(f"ошибка пополнения: {oshibka}")

    try:
        schet.withdraw(5000)
    except ValueError as oshibka:
        print(f"ошибка снятия: {oshibka}")

    print("прямое изменение баланса")
    try:
        schet.balance = 999999
    except AttributeError as oshibka:
        print(f"ошибка изменения: {oshibka}")

    print("история операций")
    print(schet.get_history())

    print("полиморфизм")
    sber = SavingsAccount("Мария", 2000, 0.1)
    for tek_schet in [schet, sber]:
        try:
            tek_schet.withdraw(1100)
            print(f"у {tek_schet.owner} успешно снято")
        except ValueError as oshibka:
            print(f"у {tek_schet.owner} ошибка: {oshibka}")

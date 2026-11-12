#!/usr/bin/env python3


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным!")

        self.__owner = owner
        self.__balance = balance
        self.__history = []


    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    def get_history(self):
        return self.__history[:]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной!")

        self.__balance += amount
        self.__history.append(f"Пополнение: +{amount}. Баланс: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной!")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете!")

        self.__balance -= amount
        self.__history.append(f"Снятие: -{amount}. Баланс: {self.__balance}")

    @classmethod
    def create_account(cls, owner, initial_balance):
        return cls(owner, initial_balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

    def withdraw(self, amount):
        if amount > self.balance * 0.5:
            raise ValueError("Нельзя снять более 50% баланса за одну операцию!")
        super().withdraw(amount)


if __name__ == '__main__':
    print("Создаем обычный счет")
    acc = BankAccount("Анна", 1000)
    print(f"Баланс: {acc.balance}")

    print("\nПополняем на 500...")
    acc.deposit(500)
    print(f"Баланс: {acc.balance}")

    print("\nСоздаем сберегательный счет с 10% ставкой...")
    sav_acc = SavingsAccount("Мария", 1000, 0.10)
    print(f"Баланс Марии: {sav_acc.balance}")

    print("\nНачисляем проценты...")
    sav_acc.apply_interest()
    print(f"Баланс после процентов: {sav_acc.balance}")

    print("\nПытаемся снять 600 (это больше 50% баланса)...")
    try:
        sav_acc.withdraw(600)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПытаемся снять 400 (это меньше 50% баланса)...")
    sav_acc.withdraw(400)
    print(f"Итоговый баланс: {sav_acc.balance}")
    
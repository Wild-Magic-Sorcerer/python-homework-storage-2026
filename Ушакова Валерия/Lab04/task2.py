#!/usr/bin/env python3

class BankAccount:
    """Класс банковского счета."""

    def __init__(self, owner, balance=0):
        """
        Инициализация счета.
        
        :param owner: Владелец счета.
        :param balance: Начальный баланс (по умолчанию 0).
        :raises ValueError: Если начальный баланс отрицательный.
        """
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным!")

        
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
        """Возвращает копию истории операций."""
        return self.__history[:]

    def deposit(self, amount):
        """
        Пополнение счета.
        :param amount: Сумма пополнения.
        :raises ValueError: Если сумма меньше или равна нулю.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной!")

        self.__balance += amount
        self.__history.append(f"Пополнение: +{amount}. Баланс: {self.__balance}")

    def withdraw(self, amount):
        """
        Снятие денег со счета.
        :param amount: Сумма снятия.
        :raises ValueError: Если сумма меньше или равна нулю, или превышает баланс.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной!")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счете!")

        self.__balance -= amount
        self.__history.append(f"Снятие: -{amount}. Баланс: {self.__balance}")


    def __str__(self):
        """
        Строковое представление счета.
        :return: Строка с информацией о владельце и балансе.
        """
        return f"Владелец: {self.__owner}, Баланс: {self.__balance}"


class SavingsAccount(BankAccount):
    """Сберегательный счет с начислением процентов."""
    
    WITHDRAW_LIMIT = 0.5

    def __init__(self, owner, balance=0, interest_rate=0.05):
        """
        Инициализация сберегательного счета.
        
        :param interest_rate: Процентная ставка (по умолчанию 0.05).
        """
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        """Возвращает процентную ставку."""
        return self._interest_rate

    def apply_interest(self):
        """Начисление процентов на текущий баланс."""
        interest_amount = self.balance * self._interest_rate
        self.deposit(interest_amount)

    def withdraw(self, amount):
        """
        Снятие денег с ограничением в 50% от баланса.
        :param amount: Сумма снятия.
        :raises ValueError: Если сумма превышает 50% баланса.
        """
        if amount > self.balance * self.WITHDRAW_LIMIT:
            raise ValueError("Нельзя снять более 50% баланса за одну операцию!")
        super().withdraw(amount)

    def __str__(self):
        """
        Строковое представление сберегательного счета.
        :return: Строка с информацией о счете и ставке.
        """
        return f"Сберегательный счет. Владелец: {self.owner}, Баланс: {self.balance}, Ставка: {self._interest_rate * 100}%"


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

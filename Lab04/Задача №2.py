#!/usr/bin/env python3

class BankAccount:
    """
    Банковский счёт с приватными полями и историей операций.
    """
    def __init__(self, owner, balance=0):
        """
        Конструктор.
        Параметры:
            owner (str): владелец счёта.
            balance (int | float): начальный баланс (по умолчанию 0).
        Возвращает:
            None
        """
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Владелец должен быть непустой строкой")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.__owner = owner
        self.__balance = balance
        self.__history = []

    @property
    def owner(self):
        """
        Свойство только для чтения: владелец.
        Параметры:
            Нет.
        Возвращает:
            str: имя владельца.
        """
        return self.__owner

    @property
    def balance(self):
        """
        Свойство только для чтения: баланс.
        Параметры:
            Нет.
        Возвращает:
            int | float: текущий баланс.
        """
        return self.__balance

    def deposit(self, amount):
        """
        Пополнение счёта.
        Параметры:
            amount (int | float): сумма пополнения (> 0).
        Возвращает:
            None
        Исключения:
            ValueError: если сумма не положительная.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount
        self.__history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        """
        Снятие денег со счёта.
        Параметры:
            amount (int | float): сумма снятия (> 0).
        Возвращает:
            None
        Исключения:
            ValueError: если сумма не положительная или превышает баланс.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        self.__history.append(f"Снятие: -{amount}")

    def get_history(self):
        """
        Возвращает КОПИЮ истории операций.
        Параметры:
            Нет.
        Возвращает:
            list[str]: копия списка операций.
        """
        return list(self.__history)

    @classmethod
    def create(cls, owner, initial_balance=0):
        """
        Публичный классовый метод для создания счёта.
        Параметры:
            owner (str): владелец.
            initial_balance (int | float): начальный баланс.
        Возвращает:
            BankAccount: новый объект.
        """
        return cls(owner, initial_balance)


class SavingsAccount(BankAccount):
    """
    Сберегательный счёт: добавляет процентную ставку и лимит снятия.
    """
    def __init__(self, owner, balance=0, interest_rate=5):
        """
        Конструктор.
        Параметры:
            owner (str): владелец.
            balance (int | float): начальный баланс.
            interest_rate (int | float): годовая ставка в процентах.
        Возвращает:
            None
        """
        super().__init__(owner, balance)
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Ставка должна быть неотрицательной")
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        """
        Свойство только для чтения: процентная ставка.
        Параметры:
            Нет.
        Возвращает:
            int | float: ставка в процентах.
        """
        return self.__interest_rate

    def apply_interest(self):
        """
        Начисляет проценты на текущий баланс и записывает это в историю.
        Параметры:
            Нет.
        Возвращает:
            None
        """
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)

    def withdraw(self, amount):
        """
        Переопределённое снятие: не более 50% баланса за операцию.
        Параметры:
            amount (int | float): сумма снятия.
        Возвращает:
            None
        Исключения:
            ValueError: если сумма не положительная, превышает баланс
            или превышает 50% от баланса.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        limit = self.balance * 0.5
        if amount > limit:
            raise ValueError(f"Нельзя снять более 50% баланса (макс {limit})")
        super().withdraw(amount)

if __name__ == "__main__":
    acc = BankAccount.create("Иван", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print("Баланс:", acc.balance)
    print("История:", acc.get_history())
    try:
        acc.deposit(-100)
    except ValueError as e:
        print("Ошибка пополнения:", e)

    try:
        acc.withdraw(10000)
    except ValueError as e:
        print("Ошибка снятия:", e)
    try:
        acc.balance = 999999
    except AttributeError as e:
        print("Нельзя изменить баланс:", type(e).__name__)
    sav = SavingsAccount("Мария", 1000, 10)
    sav.apply_interest()
    print("После процентов:", sav.balance)
    accounts = [acc, sav]
    for a in accounts:
        try:
            a.withdraw(400)
            print(f"{a.owner}: снятие 400 успешно, баланс {a.balance}")
        except ValueError as e:
            print(f"{a.owner}: ошибка — {e}")

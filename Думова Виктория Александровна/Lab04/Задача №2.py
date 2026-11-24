#!/usr/bin/env python3

MIN_BALANCE = 0
MAX_WITHDRAW_PERCENT = 0.5
DEFAULT_INTEREST_RATE = 5
PERCENT_DIVISOR = 100

class BankAccount:
    """
    Банковский счёт с защищёнными полями и историей операций.

    Attributes:
        _owner: владелец счёта.
        _balance: текущий баланс.
        _history: список операций.
    """

    def __init__(self, owner, balance=MIN_BALANCE):
        """
        Конструктор.

        Args:
            owner (str): владелец счёта.
            balance (int | float): начальный баланс (по умолчанию 0).

        Returns:
            None

        Raises:
            ValueError: если владелец пустой или баланс отрицательный.
        """
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Владелец должен быть непустой строкой")
        if balance < MIN_BALANCE:
            raise ValueError("Баланс не может быть отрицательным")
        self._owner = owner
        self._balance = balance
        self._history = []

    @property
    def owner(self):
        """
        Свойство только для чтения: владелец.

        Args:
            None

        Returns:
            str: имя владельца.
        """
        return self._owner

    @property
    def balance(self):
        """
        Свойство только для чтения: баланс.

        Args:
            None

        Returns:
            int | float: текущий баланс.
        """
        return self._balance

    def deposit(self, amount):
        """
        Пополнение счёта.

        Args:
            amount (int | float): сумма пополнения (> 0).

        Returns:
            None

        Raises:
            ValueError: если сумма не положительная.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        self._history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        """
        Снятие денег со счёта.

        Args:
            amount (int | float): сумма снятия (> 0).

        Returns:
            None

        Raises:
            ValueError: если сумма не положительная или превышает баланс.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount
        self._history.append(f"Снятие: -{amount}")

    def get_history(self):
        """
        Возвращает КОПИЮ истории операций.

        Args:
            None

        Returns:
            list[str]: копия списка операций.
        """
        return list(self._history)

    @classmethod
    def create(cls, owner, initial_balance=MIN_BALANCE):
        """
        Публичный классовый метод для создания счёта.

        Args:
            owner (str): владелец.
            initial_balance (int | float): начальный баланс.

        Returns:
            BankAccount: новый объект.
        """
        return cls(owner, initial_balance)

    def __str__(self):
        """
        Возвращает строковое представление счёта.

        Args:
            None

        Returns:
            str: строка с владельцем и балансом.
        """
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


class SavingsAccount(BankAccount):
    """
    Сберегательный счёт: добавляет процентную ставку и лимит снятия.

    Attributes:
        _interest_rate: годовая процентная ставка.
    """

    def __init__(self, owner, balance=MIN_BALANCE, interest_rate=DEFAULT_INTEREST_RATE):
        """
        Конструктор.

        Args:
            owner (str): владелец.
            balance (int | float): начальный баланс.
            interest_rate (int | float): годовая ставка в процентах.

        Returns:
            None

        Raises:
            ValueError: если ставка отрицательная.
        """
        super().__init__(owner, balance)
        if not isinstance(interest_rate, (int, float)) or interest_rate < 0:
            raise ValueError("Ставка должна быть неотрицательной")
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        """
        Свойство только для чтения: процентная ставка.

        Args:
            None

        Returns:
            int | float: ставка в процентах.
        """
        return self._interest_rate

    def apply_interest(self):
        """
        Начисляет проценты на текущий баланс и записывает это в историю.

        Args:
            None

        Returns:
            None
        """
        interest = self.balance * self.interest_rate / PERCENT_DIVISOR
        self.deposit(interest)

    def withdraw(self, amount):
        """
        Переопределённое снятие: не более 50% баланса за операцию.

        Args:
            amount (int | float): сумма снятия.

        Returns:
            None

        Raises:
            ValueError: если сумма не положительная, превышает баланс
                        или превышает 50% от баланса.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        limit = self.balance * MAX_WITHDRAW_PERCENT
        if amount > limit:
            raise ValueError(f"Нельзя снять более 50% баланса (макс {limit})")
        super().withdraw(amount)

    def __str__(self):
        """
        Возвращает строковое представление сберегательного счёта.

        Args:
            None

        Returns:
            str: строка с владельцем, балансом и ставкой.
        """
        return f"{super().__str__()}, Ставка: {self.interest_rate}%"


if __name__ == "__main__":
    acc = BankAccount.create("Иван", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc)
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

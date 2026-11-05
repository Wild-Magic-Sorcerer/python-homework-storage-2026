#!/usr/bin/env python3

MAX_WITHDRAW_PERCENT = 0.5
BASE_INTEREST = 3.0

class BankAccount:
    def __init__(self, owner: str, start_balance: float = 0.0):
        """
        Инициализирует банковский счет.

        Параметры:
        owner — имя владельца счета.
        start_balance — начальный баланс.

        Возвращает:
        None
        """
        self._owner = owner
        self._balance = start_balance
        self._history = []

        if start_balance > 0:
            self._history.append(f"Открытие счета: +{start_balance}")

    @property
    def owner(self) -> str:
        """
        Свойство для чтения имени владельца.

        Параметры:
        Нет.

        Возвращает:
        Имя владельца.
        """
        return self._owner

    @property
    def balance(self) -> float:
        """
        Свойство для чтения текущего баланса.

        Параметры:
        Нет.

        Возвращает:
        Текущий баланс.
        """
        return self._balance

    def copy_history(self) -> list[str]:
        """
        Возвращает копию истории транзакций.

        Параметры:
        Нет.

        Возвращает:
        Копию списка с историей операций.
        """
        return self._history.copy()

    def add_funds(self, amount: float) -> None:
        """
        Пополняет счет на указанную сумму.

        Параметры:
        amount — сумма пополнения.

        Возвращает:
        None
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля.")

        self._balance += amount
        self._history.append(f"Пополнение: +{amount}")

    def take_funds(self, amount: float) -> None:
        """
        Снимает деньги со счета.

        Параметры:
        amount — сумма для снятия.

        Возвращает:
        None
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля.")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете.")

        self._balance -= amount
        self._history.append(f"Снятие: -{amount}")

    @classmethod
    def build_from_dict(cls, data: dict[str, object]) -> "BankAccount":
        """
        Создает объект счета из словаря.

        Параметры:
        data — словарь с данными владельца и баланса.

        Возвращает:
        Новый экземпляр банковского счета.
        """
        owner = str(data.get("owner", "Неизвестно"))
        balance = float(data.get("balance", 0.0))
        return cls(owner=owner, start_balance=balance)


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, start_balance: float = 0.0, rate: float = BASE_INTEREST):
        """
        Инициализирует сберегательный счет.

        Параметры:
        owner — имя владельца счета.
        start_balance — начальный баланс.
        rate — процентная ставка.

        Возвращает:
        None
        """
        super().__init__(owner, start_balance)
        self.rate = rate

    def add_percents(self) -> None:
        """
        Начисляет проценты на текущий баланс.

        Параметры:
        Нет.

        Возвращает:
        None
        """
        profit = self.balance * (self.rate / 100)
        self.add_funds(profit)

    def take_funds(self, amount: float) -> None:
        """
        Снимает деньги со сберегательного счета с учетом лимита.

        Параметры:
        amount — сумма для снятия.

        Возвращает:
        None
        """
        limit = self.balance * MAX_WITHDRAW_PERCENT
        if amount > limit:
            raise ValueError(f"Превышен лимит! Можно снять не более {limit}.")

        super().take_funds(amount)

if __name__ == '__main__':
    print("1. Создание и корректные операции")
    acc_data = {"owner": "Ярослава", "balance": 1000.0}
    my_acc = BankAccount.build_from_dict(acc_data)

    my_acc.add_funds(500.0)
    my_acc.take_funds(200.0)
    print(f"Баланс {my_acc.owner}: {my_acc.balance}")

    print("\n2. Ошибки при отрицательной сумме и превышении баланса")
    try:
        my_acc.take_funds(5000.0)
    except ValueError as e:
        print(f"Ошибка снятия: {e}")

    try:
        my_acc.add_funds(-100.0)
    except ValueError as e:
        print(f"Ошибка пополнения: {e}")

    print("\n3. Невозможность изменить баланс напрямую")
    try:
        my_acc.balance = 999999.0
    except AttributeError as e:
        print("Ошибка! Баланс защищен от прямой записи!")

    print("\n4. Вывод истории операций")
    for record in my_acc.copy_history():
        print(record)

    print("\n5. Полиморфное поведение метода снятия денег")
    accounts = [
        BankAccount("Обычный", 1000.0),
        SavingsAccount("Сберегательный", 1000.0)
    ]

    for acc in accounts:
        print(f"\nПопытка снять 600 со счета '{acc.owner}'...")
        try:
            acc.take_funds(600.0)
            print("Успешно! Новый баланс:", acc.balance)
        except ValueError as e:
            print(f"Отказ: {e}")


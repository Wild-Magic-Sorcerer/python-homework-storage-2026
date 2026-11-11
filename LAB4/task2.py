#!/usr/bin/env python3
# Задание 2 — BankAccount / SavingAccount


class BankAccount:
    """
    Класс банковского счёта.

    :param owner: имя владельца счёта
    :param init_balance: начальный баланс
    """
    def __init__(self, owner, init_balance):
        self.__owner = owner
        self._history = []
        try:
            init_balance = float(init_balance)
        except (TypeError, ValueError):
            print("Баланс должен быть числом"); init_balance = 0
        if init_balance < 0:
            print("Баланс не может быть отрицательным"); init_balance = 0
        self._balance = init_balance

    @property
    def owner(self):
        """
        Возвращает имя владельца счёта.
        """
        return self.__owner

    @property
    def balance(self):
        """
        Возвращает текущий баланс счёта.
        """
        return self._balance

    @property
    def history(self):
        """
        Возвращает копию истории транзакций.
        """
        return self._history.copy()

    def deposit(self, amount):
        """
        Пополняет счёт на указанную сумму.

        :param amount: сумма пополнения
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print("Сумма должна быть числом"); return
        if amount <= 0:
            print("Сумма должна быть > 0"); return
        self._balance += amount
        self._history.append(f"Пополнение +{amount} руб. Баланс: {self._balance} руб.")
        print(f"Пополнено на {amount}. Баланс: {self._balance}")

    def withdrawal(self, amount):
        """
        Снимает указанную сумму со счёта.

        :param amount: сумма снятия
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print("Сумма должна быть числом"); return
        if amount <= 0:
            print("Сумма должна быть > 0"); return
        if amount > self._balance:
            print("Недостаточно средств"); return
        self._balance -= amount
        self._history.append(f"Снятие -{amount} руб. Баланс: {self._balance} руб.")
        print(f"Снято {amount}. Баланс: {self._balance}")

    def get_info(self):
        """
        Возвращает строку с информацией о счёте.

        :return: строка с описанием
        """
        return f"Владелец: {self.__owner}, Баланс: {self._balance} руб."

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект BankAccount из словаря.

        :param data: словарь с ключами owner и init_balance
        :return: новый объект BankAccount
        """
        return cls(data["owner"], data["init_balance"])


class SavingAccount(BankAccount):
    """
    Сберегательный счёт — наследник BankAccount.

    :param owner: имя владельца счёта
    :param init_balance: начальный баланс
    :param bet: процентная ставка (% годовых)
    """
    def __init__(self, owner, init_balance, bet):
        super().__init__(owner, init_balance)
        self.__bet = bet

    @property
    def bet(self):
        """
        Возвращает процентную ставку.
        """
        return self.__bet

    def add_procent(self):
        """
        Начисляет проценты на текущий баланс.
        """
        proc = self.balance * self.__bet / 100
        self._balance += proc
        self._history.append(f"Проценты +{proc} руб. Баланс: {self._balance} руб.")
        print(f"Начислено {proc} ({self.__bet}%). Баланс: {self.balance}")

    def withdrawal(self, amount):
        """
        Снимает сумму, но не более 60% баланса.

        :param amount: сумма снятия
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            print("Сумма должна быть числом"); return
        if amount <= 0:
            print("Сумма должна быть > 0"); return
        if amount > self.balance * 0.6:
            print(f"Максимум 60%: {self.balance * 0.6}"); return
        if amount > self.balance:
            print(f"Недостаточно средств: {self.balance}"); return
        self._balance -= amount
        self._history.append(f"Снятие -{amount} руб. Баланс: {self._balance} руб.")
        print(f"Снято {amount}. Баланс: {self.balance}")

    def get_info(self):
        """
        Возвращает строку с информацией о сберегательном счёте.

        :return: строка с описанием
        """
        return f"{super().get_info()}, Ставка: {self.__bet}%"


if __name__ == "__main__":
    print("Конструкторы:")
    acc = BankAccount("Пётр", 12000)
    sav = SavingAccount("Пётр", 12000, 8)
    print(acc.get_info()); print(sav.get_info())

    print("\nИз словаря:")
    print(BankAccount.from_dict({"owner": "Ольга", "init_balance": 500000}).get_info())

    print("\nКорректные операции:")
    acc.deposit(750); acc.withdrawal(500)
    sav.deposit(10); sav.withdrawal(3000)

    print("\nОшибки:")
    print("Отрицательное пополнение:"); acc.deposit(-200)
    print("Снятие больше баланса:"); acc.withdrawal(50000)
    print("Снятие >60%:"); sav.withdrawal(9000)

    print("\nПопытка изменить баланс (проверка только для чтения):")
    try:
        # Используем setattr, чтобы PyCharm не ругался, а Python честно проверил
        setattr(acc, 'balance', 999999)
    except AttributeError as e:
        print(f"Ошибка: {e}")
    print(f"Баланс: {acc.balance}")

    print("\nИстория обычного счёта:")
    for line in acc.history:
        print("-", line)

    print("\nИстория сберегательного счёта:")
    for line in sav.history:
        print("-", line)

    print("\nНачисление процентов:")
    sav.add_procent()

    print("\nПолиморфизм снятия:")
    for a in (acc, sav):
        print(f"{a.owner}: снятие 4000")
        a.withdrawal(4000)
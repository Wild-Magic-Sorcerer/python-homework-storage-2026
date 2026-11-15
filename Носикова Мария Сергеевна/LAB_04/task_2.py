#!/usr/bin/env python3

class BankAccount:
    """
    Класс банковского счета.
    """
    def __init__(self, owner, init_balance):
        """
        Инициализирует банковский счёт.

        :param owner: Имя владельца счета.
        :param init_balance: начальный баланс.
        :raises ValueError: Если параметры некорректны.
        """
        self.__owner = None
        self._balance = 0
        self._history = []
        self.owner = owner
        self.balance = init_balance


    @property
    def owner(self):
        """
        Возвращает имя владельца счета.
        """
        return self.__owner

    @owner.setter
    def owner(self, value):
        """
        Устанавливает имя владельца.

        :param value: Имя владельца.
        :raises ValueError: Если имя некорректно.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя владельца не должно быть пустым.")
        self.__owner = value.strip()


    @property
    def balance(self):
        """
        Возвращает текущий баланс счета.
        """
        return self._balance

    @balance.setter
    def balance(self, value):
        """
        Устанавливает баланс.

        :param value: Начальный баланс.
        :raises ValueError: Если баланс некорректен.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Баланс должен быть числом.")
        if value < 0:
            raise ValueError("Баланс должен быть неотрицательным числом.")
        self._balance = value


    @property
    def history(self):
        """
        Возвращает копию истории транзакций
        """
        return self._history.copy()


    def deposit(self, summa):
        """
        Пополняет счет на определенную сумму.

        :param summa: Сумма пополнения.
        :raises ValueError: Если сумма некорректна.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            raise ValueError("Сумма должна быть числом.")
        if summa <= 0:
            raise ValueError("Сумма поплнения счета должна быть больше 0.")
        self._balance += summa
        self._history.append(f"Пополнение счета на {summa} рублей. Баланс: {self._balance} рублей.")
        print(f"Счет пополнен на {summa} рублей. Текущий баланс: {self._balance} рублей.")


    def withdrawal(self, summa):
        """
        Снимает определенную сумму со счета.

        :param summa: Сумма, которую надо снять.
        :raises ValueError: Если сумма некорректна или превышает баланс.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            raise ValueError("Сумма должна быть числом.")
        if summa <= 0:
            raise ValueError("Сумма снятия счета должна быть больше 0.")
        if summa > self._balance:
            raise ValueError(f"Недостаточно средств. Доступно: {self._balance} рублей.")
        self._balance -= summa
        self._history.append(f"Снятие со счета: {summa} рублей. Баланс: {self._balance} рублей.")
        print(f"Со счета снято {summa} рублей. Текущий баланс: {self._balance} рублей.")

        
    def __str__(self):
        """
        Возвращает строку с информацией о счете.
        """
        return f"Владелец: {self.__owner}, Баланс: {self._balance} рублей."


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект BankAccount из словаря.

        :param data: словарь с ключами "owner" и "init_balance".
        :return: Новый объект BankAccount.
        """
        return cls(owner=data["owner"], init_balance=data["init_balance"])

    
class SavingAccount(BankAccount):
    """
    Сберегательный счет - наследник BankAccount.
    Добавляет процентную ставку и ограничение на снятие (не более 50% за операцию).
    """
    def __init__(self, owner, init_balance, bet):
        """
        Инициализирует сберегательный счёт.

        :param owner: Имя владельца счета.
        :param init_balance: Начальный баланс.
        :param bet: Процентная ставка (% годовых).
        :raises ValueError: Если параметры некорректны.
        """
        super().__init__(owner, init_balance)
        self.__bet = None
        self.bet = bet 


    @property
    def bet(self):
        """
        Возвращает процентную ставку.
        """
        return self.__bet

    @bet.setter
    def bet(self, value):
        """
        Устанавливает процентную ставку.

        :param value: Ставка в процентах.
        :raises ValueError: Если ставка некорректна.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Ставка должна быть числом.")
        if value < 0:
            raise ValueError("Ставка должна быть неотрицательной.")
        self.__bet = value


    def add_procent(self):
        """
        Начисляет проценты на текущий баланс.

        :raises ValueError: Если ставка не установлена.
        """
        procent = self.balance * (self.__bet / 100)
        self._balance += procent
        self._history.append(f"Начисление процентов: +{procent} рублей. Баланс: {self.balance} рублей.")
        print(f"Начислено {procent} рублей ({self.__bet}%). Текущий баланс: {self.balance} рублей.")


    def withdrawal(self, summa):
        """
        Снимает сумму со счета: не более 50% баланс.

        :param summa: Сумма снятия.
        :raises ValueError: Если сумма некорректна или превышает 50% баланса.
        """
        try:
            summa = float(summa)
        except (ValueError, TypeError):
            raise ValueError("Сумма должна быть числом.")
        if summa <= 0:
            raise ValueError("Сумма снятия должна быть больше 0.")
        if summa > self.balance * 0.5:
            raise ValueError(f"Со сберегательного счёта нельзя снять больше 50% от баланса. Максимум: {self.balance * 0.5} рублей.")
        if summa > self.balance:
            raise ValueError(f"Недостаточно средств. Доступно: {self.balance} рублей.")
        self._balance -= summa
        self._history.append(f"Снятие со счёта: {summa} рублей. Баланс: {self.balance} рублей.")
        print(f"Со счёта снято {summa} рублей. Текущий баланс: {self.balance} рублей.")

    def __str__(self):
        """
        Возвращает строку с информацию о сберегательном счете.
        """
        return f"{super().__str__()}, Ставка: {self.__bet}%"


if __name__ == '__main__':
    print("\n Через конструктор:")
    account = BankAccount(owner="Акакий", init_balance=15000)
    saving = SavingAccount(owner="Акакий", init_balance= 15000, bet=12)
    print(account)
    print(saving)

    print("\n Через from_dict")
    data = {"owner": "Мария", "init_balance": 1000000}
    account_from_dict = BankAccount.from_dict(data)
    print(f"Счет из словаря: {account_from_dict}")

    print("\n Корректные операции:")
    account.deposit(550)
    account.withdrawal(1000)
    saving.deposit(5)
    saving.withdrawal(4000)

    print("\n Ошибки операций: \n Попытка пополнить на отрицательную сумму:")
    try:
        account.deposit(-125)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n Попытка снять больше, чем есть на счете:")
    try:
        account.withdrawal(20000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n Попытка снять со сберегательного счета больше 50%:")
    try:
        saving.withdrawal(10000)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n Попытка изменить баланс счета напрямую:")
    try:
        account.balance = 125000
    except AttributeError as e:
        print(f"Ошибка: {e}")
    print(f"Баланс после попытки изменения: {account.balance}")

    print("\n История операций:")
    print("\n История обычного счета:")
    for action in account.history:
        print("-", action)

    print("\n История сберегательного счета:")
    for action in saving.history:
        print("-", action)

    print("Начисление процентов:")
    saving.add_procent()

    print("Снятие денег")
    accounts = (account, saving)
    for acc in accounts:
        print(f"Попытка снять 5000 рублей со счёта {acc.owner}:")
        try:
            acc.withdrawal(5000)
        except ValueError as e:
            print(f"Ошибка: {e}")

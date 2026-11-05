#!/usr/bin/env python3
class BankAccount:
    """
    Банковский счёт с владельцем, балансом и историей операций.
    """

    def __init__(self, owner: str) -> None:
        """
        Открывает пустой счёт на имя владельца.

        :param owner: Имя владельца, непустая строка
        """
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Имя владельца должно быть непустой строкой, "
                             + "получено " + repr(owner))
        self.__owner = owner.strip()
        self.__balance = 0
        self.__history = []

    @staticmethod
    def check_amount(amount: int) -> int:
        """
        Проверяет, что сумма операции целая и больше нуля.

        :param amount: Проверяемая сумма
        :return: Та же сумма, если она прошла проверку
        """
        if (not isinstance(amount, int) or isinstance(amount, bool)
                or amount <= 0):
            raise ValueError("Сумма должна быть целым числом больше нуля, "
                             + "получено " + repr(amount))
        return amount

    @property
    def owner(self) -> str:
        """
        Имя владельца.

        :return: Владелец
        """
        return self.__owner

    @property
    def balance(self) -> int:
        """
        Текущий баланс в рублях.

        :return: Баланс
        """
        return self.__balance

    def get_history(self) -> list[str]:
        """
        Возвращает копию истории операций.

        :return: Новый список строк, по одной на успешную операцию
        """
        return list(self.__history)

    def _record(self, delta: int, text: str) -> None:
        """
        Меняет баланс и записывает операцию в историю.

        :param delta: Изменение баланса, положительное или отрицательное
        :param text: Описание операции без указания баланса
        :return: Ничего не возвращает (None)
        """
        self.__balance += delta
        self.__history.append(text + ", баланс " + str(self.__balance))

    def deposit(self, amount: int) -> None:
        """
        Пополняет счёт.

        :param amount: Сумма пополнения, целое число больше нуля
        :return: Ничего не возвращает (None)
        """
        self.check_amount(amount)
        self._record(amount, "Пополнение " + str(amount))

    def withdraw(self, amount: int) -> None:
        """
        Снимает деньги со счёта, если их хватает.

        :param amount: Сумма снятия, целое число больше нуля
        :return: Ничего не возвращает (None)
        """
        self.check_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостаточно средств: на счёте "
                             + str(self.__balance) + ", запрошено "
                             + str(amount))
        self._record(-amount, "Снятие " + str(amount))

    @classmethod
    def open_account(cls, owner: str, start_balance: int) -> "BankAccount":
        """
        Открывает счёт и сразу кладёт на него начальную сумму.

        :param owner: Имя владельца
        :param start_balance: Начальная сумма, целое число больше нуля
        :return: Новый счёт с записью о пополнении в истории
        """
        account = cls(owner)
        account.deposit(start_balance)
        return account


class SavingsAccount(BankAccount):
    """
    Сберегательный счёт с процентной ставкой и лимитом на снятие.
    """

    def __init__(self, owner: str, rate: int) -> None:
        """
        Открывает сберегательный счёт со ставкой в процентах годовых.

        :param owner: Имя владельца
        :param rate: Ставка в процентах, целое число от 1 до 100
        """
        super().__init__(owner)
        if not isinstance(rate, int) or isinstance(rate, bool):
            raise ValueError("Ставка должна быть целым числом, получено "
                             + repr(rate))
        if rate < 1 or rate > 100:
            raise ValueError("Ставка должна быть от 1 до 100 процентов, "
                             + "получено " + str(rate))
        self.__rate = rate

    @property
    def rate(self) -> int:
        """
        Ставка в процентах.

        :return: Ставка
        """
        return self.__rate

    def add_interest(self) -> int:
        """
        Начисляет проценты на текущий баланс.

        :return: Начисленная сумма, целая часть от баланса умножить на
            ставку и разделить на 100
        """
        interest = self.balance * self.__rate // 100
        if interest > 0:
            self._record(interest, "Проценты " + str(interest)
                         + " по ставке " + str(self.__rate) + "%")
        return interest

    def withdraw(self, amount: int) -> None:
        """
        Снимает деньги, но не больше половины баланса за одну операцию.

        :param amount: Сумма снятия, целое число больше нуля
        :return: Ничего не возвращает (None)
        """
        self.check_amount(amount)
        if amount * 2 > self.balance:
            raise ValueError("Со сберегательного счёта нельзя снять больше "
                             + "половины баланса за раз: баланс "
                             + str(self.balance) + ", запрошено "
                             + str(amount))
        super().withdraw(amount)

    @classmethod
    def open_account(cls, owner: str, start_balance: int,
                     rate: int = 5) -> "SavingsAccount":
        """
        Открывает сберегательный счёт с начальной суммой и ставкой.

        :param owner: Имя владельца
        :param start_balance: Начальная сумма, целое число больше нуля
        :param rate: Ставка в процентах, по умолчанию 5
        :return: Новый сберегательный счёт
        """
        account = cls(owner, rate)
        account.deposit(start_balance)
        return account


def main() -> None:
    """
    Открывает два счёта и показывает операции и проверки.

    :return: Ничего не возвращает (None)
    """
    account = BankAccount.open_account("Иван", 10000)
    savings = SavingsAccount.open_account("Мария", 10000, 10)
    print("Счёт:", account.owner, account.balance)
    print("Сберегательный счёт:", savings.owner, savings.balance,
          "ставка", savings.rate, "%")
    account.deposit(2500)
    print("После пополнения на 2500:", account.balance)
    account.withdraw(500)
    print("После снятия 500:", account.balance)
    print()
    print("Ошибки операций:")
    for amount in [-100, 0, 100000]:
        try:
            account.withdraw(amount)
        except ValueError as error:
            print("  ValueError:", error)
    try:
        account.deposit(-100)
    except ValueError as error:
        print("  ValueError:", error)
    print()
    print("Попытки изменить баланс напрямую:")
    try:
        account.balance = 1000000
    except AttributeError as error:
        print("  AttributeError:", error)
    account.__balance = 1000000
    print("  после account.__balance = 1000000 баланс равен",
          account.balance)
    history = account.get_history()
    history.append("Подделка")
    print("  в копии истории записей", len(history),
          "в счёте", len(account.get_history()))
    print()
    print("Проценты по сберегательному счёту:", savings.add_interest())
    print("Баланс после процентов:", savings.balance)
    print()
    for item in [account, savings]:
        print("История", item.owner + ":")
        for line in item.get_history():
            print(" ", line)
    print()
    print("Снятие 7000 с обоих счетов:")
    for item in [account, savings]:
        try:
            item.withdraw(7000)
            print(" ", item.owner + ": снято, баланс", item.balance)
        except ValueError as error:
            print(" ", item.owner + ": ValueError:", error)


main()

"""
Модуль для работы с банковскими счетами.
Демонстрирует наследование, инкапсуляцию и полиморфизм.
"""

class BankAccount:
    """Базовый класс банковского счета."""
    def __init__(self, owner, balance=0):
        """Инициализация счета с владельцем и балансом."""
        if balance < 0:
            raise ValueError('Баланс не может быть меньше 0!')
        self.__balance = balance
        self.__owner = owner
        self.__transaction = []

    @property
    def balance(self):
        """Возвращает текущий баланс счета."""
        return self.__balance

    @property
    def owner(self):
        """Возвращает владельца счета."""
        return self.__owner

    @property
    def transaction(self):
        """Возвращает копию истории транзакций."""
        return [d.copy() for d in self.__transaction]

    def increase_amount(self, amount):
        """Пополняет счет на указанную сумму."""
        if amount <= 0:
            raise ValueError('Сумма пополнения не может быть 0 или меньше!')
        self.__balance += amount
        self.__transaction.append({'operation': 'depositing money',
                                   'amount': amount,
                                   'new_balance': self.__balance})

    def decrease_amount(self, amount):
        """Снимает указанную сумму со счета."""
        if amount <= 0:
            raise ValueError('Сумма снятия не может быть 0 или меньше!')
        if amount > self.__balance:
            raise ValueError('Недостаточно средств!')
        self.__balance -= amount
        self.__transaction.append({'operation': 'withdrawing money',
                                   'amount': amount,
                                   'new_balance': self.__balance})

    @classmethod
    def create(cls, owner, balance=0):
        """Создает объект счета через классовый метод."""
        return cls(owner, balance)

class SavingsAccount(BankAccount):
    """Класс сберегательного счета с процентной ставкой."""
    def __init__(self, owner, balance=0, interest_rate=0.05):
        """Инициализация сберегательного счета с процентной ставкой."""
        super().__init__(owner, balance)
        if interest_rate < 0:
            raise ValueError('Процентная ставка не может быть меньше 0!')
        self.__interest_rate = interest_rate

    def interest_accrual(self):
        """Начисляет проценты на текущий баланс."""
        new_amount = self.balance * self.__interest_rate
        if new_amount > 0:
            self.increase_amount(new_amount)

    def decrease_amount(self, amount):
        """Снимает сумму со счета (не более 50% от баланса)."""
        if amount > self.balance * 0.5:
            raise ValueError('Нельзя снять более 50% от текущего баланса!')
        super().decrease_amount(amount)

if __name__ == '__main__':

    print('\nКорректные пополнение и снятие')
    account = BankAccount.create("Alice", 1000)
    print(f"Владелец: {account.owner}, баланс: {account.balance}")

    account.increase_amount(999)
    print(f"Баланс после пополнения на 999: {account.balance}")

    account.decrease_amount(231)
    print(f"Баланс после снятия 231: {account.balance}")

    print('\nОшибки при отрицательной сумме и превышении баланса')
    try:
        account_2 = BankAccount("Маша", -500)
    except ValueError as e:
        print(f"Счёт с балансом -500: {e}")

    try:
        account.increase_amount(-100)
    except ValueError as e:
        print(f"Пополнение счета на -100: {e}")

    try:
        account.decrease_amount(-50)
    except ValueError as e:
        print(f"Снятие со счета -50: {e}")

    try:
        account.decrease_amount(10000000)
    except ValueError as e:
        print(f"Снятие 10000000, когда на счёте только {account.balance}: {e}")

    print('\nНевозможность изменить баланс напрямую')
    print(f"Текущий баланс: {account.balance}")

    try:
        account.balance = 999999
        print(f"Попытка изменения баланса: {account.balance}")
    except AttributeError as e:
        print(f"Попытка изменить balance напрямую: {e}")

    print('\nВывод истории операций')
    account_1 = BankAccount.create("Оля", 1000)
    account_1.increase_amount(500)
    account_1.decrease_amount(200)
    for record in account_1.transaction:
        print(f"История операций: {record['operation']}: {record['amount']} руб. (баланс:{record['new_balance']})")

    print('\nПолиморфное поведение метода снятия денег для обычного и сберегательного счёта')
    bank_account = BankAccount.create("Обычный", 1000)
    savings_account = SavingsAccount("Сберегательный", 1000, interest_rate=0.05)

    print(f"Обычный счёт: {bank_account.balance} руб.")
    print(f"Сберегательный счёт: {savings_account.balance} руб.")
    print("Попытка снять 800 рублей (80% от баланса):")

    try:
        bank_account.decrease_amount(800)
        print(f"Снятие с обычного счета. Баланс: {bank_account.balance}")
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        savings_account.decrease_amount(800)
        print(f"Снятие со сберегательного счета. Баланс: {savings_account.balance}")
    except ValueError as e:
        print(f"Ошибка: {e}")

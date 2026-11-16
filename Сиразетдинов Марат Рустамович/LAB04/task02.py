class BankAccount:
    """
    Базовый класс банковского счёта

    :param owner: имя владельца счёта
    :param balance: начальный баланс счёта
    """

    def __init__(self, owner, balance):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError('Имя владельца должно быть непустой строкой')
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise ValueError('Начальный баланс должен быть числом')
        if balance < 0:
            raise ValueError('Начальный баланс не может быть отрицательным')

        self.__owner = owner.strip()
        self.__balance = float(balance)
        self.__history = []

        if self.__balance > 0:
            self.__history.append(f'Открытие счёта: +{self.__balance} руб.')

    @property
    def owner(self):
        """
        Возвращает имя владельца счёта
        """
        return self.__owner

    @property
    def balance(self):
        """
        Возвращает текущий баланс счёта
        """
        return self.__balance

    @property
    def history(self):
        """
        Возвращает копию истории транзакций
        """
        return self.__history.copy()

    def get_history(self):
        """
        Возвращает независимую копию списка операций по счёту

        :return: копия списка строк с историей транзакций
        """
        return self.__history.copy()

    def _validate_amount(self, amount):
        """
        Проверяет корректность суммы денежной операции

        :param amount: сумма операции
        """
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise ValueError('Сумма операции должна быть числом')
        if amount <= 0:
            raise ValueError('Сумма операции должна быть больше нуля')

    def _update_balance(self, new_balance, record):
        """
        Защищённый метод для обновления баланса и записи в историю

        :param new_balance: новое значение баланса
        :param record: текстовое описание операции
        """
        self.__balance = round(float(new_balance), 2)
        self.__history.append(record)

    def deposit(self, amount):
        """
        Пополняет счёт на указанную сумму

        :param amount: сумма пополнения
        """
        self._validate_amount(amount)
        new_balance = round(self.__balance + amount, 2)
        self._update_balance(
            new_balance,
            f'Пополнение: +{float(amount)} руб. (Баланс: {new_balance} руб.)',
        )

    def withdraw(self, amount):
        """
        Снимает указанную сумму со счёта при достаточном балансе

        :param amount: сумма снятия
        """
        self._validate_amount(amount)
        if amount > self.__balance:
            raise ValueError('Недостаточно средств на счёте')
        new_balance = round(self.__balance - amount, 2)
        self._update_balance(
            new_balance,
            f'Снятие: -{float(amount)} руб. (Баланс: {new_balance} руб.)',
        )

    def get_info(self):
        """
        Возвращает строку с основной информацией о счёте

        :return: строка с описанием счёта
        """
        return (
            f'{self.__class__.__name__}: \n'
            f'Владелец: {self.owner} \n'
            f'Баланс: {self.balance} руб.'
        )

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект BankAccount из словаря

        :param d: словарь с ключами owner и balance
        :return: новый объект BankAccount
        """
        return cls(d['owner'], d['balance'])


class SavingsAccount(BankAccount):
    """
    Дочерний класс для создания сберегательного счёта, наследник BankAccount

    :param owner: имя владельца счёта
    :param balance: начальный баланс счёта
    :param interest_rate: годовая процентная ставка
    """

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        if not isinstance(interest_rate, (int, float)) or isinstance(
            interest_rate, bool
        ):
            raise ValueError('Процентная ставка должна быть числом')
        if interest_rate <= 0:
            raise ValueError('Процентная ставка должна быть больше нуля')
        self.__interest_rate = float(interest_rate)

    @property
    def interest_rate(self):
        """
        Возвращает процентную ставку по счёту
        """
        return self.__interest_rate

    def apply_interest(self):
        """
        Начисляет проценты на текущий баланс счёта

        :return: сумма начисленных процентов
        """
        interest = round(self.balance * (self.__interest_rate / 100), 2)
        if interest > 0:
            new_balance = round(self.balance + interest, 2)
            self._update_balance(
                new_balance,
                f'Начисление процентов ({self.__interest_rate}%): '
                f'+{interest} руб. (Баланс: {new_balance} руб.)',
            )
        return interest

    def withdraw(self, amount):
        """
        Снимает средства со сберегательного счёта

        :param amount: сумма снятия
        """
        self._validate_amount(amount)
        max_allowed = self.balance * 0.5
        if amount > max_allowed:
            raise ValueError(
                f'Нельзя снять более 50% баланса за одну операцию '
                f'(максимум {max_allowed} руб.)'
            )
        super().withdraw(amount)

    def get_info(self):
        """
        Возвращает строку с информацией о сберегательном счёте

        :return: строка с описанием счёта и ставкой
        """
        base_info = super().get_info()
        return f'{base_info} \nСтавка: {self.interest_rate}%'

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект SavingsAccount из словаря

        :param d: словарь с ключами owner, balance и interest_rate
        :return: новый объект SavingsAccount
        """
        return cls(d['owner'], d['balance'], d['interest_rate'])


if __name__ == '__main__':
    print('Создание счетов и операции с ними')
    acc = BankAccount('Семен', 1500)
    sav_acc = SavingsAccount.from_dict({'owner': 'Мария', 'balance': 5000, 'interest_rate': 11})

    acc.deposit(500)
    acc.withdraw(250)
    sav_acc.apply_interest()
    sav_acc.withdraw(1000)

    print(acc.get_info())
    print(sav_acc.get_info())

    print('\nОшибки:')
    try:
        acc.deposit(-200.0)
    except ValueError as err:
        print(f'Ошибка пополнения: {err}')

    try:
        acc.withdraw(4000.0)
    except ValueError as err:
        print(f'Ошибка снятия: {err}')

    print('\nНевозможность изменить баланс, владельца или историю напрямую:')
    try:
        acc.balance = 500000.0
    except AttributeError as err:
        print(f'Мод - много денег не сработал: {err}')

    history_copy = acc.get_history()
    history_copy.append('Фейковая операция')
    print(
        f'Длина оригинала истории: {len(acc.get_history())}, '
        f'копии: {len(history_copy)}'
    )

    print('\nВывод истории операций (обычный счёт):')
    for record in acc.get_history():
        print(f'- {record}')

    print('\nПолиморфное поведение метода withdraw')
    accounts = [BankAccount('Артём', 1800),SavingsAccount('Ольга', 1800, 7.5),]

    for account in accounts:
        try:
            account.withdraw(1200.0)
            print(
                f'{account.__class__.__name__}: снятие прошло успешно. '
                f'Баланс: {account.balance} руб.'
            )
        except ValueError as err:
            print(f'{account.__class__.__name__}: отказ — {err}')

#!/usr/bin/env python3

import random

RETIREMENT_AGE = 65
ADULT_AGE = 18
MONTHS_IN_YEAR = 12

class Person:
    """
    Базовый класс, представляющий человека.
    """

    def __init__(self, name: str, gender: str, age: int):
        """
        Инициализирует человека.

        :param name: Имя человека.
        :param gender: Пол человека.
        :param age: Возраст человека.
        """
        self._name = name
        self._gender = gender
        self._age = 0

        self.age = age

    @property
    def name(self) -> str:
        """
        Свойство для чтения имени.

        :return: Имя человека.
        """
        return self._name

    @property
    def gender(self) -> str:
        """
        Свойство для чтения пола.

        :return: Пол человека.
        """
        return self._gender

    @property
    def age(self) -> int:
        """
        Свойство для чтения возраста.

        :return: Возраст человека.
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """
        Сеттер для возраста с валидацией.

        :param value: Новый возраст.
        :raises ValueError: Если возраст отрицательный.
        """
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = value

    def __str__(self) -> str:
        """
        Формирует строковое представление информации о человеке.

        :return: Строка с базовой информацией.
        """
        return f"{self.name} (Пол: {self.gender}, Возраст: {self.age})"

    def is_adult(self) -> bool:
        """
        Оценивает совершеннолетие человека.

        :return: True, если возраст >= ADULT_AGE, иначе False.
        """
        return self.age >= ADULT_AGE

    @classmethod
    def build_from_dict(cls, data: dict) -> "Person":
        """
        Конструирует персону из словаря.

        :param data: Словарь с данными человека.
        :return: Новый экземпляр Person.
        """
        name = str(data.get("name", "Аноним"))
        gender = str(data.get("gender", "Не указан"))
        age = int(data.get("age", 0))
        return cls(name=name, gender=gender, age=age)


class Employee(Person):
    """
    Класс сотрудника, наследующий Person.
    """

    def __init__(self, name: str, gender: str, age: int, position: str, salary: float, expenses: float):
        """
        Инициализирует сотрудника.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :param position: Должность.
        :param salary: Зарплата.
        :param expenses: Расходы в месяц.
        """
        super().__init__(name, gender, age)
        self._position = position
        self._salary = 0.0
        self._expenses = 0.0
        self._is_alive = True

        self.salary = salary
        self.expenses = expenses

        self._check_survival()

    @property
    def position(self) -> str:
        """
        Свойство для чтения должности.

        :return: Должность сотрудника.
        """
        return self._position

    @property
    def is_alive(self) -> bool:
        """
        Свойство для проверки статуса жизни сотрудника.

        :return: True, если жив, иначе False.
        """
        return self._is_alive

    @property
    def salary(self) -> float:
        """
        Свойство для чтения зарплаты.

        :return: Текущая зарплата сотрудника.
        """
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """
        Сеттер для зарплаты с валидацией.

        :param value: Новое значение зарплаты.
        :raises ValueError: Если зарплата отрицательная.
        """
        if value < 0:
            raise ValueError("Ошибка! Зарплата не может быть отрицательной!")
        self._salary = value

    @property
    def expenses(self) -> float:
        """
        Свойство для чтения расходов.

        :return: Текущие расходы сотрудника.
        """
        return self._expenses

    @expenses.setter
    def expenses(self, value: float) -> None:
        """
        Сеттер для расходов с валидацией.

        :param value: Новое значение расходов.
        :raises ValueError: Если расходы отрицательные.
        """
        if value < 0:
            raise ValueError("Ошибка! Расходы не могут быть отрицательными!")
        self._expenses = value

    def _check_survival(self) -> None:
        """
        Проверяет выживаемость сотрудника на основе его финансов.
        Если расходы превышают доходы, сотрудник "умирает".
        """
        if self.expenses > self.salary:
            self._is_alive = False
            print(f"ТРАГЕДИЯ: {self.name} тратил больше, чем зарабатывал, и умер от долгов!")

    def work(self) -> str:
        """
        Абстрактный метод работы. Должен быть переопределен в наследниках.

        :raises NotImplementedError: Если метод не переопределен.
        :return: Строка с описанием работы.
        """
        raise NotImplementedError("Этот метод должны реализовать дочерние классы!")

    def calc_profit(self, months: int) -> float:
        """
        Оценивает приток денег за указанное количество месяцев.

        :param months: Количество месяцев для расчета.
        :return: Сумма накоплений за это время.
        """
        if not self.is_alive:
            return 0.0
        return (self.salary - self.expenses) * months

    def calc_retirement_savings(self) -> float:
        """
        Рассчитывает, сколько человек скопит до пенсии.

        :return: Сумма накоплений до пенсии.
        """
        if not self.is_alive or self.age >= RETIREMENT_AGE:
            return 0.0
        months_left = (RETIREMENT_AGE - self.age) * MONTHS_IN_YEAR
        return self.calc_profit(months_left)

    def __str__(self) -> str:
        """
        Формирует строковое представление информации о сотруднике.

        :return: Строка с данными человека и его финансовым статусом.
        """
        base_info = super().__str__()
        status = "Жив" if self.is_alive else "Мертв"
        return f"[{self.position}] {base_info} | ЗП: {self.salary}, Траты: {self.expenses} | Статус: {status}"


class Manager(Employee):
    """
    Класс менеджера, наследующий Employee.
    """

    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float):
        """
        Инициализирует менеджера.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :param salary: Зарплата.
        :param expenses: Расходы.
        """
        super().__init__(name, gender, age, "Менеджер", salary, expenses)
        self._subordinates = 0

    @property
    def subordinates(self) -> int:
        """
        Свойство для получения количества подчиненных.

        :return: Количество подчиненных.
        """
        return self._subordinates

    def add_worker(self) -> None:
        """
        Увеличивает количество подчиненных менеджера на одного.
        """
        self._subordinates += 1

    def start_meeting(self) -> str:
        """
        Проводит встречу с подчиненными.

        :return: Строка с описанием встречи.
        """
        return f"{self.name} собирает {self.subordinates} подчиненных на встречу."

    def work(self) -> str:
        """
        Реализует рабочий процесс менеджера (проведение митинга).

        :return: Строка с результатом работы.
        """
        return self.start_meeting()

    def __str__(self) -> str:
        """
        Формирует строковое представление информации о менеджере.

        :return: Строка с данными сотрудника и количеством подчиненных.
        """
        return super().__str__() + f" | Подчиненных: {self.subordinates}"


class Developer(Employee):
    """
    Класс разработчика, наследующий Employee.
    """

    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float, languages: list[str]):
        """
        Инициализирует разработчика.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :param salary: Зарплата.
        :param expenses: Расходы.
        :param languages: Список языков программирования.
        """
        super().__init__(name, gender, age, "Разработчик", salary, expenses)
        self._languages = languages

    @property
    def languages(self) -> list[str]:
        """
        Свойство для получения списка языков программирования.

        :return: Список языков.
        """
        return self._languages

    def write_code(self) -> str:
        """
        Имитирует написание кода на случайном языке из списка.

        :return: Строка с описанием процесса написания кода.
        """
        lang = random.choice(self.languages) if self.languages else "псевдокоде"
        return f"{self.name} яростно пишет код на {lang}."

    def work(self) -> str:
        """
        Реализует рабочий процесс разработчика (написание кода).

        :return: Строка с результатом работы.
        """
        return self.write_code()

    def __str__(self) -> str:
        """
        Формирует строковое представление информации о разработчике.

        :return: Строка с данными сотрудника и списком языков.
        """
        return super().__str__() + f" | Языки: {', '.join(self.languages)}"


class Designer(Employee):
    """
    Класс дизайнера, наследующий Employee.
    """

    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float, tools: list[str]):
        """
        Инициализирует дизайнера.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :param salary: Зарплата.
        :param expenses: Расходы.
        :param tools: Список инструментов дизайна.
        """
        super().__init__(name, gender, age, "Дизайнер", salary, expenses)
        self._tools = tools

    @property
    def tools(self) -> list[str]:
        """
        Свойство для получения списка инструментов.

        :return: Список инструментов.
        """
        return self._tools

    def make_layout(self) -> str:
        """
        Имитирует создание макета с использованием случайного инструмента.

        :return: Строка с описанием процесса создания макета.
        """
        tool = random.choice(self.tools) if self.tools else "карандашом"
        return f"{self.name} рисует красивый макет, используя {tool}."

    def work(self) -> str:
        """
        Реализует рабочий процесс дизайнера (создание макета).

        :return: Строка с результатом работы.
        """
        return self.make_layout()

    def __str__(self) -> str:
        """
        Формирует строковое представление информации о дизайнере.

        :return: Строка с данными сотрудника и списком инструментов.
        """
        return super().__str__() + f" | Инструменты: {', '.join(self.tools)}"


if __name__ == '__main__':
    print("1. Создание сотрудников (и смерть от долгов)")
    bankrupt = Developer("Иван", "М", 25, salary=50000, expenses=80000, languages=["Python"])

    manager = Manager("Кукуцаполь", "М", 35, salary=120000, expenses=50000)
    manager.add_worker()
    manager.add_worker()

    dev = Developer("Алексей", "М", 28, salary=150000, expenses=60000, languages=["Python", "C++", "Go"])

    designer = Designer("Жозефина", "Ж", 24, salary=90000, expenses=40000, tools=["Figma", "Photoshop"])

    print("\n2. Полиморфный вызов красивого представления (__str__)")
    team = [bankrupt, manager, dev, designer]
    for worker in team:
        print(worker)

    print("\n3. Полиморфный вызов метода работы (work)")
    for worker in team:
        if worker.is_alive:
            print(worker.work())

    print("\n4. Расчет накоплений до пенсии")
    for worker in team:
        if worker.is_alive:
            savings = worker.calc_retirement_savings()
            print(f"{worker.name} накопит до пенсии ({RETIREMENT_AGE} лет): {savings} руб.")


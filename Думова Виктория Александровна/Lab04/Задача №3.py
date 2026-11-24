#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

MIN_AGE = 0
MAX_AGE = 120
ADULT_AGE = 18
PENSION_AGE = 65
MONTHS_IN_YEAR = 12


class Person:
    """
    Класс человека: имя, пол, возраст с валидацией.

    Attributes:
        _name: имя человека.
        _gender: пол ('м' или 'ж').
        _age: возраст (0..120).
    """

    def __init__(self, name, gender, age):
        """
        Конструктор.

        Args:
            name (str): имя.
            gender (str): 'м' или 'ж'.
            age (int): возраст (0..120).

        Returns:
            None

        Raises:
            ValueError: при некорректных значениях.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        if gender not in ("м", "ж"):
            raise ValueError("Пол должен быть 'м' или 'ж'")
        if type(age) is not int or not (MIN_AGE <= age <= MAX_AGE):
            raise ValueError("Возраст должен быть целым 0..120")
        self._name = name
        self._gender = gender
        self._age = age

    @property
    def name(self):
        """
        Свойство только для чтения: имя.

        Args:
            None

        Returns:
            str: имя.
        """
        return self._name

    @property
    def gender(self):
        """
        Свойство только для чтения: пол.

        Args:
            None

        Returns:
            str: 'м' или 'ж'.
        """
        return self._gender

    @property
    def age(self):
        """
        Свойство только для чтения: возраст.

        Args:
            None

        Returns:
            int: возраст.
        """
        return self._age

    def is_adult(self):
        """
        Проверяет совершеннолетие.

        Args:
            None

        Returns:
            bool: True если age >= 18.
        """
        return self.age >= ADULT_AGE

    @classmethod
    def from_variables(cls, name, gender, age):
        """
        Классовый метод создания Person из переменных.

        Args:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.

        Returns:
            Person: новый объект.
        """
        return cls(name, gender, age)

    def __str__(self):
        """
        Строковое представление человека.

        Args:
            None

        Returns:
            str: строка с информацией о человеке.
        """
        return f"Человек: {self.name}, пол: {self.gender}, возраст: {self.age}"


class Employee(Person, ABC):
    """
    Сотрудник: расширяет Person должностью, зарплатой и расходами.
    Абстрактный класс (нельзя создать напрямую).

    Attributes:
        _position: должность.
        _salary: зарплата в месяц.
        _monthly_expenses: средние расходы в месяц.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Конструктор.

        Args:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.
            position (str): должность.
            salary (int | float): зарплата в месяц.
            monthly_expenses (int | float): средние расходы в месяц.

        Returns:
            None

        Raises:
            ValueError: при некорректных значениях.
        """
        super().__init__(name, gender, age)
        if not isinstance(position, str) or not position.strip():
            raise ValueError("Должность должна быть непустой строкой. Иди работай.")
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Зарплата должна быть положительной")
        if not isinstance(monthly_expenses, (int, float)) or monthly_expenses < 0:
            raise ValueError("Расходы не могут быть отрицательными. Вы не в утопии !")
        self._position = position
        self._salary = salary
        self._monthly_expenses = monthly_expenses
        if self._monthly_expenses > self._salary:
            raise ValueError("Какая жалость, вы умерли. Сотрудник не может тратить больше, чем зарабатывает.")

    @property
    def position(self):
        """
        Свойство только для чтения: должность.

        Args:
            None

        Returns:
            str: должность.
        """
        return self._position

    @property
    def salary(self):
        """
        Свойство только для чтения: зарплата.

        Args:
            None

        Returns:
            int | float: зарплата.
        """
        return self._salary

    @property
    def monthly_expenses(self):
        """
        Свойство только для чтения: расходы.

        Args:
            None

        Returns:
            int | float: расходы.
        """
        return self._monthly_expenses

    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы. Должен быть реализован в наследниках.

        Args:
            None

        Returns:
            str: описание работы.
        """
        pass

    def income_after_months(self, months):
        """
        Приток денег за N месяцев (доходы минус расходы).

        Args:
            months (int): количество месяцев.

        Returns:
            int | float: накопленная сумма.
        """
        return (self.salary - self.monthly_expenses) * months

    def money_until_pension(self, pension_age=PENSION_AGE):
        """
        Сколько накопится до пенсии.

        Args:
            pension_age (int): пенсионный возраст (по умолчанию 65).

        Returns:
            int | float: накопленная сумма.
        """
        months = (pension_age - self.age) * MONTHS_IN_YEAR
        if months < 0:
            return 0
        return self.income_after_months(months)

    def __str__(self):
        """
        Строковое представление сотрудника.

        Args:
            None

        Returns:
            str: строка с информацией.
        """
        return (f"{super().__str__()}, должность: {self.position}, "
                f"зарплата: {self.salary}, расходы: {self.monthly_expenses}")


class Manager(Employee):
    """
    Менеджер с подчинёнными.

    Attributes:
        _subordinates: список подчинённых.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, subordinates=None):
        """
        Конструктор.

        Args:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.
            position (str): должность.
            salary (int | float): зарплата.
            monthly_expenses (int | float): расходы.
            subordinates (list[str] | None): список подчинённых.

        Returns:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._subordinates = subordinates if subordinates else []

    @property
    def subordinates(self):
        """
        Свойство только для чтения: список подчинённых (кортеж).

        Args:
            None

        Returns:
            tuple[str]: кортеж подчинённых.
        """
        return tuple(self._subordinates)

    def add_subordinate(self, name):
        """
        Добавляет подчинённого.

        Args:
            name (str): имя подчинённого.

        Returns:
            None
        """
        self._subordinates.append(name)

    def remove_subordinate(self, name):
        """
        Удаляет подчинённого, если он есть.

        Args:
            name (str): имя подчинённого.

        Returns:
            None
        """
        if name in self._subordinates:
            self._subordinates.remove(name)

    def work(self):
        """
        Работа менеджера.

        Args:
            None

        Returns:
            str: описание.
        """
        return "Управляю командой и провожу митинги"

    def conduct_meeting(self):
        """
        Проводит митинг для подчинённых.

        Args:
            None

        Returns:
            str: описание митинга.
        """
        subs = ', '.join(self.subordinates) if self.subordinates else 'пусто'
        return f"Митинг для: {subs}"

    def __str__(self):
        """
        Строковое представление менеджера.

        Args:
            None

        Returns:
            str: строка с информацией.
        """
        return f"{super().__str__()}, подчинённые: {list(self.subordinates)}"


class Developer(Employee):
    """
    Разработчик с языками программирования.

    Attributes:
        _languages: список языков программирования.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages=None):
        """
        Конструктор.

        Args:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.
            position (str): должность.
            salary (int | float): зарплата.
            monthly_expenses (int | float): расходы.
            languages (list[str] | None): языки программирования.

        Returns:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._languages = languages if languages else []

    @property
    def languages(self):
        """
        Свойство только для чтения: языки (кортеж).

        Args:
            None

        Returns:
            tuple[str]: кортеж языков.
        """
        return tuple(self._languages)

    def work(self):
        """
        Работа разработчика.

        Args:
            None

        Returns:
            str: описание.
        """
        return "Пишу код"

    def write_code(self):
        """
        Пишет код на случайном языке.

        Args:
            None

        Returns:
            str: описание действия.

        Raises:
            ValueError: если список языков пуст.
        """
        if not self._languages:
            raise ValueError("Нет языков для написания кода")
        lang = random.choice(self._languages)
        return f"Пишу код на {lang}"

    def __str__(self):
        """
        Строковое представление разработчика.

        Args:
            None

        Returns:
            str: строка с информацией.
        """
        return f"{super().__str__()}, языки: {list(self.languages)}"


class Designer(Employee):
    """
    Дизайнер с инструментами.

    Attributes:
        _tools: список инструментов.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools=None):
        """
        Конструктор.

        Args:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.
            position (str): должность.
            salary (int | float): зарплата.
            monthly_expenses (int | float): расходы.
            tools (list[str] | None): инструменты.

        Returns:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._tools = tools if tools else []

    @property
    def tools(self):
        """
        Свойство только для чтения: инструменты (кортеж).

        Args:
            None

        Returns:
            tuple[str]: кортеж инструментов.
        """
        return tuple(self._tools)

    def work(self):
        """
        Работа дизайнера.

        Args:
            None

        Returns:
            str: описание.
        """
        return "Рисую макеты"

    def __str__(self):
        """
        Строковое представление дизайнера.

        Args:
            None

        Returns:
            str: строка с информацией.
        """
        return f"{super().__str__()}, инструменты: {list(self.tools)}"


if __name__ == "__main__":
    print("=" * 50)
    print("Проверка кода на трезвость")
    print("=" * 50)

    print("\n--- Тест 1: Person ---")
    person = Person.from_variables("Виктория", "ж", 19)
    print(person)
    print("Совершеннолетний?", person.is_adult())

    print("\n--- Тест 2: Ошибки валидации Person ---")
    try:
        Person("", "ж", 19)
    except ValueError as e:
        print("Ошибка имени:", e)
    try:
        Person("Виктория", "x", 19)
    except ValueError as e:
        print("Ошибка пола:", e)
    try:
        Person("Виктория", "ж", 190)
    except ValueError as e:
        print("Ошибка возраста:", e)

    print("\n--- Тест 3: Manager ---")
    manager = Manager("Виктория", "ж", 19, "Руководитель", 120000, 50000,
                      ["Александра", "Мария", "Евгения"])
    print(manager)
    print("Работа:", manager.work())
    print("Митинг:", manager.conduct_meeting())
    print("Доход за 6 месяцев:", manager.income_after_months(6))
    print("До пенсии накопится:", manager.money_until_pension())

    print("\n--- Тест 4: Developer ---")
    dev = Developer("Дмитрий", "м", 28, "Python-разработчик", 90000, 40000,
                    ["Python", "JavaScript", "SQL"])
    print(dev)
    print("Работа:", dev.work())
    print("Пишу код:", dev.write_code())

    print("\n--- Тест 5: Designer ---")
    designer = Designer("Виктория", "ж", 19, "UI/UX дизайнер", 80000, 35000,
                        ["Figma", "Photoshop", "Illustrator"])
    print(designer)
    print("Работа:", designer.work())

    print("\n--- Тест 6: Полиморфизм ---")
    employees = [manager, dev, designer]
    for emp in employees:
        print(f"{emp.name}: {emp.work()}")

    print("\n--- Тест 7: Кортеж подчинённых ---")
    print("Подчинённые (кортеж):", manager.subordinates)
    print("Тип:", type(manager.subordinates).__name__)
    manager.add_subordinate("Новый сотрудник")
    print("После добавления:", manager.subordinates)
    manager.remove_subordinate("Новый сотрудник")
    print("После удаления:", manager.subordinates)

    print("\n--- Тест 8: Кортеж языков ---")
    print("Языки (кортеж):", dev.languages)
    print("Тип:", type(dev.languages).__name__)

    print("\n--- Тест 9: Кортеж инструментов ---")
    print("Инструменты (кортеж):", designer.tools)
    print("Тип:", type(designer.tools).__name__)

    print("\n--- Тест 10: Ошибки Employee ---")
    try:
        Developer("Тест", "м", 25, "Разработчик", 50000, 60000)
    except ValueError as e:
        print("Ошибка расходов:", e)

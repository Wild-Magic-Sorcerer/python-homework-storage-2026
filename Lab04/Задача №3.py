#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

class Person:
    """
    Класс человека: имя, пол, возраст с валидацией.
    """
    def __init__(self, name, gender, age):
        """
        Конструктор.
        Параметры:
            name (str): имя.
            gender (str): 'м' или 'ж'.
            age (int): возраст (0..120).
        Возвращает:
            None
        Исключения:
            ValueError: при некорректных значениях.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        if gender not in ("м", "ж"):
            raise ValueError("Пол должен быть 'м' или 'ж'")
        if not isinstance(age, int) or not (0 <= age <= 120):
            raise ValueError("Возраст должен быть целым 0..120")
        self.__name = name
        self.__gender = gender
        self.__age = age

    @property
    def name(self):
        """
        Свойство только для чтения: имя.
        Параметры:
            Нет.
        Возвращает:
            str: имя.
        """
        return self.__name

    @property
    def gender(self):
        """
        Свойство только для чтения: пол.
        Параметры:
            Нет.
        Возвращает:
            str: 'м' или 'ж'.
        """
        return self.__gender

    @property
    def age(self):
        """
        Свойство только для чтения: возраст.
        Параметры:
            Нет.
        Возвращает:
            int: возраст.
        """
        return self.__age

    def introduce(self):
        """
        Красивое представление человека.
        Параметры:
            Нет.
        Возвращает:
            str: строка с информацией о человеке.
        """
        return f"Человек: {self.name}, пол: {self.gender}, возраст: {self.age}"

    def is_adult(self):
        """
        Проверяет совершеннолетие.
        Параметры:
            Нет.
        Возвращает:
            bool: True если age >= 18.
        """
        return self.age >= 18

    @classmethod
    def from_variables(cls, name, gender, age):
        """
        Классовый метод создания Person из переменных.
        Параметры:
            name (str): имя.
            gender (str): пол.
            age (int): возраст.
        Возвращает:
            Person: новый объект.
        """
        return cls(name, gender, age)

class Employee(Person, ABC):
    """
    Сотрудник: расширяет Person должностью, зарплатой и расходами.
    Абстрактный класс (нельзя создать напрямую).
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Конструктор.
        Параметры:
            name (str), gender (str), age (int): как у Person.
            position (str): должность.
            salary (int | float): зарплата в месяц.
            monthly_expenses (int | float): средние расходы в месяц.
        Возвращает:
            None
        Исключения:
            ValueError: при некорректных значениях.
        """
        super().__init__(name, gender, age)
        if not isinstance(position, str) or not position.strip():
            raise ValueError("Должность должна быть непустой строкой")
        if not isinstance(salary, (int, float)) or salary <= 0:
            raise ValueError("Зарплата должна быть положительной")
        if not isinstance(monthly_expenses, (int, float)) or monthly_expenses < 0:
            raise ValueError("Расходы не могут быть отрицательными")
        self.__position = position
        self.__salary = salary
        self.__monthly_expenses = monthly_expenses
        if self.__monthly_expenses > self.__salary:
            raise ValueError("Сотрудник не может тратить больше, чем зарабатывает (умер)")

    @property
    def position(self):
        """
        Свойство только для чтения: должность.
        Параметры:
            Нет.
        Возвращает:
            str: должность.
        """
        return self.__position

    @property
    def salary(self):
        """
        Свойство только для чтения: зарплата.
        Параметры:
            Нет.
        Возвращает:
            int | float: зарплата.
        """
        return self.__salary

    @property
    def monthly_expenses(self):
        """
        Свойство только для чтения: расходы.
        Параметры:
            Нет.
        Возвращает:
            int | float: расходы.
        """
        return self.__monthly_expenses

    def introduce(self):
        """
        Красивое представление сотрудника (использует super()).
        Параметры:
            Нет.
        Возвращает:
            str: строка с информацией.
        """
        return (f"{super().introduce()}, должность: {self.position}, "
                f"зарплата: {self.salary}, расходы: {self.monthly_expenses}")

    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы. Должен быть реализован в наследниках.
        Параметры:
            Нет.
        Возвращает:
            str: описание работы.
        """
        pass

    def income_after_months(self, months):
        """
        Приток денег за N месяцев (доходы минус расходы).
        Параметры:
            months (int): количество месяцев.
        Возвращает:
            int | float: накопленная сумма.
        """
        return (self.salary - self.monthly_expenses) * months

    def money_until_pension(self, pension_age=65):
        """
        Сколько накопится до пенсии.
        Параметры:
            pension_age (int): пенсионный возраст (по умолчанию 65).
        Возвращает:
            int | float: накопленная сумма.
        """
        months = (pension_age - self.age) * 12
        if months < 0:
            return 0
        return self.income_after_months(months)

class Manager(Employee):
    """
    Менеджер с подчинёнными.
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses, subordinates=None):
        """
        Конструктор.
        Параметры:
            ... (как у Employee)
            subordinates (list[str]): список имён подчинённых.
        Возвращает:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__subordinates = subordinates if subordinates else []

    @property
    def subordinates(self):
        """
        Свойство только для чтения: список подчинённых (копия).
        Параметры:
            Нет.
        Возвращает:
            list[str]: копия списка.
        """
        return list(self.__subordinates)

    def add_subordinate(self, name):
        """
        Добавляет подчинённого.
        Параметры:
            name (str): имя подчинённого.
        Возвращает:
            None
        """
        self.__subordinates.append(name)

    def remove_subordinate(self, name):
        """
        Удаляет подчинённого, если он есть.
        Параметры:
            name (str): имя подчинённого.
        Возвращает:
            None
        """
        if name in self.__subordinates:
            self.__subordinates.remove(name)

    def introduce(self):
        """
        Красивое представление менеджера (super()).
        Параметры:
            Нет.
        Возвращает:
            str: строка с информацией.
        """
        return f"{super().introduce()}, подчинённые: {self.subordinates}"

    def work(self):
        """
        Работа менеджера.
        Параметры:
            Нет.
        Возвращает:
            str: описание.
        """
        return "Управляю командой и провожу митинги"

    def conduct_meeting(self):
        """
        Проводит митинг для подчинённых.
        Параметры:
            Нет.
        Возвращает:
            str: описание митинга.
        """
        return f"Митинг для: {', '.join(self.subordinates) if self.subordinates else 'пусто'}"

class Developer(Employee):
    """
    Разработчик с языками программирования.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages=None):
        """
        Конструктор.
        Параметры:
            ... (как у Employee)
            languages (list[str]): языки программирования.
        Возвращает:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__languages = languages if languages else []

    @property
    def languages(self):
        """
        Свойство только для чтения: языки (копия).
        Параметры:
            Нет.
        Возвращает:
            list[str]: копия списка языков.
        """
        return list(self.__languages)

    def introduce(self):
        """
        Красивое представление разработчика.
        Параметры:
            Нет.
        Возвращает:
            str: строка с информацией.
        """
        return f"{super().introduce()}, языки: {self.languages}"

    def work(self):
        """
        Работа разработчика.
        Параметры:
            Нет.
        Возвращает:
            str: описание.
        """
        return "Пишу код"

    def write_code(self):
        """
        Пишет код на случайном языке.
        Параметры:
            Нет.
        Возвращает:
            str: описание действия.
        Исключения:
            ValueError: если список языков пуст.
        """
        if not self.__languages:
            raise ValueError("Нет языков для написания кода")
        lang = random.choice(self.__languages)
        return f"Пишу код на {lang}"

class Designer(Employee):
    """
    Дизайнер с инструментами.
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools=None):
        """
        Конструктор.
        Параметры:
            ... (как у Employee)
            tools (list[str]): инструменты.
        Возвращает:
            None
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__tools = tools if tools else []

    @property
    def tools(self):
        """
        Свойство только для чтения: инструменты (копия).
        Параметры:
            Нет.
        Возвращает:
            list[str]: копия списка инструментов.
        """
        return list(self.__tools)

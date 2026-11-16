#!/usr/bin/env python3

import math
import random


class Person:
    """
    Базовый класс 
    """

    def __init__(self, name, gender, age):
        """
        Конструктор класса

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой!")

        if gender not in ("мужской", "женский"):
            raise ValueError("Некорректно указан пол!")

        if isinstance(age, bool) or not isinstance(age, int) or age < 0:
            raise ValueError("Возраст не может быть отрицательным числом или дробным!")

        self.__name = name.strip()
        self.__gender = gender
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @classmethod
    def from_data(cls, name, gender, age):
        """
        Создание объекта через переданные данные

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :return: объект класса
        """
        return cls(name, gender, age)

    def info(self):
        """
        Вывод информации о человеке

        :return: информация о человеке
        """
        return (
            f"Имя: {self.name}\n"
            f"Пол: {self.gender}\n"
            f"Возраст: {self.age}"
        )

    def is_adult(self):
        """
        Проверка совершеннолетия

        :return: True, если человеку есть 18 лет
        """
        return self.age >= 18


class Employee(Person):
    """
    Класс сотрудника, наследуемый от Person
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        """
        Конструктор класса

        :param name: имя сотрудника
        :param gender: пол сотрудника
        :param age: возраст сотрудника
        :param position: должность
        :param salary: зарплата
        :param expenses: ежемесячные расходы
        """
        super().__init__(name, gender, age)

        if not isinstance(position, str) or not position.strip():
            raise ValueError("Должность должна быть непустой строкой!")

        self.__position = position.strip()
        self.__salary = self._check_money(salary)
        self.__expenses = self._check_money(expenses)

    @staticmethod
    def _check_money(value):
        """
        Проверка денежного значения

        :param value: денежное значение
        :return: проверенное значение
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом!")

        if not math.isfinite(value) or value < 0:
            raise ValueError("Значение должно быть неотрицательным!")

        return value

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    @property
    def expenses(self):
        return self.__expenses

    @property
    def is_alive(self):
        """
        Проверка, хватает ли зарплаты на расходы

        :return: True, если зарплата не меньше расходов
        """
        return self.salary >= self.expenses

    def info(self):
        """
        Вывод информации о сотруднике

        :return: информация о сотруднике
        """
        return (
            f"{super().info()}\n"
            f"Должность: {self.position}\n"
            f"Зарплата: {self.salary}\n"
            f"Ежемесячные расходы: {self.expenses}\n"
            f"Состояние: {'Жив' if self.is_alive else 'Мёртв'}"
        )

    def work(self):
        """
        Общее действие сотрудника

        :return: описание работы
        """
        return f"{self.name} выполняет свою работу."

    def income_for_months(self, months):
        """
        Расчёт дохода за указанное количество месяцев

        :param months: количество месяцев
        :return: доход за указанный период
        """
        if isinstance(months, bool) or not isinstance(months, int) or months < 0:
            raise ValueError("Количество месяцев должно быть неотрицательным целым числом!")

        if not self.is_alive:
            return 0

        return self.salary * months

    def savings_until_retirement(self, retirement_age=65):
        """
        Расчёт накоплений до выхода на пенсию

        :param retirement_age: возраст выхода на пенсию
        :return: сумма накоплений
        """
        if isinstance(retirement_age, bool) or not isinstance(retirement_age, int):
            raise TypeError("Возраст выхода на пенсию должен быть целым числом!")

        if retirement_age < self.age:
            raise ValueError("Возраст выхода на пенсию не может быть меньше текущего!")

        if not self.is_alive:
            return 0

        months = (retirement_age - self.age) * 12
        return (self.salary - self.expenses) * months


class Manager(Employee):
    """
    Класс менеджера
    """

    def __init__(self, name, gender, age, salary, expenses):
        """
        Конструктор класса

        :param name: имя менеджера
        :param gender: пол менеджера
        :param age: возраст менеджера
        :param salary: зарплата
        :param expenses: ежемесячные расходы
        """
        super().__init__(
            name, gender, age,
            "Менеджер", salary, expenses
        )
        self.__subordinates = []

    @property
    def subordinates(self):
        return self.__subordinates.copy()

    def add_subordinate(self, employee):
        """
        Добавление подчинённого

        :param employee: сотрудник
        """
        if not isinstance(employee, Employee):
            raise TypeError("Подчинённый должен быть сотрудником!")

        self.__subordinates.append(employee)

    def remove_subordinate(self, employee):
        """
        Удаление подчинённого

        :param employee: сотрудник
        """
        if employee in self.__subordinates:
            self.__subordinates.remove(employee)

    def hold_meeting(self):
        """
        Проведение собрания с подчинёнными

        :return: результат собрания
        """
        if not self.__subordinates:
            return f"{self.name} проводит собрание, но подчинённых пока нет"

        return (
            f"{self.name} проводит собрание "
            f"Количество участников: {len(self.__subordinates)}"
        )

    def work(self):
        return self.hold_meeting()

    def info(self):
        """
        Информация о менеджере

        :return: информация о менеджере
        """
        return (
            f"{super().info()}\n"
            f"Количество подчинённых: {len(self.__subordinates)}"
        )


class Developer(Employee):
    """
    Класс разработчика
    """

    def __init__(self, name, gender, age, salary, expenses, languages):
        """
        Конструктор класса

        :param name: имя разработчика
        :param gender: пол разработчика
        :param age: возраст разработчика
        :param salary: зарплата
        :param expenses: ежемесячные расходы
        :param languages: список языков программирования
        """
        super().__init__(
            name, gender, age,
            "Разработчик", salary, expenses
        )

        if not isinstance(languages, list) or not languages:
            raise ValueError("Необходимо указать список языков программирования!")

        if not all(isinstance(lang, str) and lang.strip() for lang in languages):
            raise ValueError("Все языки должны быть строками!")

        self.__languages = languages.copy()

    @property
    def languages(self):
        return self.__languages.copy()

    def write_code(self):
        """
        Написание кода на случайном языке программирования

        :return: описание действия
        """
        language = random.choice(self.__languages)
        return f"{self.name} пишет код на языке {language}."

    def work(self):
        return self.write_code()

    def info(self):
        """
        Информация о разработчике

        :return: информация о разработчике
        """
        return (
            f"{super().info()}\n"
            f"Языки программирования: {', '.join(self.__languages)}"
        )


class Designer(Employee):
    """
    Класс дизайнера
    """

    def __init__(self, name, gender, age, salary, expenses, tools):
        """
        Конструктор класса.

        :param name: имя дизайнера
        :param gender: пол дизайнера
        :param age: возраст дизайнера
        :param salary: зарплата
        :param expenses: ежемесячные расходы
        :param tools: список инструментов
        """
        super().__init__(
            name, gender, age,
            "Дизайнер", salary, expenses
        )

        if not isinstance(tools, list) or not tools:
            raise ValueError("Необходимо указать список инструментов!")

        if not all(isinstance(tool, str) and tool.strip() for tool in tools):
            raise ValueError("Все инструменты должны быть строками!")

        self.__tools = tools.copy()

    @property
    def tools(self):
        return self.__tools.copy()

    def create_layout(self):
        """
        Создание макета с помощью случайного инструмента

        :return: описание действия
        """
        tool = random.choice(self.__tools)
        return f"{self.name} создаёт макет с помощью {tool}"

    def work(self):
        return self.create_layout()

    def info(self):
        """
        Информация о дизайнере

        :return: информация о дизайнере
        """
        return (
            f"{super().info()}\n"
            f"Инструменты: {', '.join(self.__tools)}"
        )


# Основная часть программы
if __name__ == "__main__":

    # Создание человека через classmethod
    person = Person.from_data("Анна", "женский", 21)

    print("Информация о человеке")
    print(person.info())
    print("Совершеннолетний:", person.is_adult())

    print("Создание новых сотрудников")

    manager = Manager(
        "Павел", "мужской", 40,
        150000, 50000
    )

    developer = Developer(
        "Евгений", "мужской", 30,
        190000, 60000,
        ["Python", "Java", "C++"]
    )

    designer = Designer(
        "Елена", "женский", 27,
        100000, 35000,
        ["Figma", "Photoshop", "Illustrator"]
    )

    manager.add_subordinate(developer)
    manager.add_subordinate(designer)

    print("Список подчинённых менеджера:")
    for employee in manager.subordinates:
        print(employee.name)
        print()

    manager.remove_subordinate(designer)

    print("После удаления подчинённого:")
    for employee in manager.subordinates:
        print(employee.name)
        print()

    # Полиморфизм
    employees = [manager, developer, designer]

    print("Инфорация о сотрудниках\n")

    for employee in employees:
        print("--------------------")
        print(employee.info())
        print()

    print("Действия сотрудников")

    for employee in employees:
        print(employee.work())
        print()

    print("Доход за год")

    for employee in employees:
        print(
            f"{employee.name}: "
            f"{employee.income_for_months(12)}"
        )

    print("\nНакопления до пенсии")

    for employee in employees:
        print(
            f"{employee.name}: "
            f"{employee.savings_until_retirement()}"
        )

    # Проверка ситуации, когда расходы больше зарплаты
    print("\nПроверка расходов")

    poor_employee = Employee(
        "Валера", "мужской", 35,
        "Сотрудник", 30000, 50000
    )

    print(poor_employee.info())
    print("Доход за 12 месяцев:", poor_employee.income_for_months(12))
    print("Накопления:", poor_employee.savings_until_retirement())
#!/usr/bin/env python3
# Задание 3 — Person / Employee / Manager / Developer / Designer
import random
from abc import ABC, abstractmethod

MIN_AGE, MAX_AGE = 16, 100
RETIREMENT_AGE = 65
GENDERS = {"м", "ж", "мужской", "женский"}


class Person(ABC):
    """
    Класс человека.

    :param name: имя человека
    :param gender: пол человека
    :param age: возраст человека
    """
    def __init__(self, name, gender, age):
        self.name = name; self.gender = gender; self.age = age

    @property
    def name(self):
        """
        Возвращает имя человека.
        """
        return self.__name

    @name.setter
    def name(self, v):
        """
        Устанавливает имя с проверкой на пустоту.

        :param v: имя человека
        """
        if not isinstance(v, str) or not v.strip():
            print("Имя не может быть пустым"); return
        self.__name = v.strip()

    @property
    def gender(self):
        """
        Возвращает пол человека.
        """
        return self.__gender

    @gender.setter
    def gender(self, v):
        """
        Устанавливает пол с проверкой допустимых значений.

        :param v: пол человека
        """
        if not isinstance(v, str) or v.strip().lower() not in GENDERS:
            print(f"Пол должен быть из {GENDERS}"); return
        self.__gender = v.strip().lower()

    @property
    def age(self):
        """
        Возвращает возраст человека.
        """
        return self.__age

    @age.setter
    def age(self, v):
        """
        Устанавливает возраст с проверкой диапазона MIN_AGE..MAX_AGE.

        :param v: возраст человека
        """
        try:
            v = int(v)
        except (TypeError, ValueError):
            print("Возраст — целое число"); return
        if not MIN_AGE <= v <= MAX_AGE:
            print(f"Возраст от {MIN_AGE} до {MAX_AGE}"); return
        self.__age = v

    def get_info(self):
        """
        Возвращает строку с информацией о человеке.

        :return: строка с описанием
        """
        return f"Имя: {self.__name}, Пол: {self.__gender}, Возраст: {self.__age}"

    def is_adult(self):
        """
        Проверяет совершеннолетие.

        :return: True, если возраст >= 18
        """
        return self.__age >= 18

    @classmethod
    def create_person(cls, name, gender, age):
        """
        Создаёт объект Person через переменные.

        :param name: имя
        :param gender: пол
        :param age: возраст
        :return: новый объект Person
        """
        return cls(name, gender, age)


class Employee(Person):
    """
    Класс сотрудника — наследник Person.

    :param name: имя сотрудника
    :param gender: пол сотрудника
    :param age: возраст сотрудника
    :param position: должность
    :param salary: зарплата
    :param expenses: расходы в месяц
    """
    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age)
        self.position = position; self.salary = salary; self.expenses = expenses

    @property
    def position(self):
        """
        Возвращает должность сотрудника.
        """
        return self.__position

    @position.setter
    def position(self, v):
        """
        Устанавливает должность с проверкой на пустоту.

        :param v: должность
        """
        if not isinstance(v, str) or not v.strip():
            print("Должность не может быть пустой"); return
        self.__position = v.strip()

    @property
    def salary(self):
        """
        Возвращает зарплату сотрудника.
        """
        return self.__salary

    @salary.setter
    def salary(self, v):
        """
        Устанавливает зарплату с проверкой положительности.

        :param v: зарплата
        """
        try:
            v = float(v)
        except (TypeError, ValueError):
            print("Зарплата — число"); return
        if v <= 0:
            print("Зарплата должна быть > 0"); return
        self.__salary = v

    @property
    def expenses(self):
        """
        Возвращает расходы в месяц.
        """
        return self.__expenses

    @expenses.setter
    def expenses(self, v):
        """
        Устанавливает расходы с проверкой неотрицательности.

        :param v: расходы
        """
        try:
            v = float(v)
        except (TypeError, ValueError):
            print("Расходы — число"); return
        if v < 0:
            print("Расходы не могут быть отрицательными"); return
        self.__expenses = v

    def get_info(self):
        """
        Возвращает строку с информацией о сотруднике.

        :return: строка с описанием
        """
        return (f"{super().get_info()}, Должность: {self.__position}, "
                f"Зарплата: {self.__salary} руб., Расходы: {self.__expenses} руб./мес.")

    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы.
        """
        ...

    def income_for_months(self, months):
        """
        Оценивает приток денег за N месяцев.

        :param months: количество месяцев
        :return: сумма притока
        """
        try:
            months = int(months)
        except (TypeError, ValueError):
            print("Месяцы — целое число"); return 0
        if months <= 0:
            print("Месяцы > 0"); return 0
        return (self.__salary - self.__expenses) * months

    def savings_until_retirement(self):
        """
        Рассчитывает накопления до пенсии.

        :return: сумма накоплений
        """
        years = RETIREMENT_AGE - self.age
        if years <= 0:
            print(f"{self.name} уже на пенсии"); return 0
        monthly = self.__salary - self.__expenses
        if monthly <= 0:
            print(f"{self.name} не копит"); return 0
        return monthly * 12 * years

    def check_survival(self, months):
        """
        Симулирует жизнь сотрудника на N месяцев.

        :param months: количество месяцев
        """
        try:
            months = int(months)
        except (TypeError, ValueError):
            print("Месяцы — целое число"); return
        if months <= 0:
            print("Месяцы > 0"); return
        balance = 0
        print(f"Симуляция {self.name} на {months} мес.")
        for m in range(1, months + 1):
            balance += self.__salary - self.__expenses
            print(f"  Месяц {m}: {balance} руб.")
            if balance < 0:
                print(f"{self.name} умер на {m}-м месяце(("); return
        print(f"{self.name} выжил. Итог: {balance} руб.")


class Manager(Employee):
    """
    Менеджер — наследник Employee.

    :param name: имя менеджера
    :param gender: пол менеджера
    :param age: возраст менеджера
    :param position: должность
    :param salary: зарплата
    :param expenses: расходы
    """
    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__subs = []

    def add_subordinate(self, emp):
        """
        Добавляет подчинённого.

        :param emp: объект сотрудника
        """
        self.__subs.append(emp); print(f"{emp.name} → подчинённый {self.name}")

    def remove_subordinate(self, emp):
        """
        Удаляет подчинённого.

        :param emp: объект сотрудника
        """
        if emp in self.__subs:
            self.__subs.remove(emp); print(f"{emp.name} удалён из подчинения")
        else:
            print(f"{emp.name} не подчинённый {self.name}")

    def hold_meeting(self):
        """
        Проводит митинг для подчинённых.
        """
        if not self.__subs:
            print(f"{self.name}: митинг без подчинённых"); return
        print(f"{self.name} ведёт митинг ({len(self.__subs)} чел.):")
        for s in self.__subs:
            print(f"  - {s.name} ({s.position})")

    def get_info(self):
        """
        Возвращает строку с информацией о менеджере.

        :return: строка с описанием
        """
        return f"{super().get_info()}, Подчинённых: {len(self.__subs)}"

    def work(self):
        """
        Менеджер управляет командой.
        """
        print(f"{self.name} управляет {len(self.__subs)} подчинёнными")


class Developer(Employee):
    """
    Разработчик — наследник Employee.

    :param name: имя разработчика
    :param gender: пол разработчика
    :param age: возраст разработчика
    :param position: должность
    :param salary: зарплата
    :param expenses: расходы
    :param languages: список языков программирования
    """
    def __init__(self, name, gender, age, position, salary, expenses, languages):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__langs = languages

    def write_code(self):
        """
        Пишет код на случайном языке из списка.
        """
        if not self.__langs:
            print(f"{self.name} не знает языков"); return
        print(f"{self.name} пишет на {random.choice(self.__langs)}")

    def get_info(self):
        """
        Возвращает строку с информацией о разработчике.

        :return: строка с описанием
        """
        return f"{super().get_info()}, Языки: {', '.join(self.__langs)}"

    def work(self):
        """
        Разработчик пишет код.
        """
        self.write_code()


class Designer(Employee):
    """
    Дизайнер — наследник Employee.

    :param name: имя дизайнера
    :param gender: пол дизайнера
    :param age: возраст дизайнера
    :param position: должность
    :param salary: зарплата
    :param expenses: расходы
    :param tools: список инструментов
    """
    def __init__(self, name, gender, age, position, salary, expenses, tools):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__tools = tools

    def create_mockup(self):
        """
        Создаёт макет с использованием случайного инструмента.
        """
        if not self.__tools:
            print(f"{self.name} без инструментов"); return
        print(f"{self.name} рисует макет в {random.choice(self.__tools)}")

    def get_info(self):
        """
        Возвращает строку с информацией о дизайнере.

        :return: строка с описанием
        """
        return f"{super().get_info()}, Инструменты: {', '.join(self.__tools)}"

    def work(self):
        """
        Дизайнер создаёт макеты.
        """
        self.create_mockup()


if __name__ == "__main__":
    print("Конструкторы:")
    manager = Manager("Алексей", "мужской", 34, "Руководитель", 180000, 110000)
    developer = Developer("Ирина", "женский", 29, "Программист", 140000, 90000,
                          ["Python", "Go", "Rust"])
    designer = Designer("Олег", "мужской", 26, "UI/UX", 110000, 85000,
                        ["Figma", "Sketch", "Blender"])
    for e in (manager, developer, designer):
        print(e.get_info())

    print("\ncreate_person:")
    print(Person.create_person("Светлана", "женский", 22).get_info())

    print("\nСовершеннолетие:")
    print(f"{manager.name}: {manager.is_adult()}")
    print(f"{developer.name}: {developer.is_adult()}")

    print("\nПодчинённые:")
    manager.add_subordinate(developer)
    manager.add_subordinate(designer)
    manager.hold_meeting()

    print("\nПолиморфизм get_info:")
    staff = [manager, developer, designer]
    for e in staff:
        print("-", e.get_info())

    print("\nПолиморфизм work:")
    for e in staff:
        e.work()

    print("\nДоход за 4 мес.:")
    for e in staff:
        print(f"- {e.name}: {e.income_for_months(4)} руб.")

    print("\nНакопления до пенсии:")
    for e in staff:
        print(f"- {e.name}: {e.savings_until_retirement()} руб.")

    print("\nСимуляция 5 мес.:")
    manager.check_survival(5)

    print("\nСтажёр с дефицитом:")
    Manager("Студент", "мужской", 19, "Стажёр", 25000, 35000).check_survival(5)

    print("\nВалидация:")
    print("Возраст 150:")
    Developer("Тест", "мужской", 150, "Тест", 50000, 0, ["Python"])
    print("Пол 'робот':")
    Developer("Тест", "робот", 25, "Тест", 50000, 0, ["Python"])
    print("Зарплата -500:")
    Designer("Тест", "женский", 50, "Тест", -500, 0, ["Paint"])
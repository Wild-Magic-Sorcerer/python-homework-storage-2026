#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

adult_age = 18
pension_age = 65


class Person:
    """Человек."""

    def __init__(self, name, gender, age):
        """Инициализация данных человека."""
        if not name:
            raise ValueError("имя не может быть пустым")
        if gender not in ["м", "ж"]:
            raise ValueError("пол должен быть 'м' или 'ж'")
        if age < 0:
            raise ValueError("возраст не может быть отрицательным")
        self.name = name
        self.gender = gender
        self.age = age

    def get_info(self):
        """Возвращает информацию о человеке."""
        return f"{self.name}, пол: {self.gender}, возраст: {self.age}"

    def is_adult(self):
        """Проверяет совершеннолетие."""
        return self.age >= adult_age

    @classmethod
    def from_vars(cls, name, gender, age):
        """Создает человека из переменных."""
        return cls(name, gender, age)


class Employee(Person, ABC):
    """Сотрудник."""

    def __init__(self, name, gender, age, position, salary, expenses):
        """Инициализация сотрудника с валидацией всех полей."""
        super().__init__(name, gender, age)
        if not position:
            raise ValueError("должность не может быть пустой")
        if salary < 0 or expenses < 0:
            raise ValueError("зарплата и расходы не могут быть отрицательными")
        self.position = position
        self.salary = salary
        self.expenses = expenses
        self._is_alive = True

    def get_info(self):
        """Возвращает расширенную информацию о сотруднике."""
        return f"{super().get_info()}, должность: {self.position}, зарплата: {self.salary}"

    def get_money_flow(self, months):
        """Считает приток денег за n месяцев."""
        return (self.salary - self.expenses) * months

    def check_alive(self):
        """Проверяет, жив ли сотрудник."""
        if self.expenses > self.salary:
            self._is_alive = False
            print(f"сотрудник {self.name} умер из-за долгов.")
        return self._is_alive

    def calculate_pension_savings(self):
        """Считает накопления до пенсии."""
        months_to_pension = (pension_age - self.age) * 12
        return self.get_money_flow(months_to_pension) if months_to_pension > 0 else 0

    @abstractmethod
    def work(self):
        """Абстрактный метод работы."""
        pass


class Manager(Employee):
    """Менеджер (директор)."""

    def __init__(self, name, gender, age, position, salary, expenses, subordinates):
        super().__init__(name, gender, age, position, salary, expenses)
        self.subordinates = subordinates

    def get_info(self):
        """Возвращает информацию о менеджере."""
        return f"{super().get_info()}, подчинённых: {len(self.subordinates)}"

    def work(self):
        """Имитация работы менеджера."""
        return f"менеджер {self.name} подписывает документы."

    def hire(self, person):
        """Добавляет подчиненного."""
        self.subordinates.append(person)

    def fire(self):
        """Увольняет последнего подчиненного."""
        if self.subordinates:
            self.subordinates.pop()

    def meeting(self):
        """Проводит митинг."""
        return f"митинг.. {self.name} собрал {len(self.subordinates)} подчинённых."


class Developer(Employee):
    """Разработчик."""

    def __init__(self, name, gender, age, position, salary, expenses, languages):
        super().__init__(name, gender, age, position, salary, expenses)
        self.languages = languages

    def get_info(self):
        """Возвращает информацию о разработчике."""
        return f"{super().get_info()}, языки: {', '.join(self.languages)}"

    def work(self):
        """Имитация работы разработчика."""
        lang = random.choice(self.languages) if self.languages else "Python"
        return f"разработчик {self.name} пишет код на {lang}."


class Designer(Employee):
    """Дизайнер."""

    def __init__(self, name, gender, age, position, salary, expenses, tools):
        super().__init__(name, gender, age, position, salary, expenses)
        self.tools = tools

    def get_info(self):
        """Возвращает информацию о дизайнере."""
        return f"{super().get_info()}, инструменты: {', '.join(self.tools)}"

    def work(self):
        """Имитация работы дизайнера."""
        return f"дизайнер {self.name} работает с инструментами: {', '.join(self.tools)}."

    def create_mockup(self):
        """Создает макет."""
        tool = self.tools[0] if self.tools else "Figma"
        return f"дизайнер {self.name} создал макет в {tool}."


if __name__ == "__main__":
    menedzher = Manager("Евгений", "м", 60, "Директор", 120000, 60000, ["Иван", "Мария"])
    razrabotchik = Developer("Марина", "ж", 50, "Разработчик", 80000, 40000, ["Python", "C++"])
    dizayner = Designer("Александр", "м", 40, "Дизайнер", 70000, 50000, ["Figma", "Photoshop"])

    print("проверка валидации")
    try:
        Manager("Тест", "м", 30, "", 50000, 30000, [])
    except ValueError as oshibka:
        print(f"ошибка: {oshibka}")

    workers = [menedzher, razrabotchik, dizayner]

    print("информация о сотрудниках")
    for sotrudnik in workers:
        print(sotrudnik.get_info())

    print("работа (полиморфизм)")
    for sotrudnik in workers:
        print(sotrudnik.work())

    print("создание макета")
    print(dizayner.create_mockup())

    print("работа менеджера")
    menedzher.hire("Новый сотрудник")
    print(menedzher.meeting())
    menedzher.fire()

    print("проверка на смерть")
    bednyak = Developer("Василий", "м", 30, "Junior", 30000, 50000, ["Python"])
    bednyak.check_alive()

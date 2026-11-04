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
        """Инициализация сотрудника."""
        super().__init__(name, gender, age)
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


class Director(Employee):
    """Директор школы."""

    def __init__(self, name, gender, age, position, salary, expenses, subordinates):
        super().__init__(name, gender, age, position, salary, expenses)
        self.subordinates = subordinates

    def get_info(self):
        """Возвращает информацию о директоре."""
        return f"{super().get_info()}, подчинённых: {len(self.subordinates)}"

    def work(self):
        """Имитация работы директора."""
        return f"директор {self.name} подписывает документы."

    def hire(self, person):
        """Добавляет подчиненного."""
        self.subordinates.append(person)

    def fire(self):
        """Увольняет последнего подчиненного."""
        if self.subordinates:
            self.subordinates.pop()

    def meeting(self):
        """Проводит педсовет."""
        return f"педсовет! {self.name} собрал {len(self.subordinates)} учителей."


class EnglishTeacher(Employee):
    """Учитель английского языка."""

    def __init__(self, name, gender, age, position, salary, expenses, languages):
        super().__init__(name, gender, age, position, salary, expenses)
        self.languages = languages

    def get_info(self):
        """Возвращает информацию об учителе английского."""
        return f"{super().get_info()}, знает языки: {', '.join(self.languages)}"

    def work(self):
        """Имитация работы учителя."""
        lang = random.choice(self.languages) if self.languages else "English"
        return f"учитель {self.name} ведет урок на {lang}."


class SecurityGuard(Employee):
    """Охранник школы."""

    def __init__(self, name, gender, age, position, salary, expenses, equipment):
        super().__init__(name, gender, age, position, salary, expenses)
        self.equipment = equipment

    def get_info(self):
        """Возвращает информацию об охраннике."""
        return f"{super().get_info()}, имеет при себе: {self.equipment}"

    def work(self):
        """Имитация работы охранника."""
        return f"охранник {self.name} обходит здание с {self.equipment}."


class PE_Teacher(Employee):
    """Учитель физкультуры."""

    def __init__(self, name, gender, age, position, salary, expenses, sport_tools):
        super().__init__(name, gender, age, position, salary, expenses)
        self.sport_tools = sport_tools

    def get_info(self):
        """Возвращает информацию об учителе физкультуры."""
        return f"{super().get_info()}, использует инвентарь: {', '.join(self.sport_tools)}"

    def work(self):
        """Имитация работы учителя физкультуры."""
        tool = self.sport_tools[0] if self.sport_tools else "свисток"
        return f"учитель физкультуры {self.name} проводит разминку с {tool}."


if __name__ == "__main__":
    direktor = Director("Евгений", "м", 60, "Директор", 120000, 60000, ["Иван", "Мария"])
    anglichanin = EnglishTeacher("Марина", "ж", 50, "Учитель английского", 80000, 40000, ["English", "Russian"])
    ohranik = SecurityGuard("Александр", "м", 50, "Охранник", 40000, 30000, "рация")
    fizra = PE_Teacher("Алла", "ж", 40, "Учитель физкультуры", 70000, 60000, ["мяч", "свисток"])

    workers = [direktor, anglichanin, ohranik, fizra]

    print("информация о сотрудниках")
    for sotrudnik in workers:
        print(sotrudnik.get_info())

    print("работа (полиморфизм)")
    for sotrudnik in workers:
        print(sotrudnik.work())

    print("проверка на смерть")
    bednyak = SecurityGuard("Василий", "м", 40, "Охранник", 30000, 50000, "фонарик")
    bednyak.check_alive()

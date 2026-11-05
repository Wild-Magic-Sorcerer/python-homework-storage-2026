#!/usr/bin/env python3

import random

RETIREMENT_AGE = 65

class Person:
    def __init__(self, name: str, gender: str, age: int):
        """
        Инициализирует человека.

        Параметры:
        name — имя человека.
        gender — пол.
        age — возраст.

        Возвращает:
        None
        """
        self._name = name
        self._gender = gender
        self.age = age

    @property
    def age(self) -> int:
        """
        Свойство для чтения возраста.

        Параметры:
        Нет.

        Возвращает:
        Возраст человека.
        """
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """
        Сеттер для возраста с валидацией.

        Параметры:
        value — новый возраст.

        Возвращает:
        None
        """
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        self._age = value

    def show_info(self) -> str:
        """
        Красиво представляет информацию о человеке.

        Параметры:
        Нет.

        Возвращает:
        Строку с базовой информацией.
        """
        return f"{self._name} (Пол: {self._gender}, Возраст: {self.age})"

    def is_adult(self) -> bool:
        """
        Оценивает совершеннолетие человека.

        Параметры:
        Нет.

        Возвращает:
        True, если возраст >= 18, иначе False.
        """
        return self.age >= 18

    @classmethod
    def build_from_dict(cls, data: dict[str, object]) -> "Person":
        """
        Конструирует персону из словаря.

        Параметры:
        data — словарь с данными человека.

        Возвращает:
        Новый экземпляр Person.
        """
        name = str(data.get("name", "Аноним"))
        gender = str(data.get("gender", "Не указан"))
        age = int(data.get("age", 0))
        return cls(name=name, gender=gender, age=age)


class Employee(Person):
    def __init__(self, name: str, gender: str, age: int, position: str, salary: float, expenses: float):
        """
        Инициализирует сотрудника.

        Параметры:
        name — имя.
        gender — пол.
        age — возраст.
        position — должность.
        salary — зарплата.
        expenses — расходы в месяц.

        Возвращает:
        None
        """
        super().__init__(name, gender, age)
        self._position = position
        self.salary = salary
        self.expenses = expenses
        self.is_alive = True

        self._check_survival()

    @property
    def salary(self) -> float:
        """
        Свойство для чтения зарплаты.

        Параметры:
        Нет.

        Возвращает:
        Текущую зарплату сотрудника.
        """
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """
        Сеттер для зарплаты с валидацией.

        Параметры:
        value — новое значение зарплаты.

        Возвращает:
        None
        """
        if value < 0:
            raise ValueError("Ошибка! Зарплата не может быть отрицательной!")
        self._salary = value

    @property
    def expenses(self) -> float:
        """
        Свойство для чтения расходов.

        Параметры:
        Нет.

        Возвращает:
        Текущие расходы сотрудника.
        """
        return self._expenses

    @expenses.setter
    def expenses(self, value: float) -> None:
        """
        Сеттер для расходов с валидацией.

        Параметры:
        value — новое значение расходов.

        Возвращает:
        None
        """
        if value < 0:
            raise ValueError("Ошибка! Расходы не могут быть отрицательными!")
        self._expenses = value

    def _check_survival(self) -> None:
        """
        Проверяет выживаемость сотрудника на основе его финансов.

        Параметры:
        Нет.

        Возвращает:
        None
        """
        if self.expenses > self.salary:
            self.is_alive = False
            print(f"ТРАГЕДИЯ: {self._name} тратил больше, чем зарабатывал, и умер от долгов!")

    def work(self) -> str:
        """
        Абстрактный метод работы. Должен быть переопределен в наследниках.

        Параметры:
        Нет.

        Возвращает:
        Строку с описанием работы.
        """
        raise NotImplementedError("Этот метод должны реализовать дочерние классы!")

    def calc_profit(self, months: int) -> float:
        """
        Оценивает приток денег за N месяцев.

        Параметры:
        months — количество месяцев.

        Возвращает:
        Сумму накоплений за это время.
        """
        if not self.is_alive:
            return 0.0
        return (self.salary - self.expenses) * months

    def calc_retirement_savings(self) -> float:
        """
        Рассчитывает, сколько человек скопит до пенсии.

        Параметры:
        Нет.

        Возвращает:
        Сумму накоплений до пенсии.
        """
        if not self.is_alive or self.age >= RETIREMENT_AGE:
            return 0.0
        months_left = (RETIREMENT_AGE - self.age) * 12
        return self.calc_profit(months_left)

    def show_info(self) -> str:
        """
        Представляет информацию о сотруднике.

        Параметры:
        Нет.

        Возвращает:
        Строку с данными человека и его финансовым статусом.
        """
        base_info = super().show_info()
        status = "Жив" if self.is_alive else "Мертв"
        return f"[{self._position}] {base_info} | ЗП: {self.salary}, Траты: {self.expenses} | Статус: {status}"


class Manager(Employee):
    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float):
        """
        Инициализирует менеджера.

        Параметры:
        name — имя.
        gender — пол.
        age — возраст.
        salary — зарплата.
        expenses — расходы.

        Возвращает:
        None
        """
        super().__init__(name, gender, age, "Менеджер", salary, expenses)
        self.subordinates = 0

    def add_worker(self) -> None:
        """
        Добавляет одного подчиненного менеджеру.

        Параметры:
        Нет.

        Возвращает:
        None
        """
        self.subordinates += 1

    def start_meeting(self) -> str:
        """
        Проводит встречу с подчиненными.

        Параметры:
        Нет.

        Возвращает:
        Строку с описанием втречи.
        """
        return f"{self._name} собирает {self.subordinates} подчиненных на встречу."

    def work(self) -> str:
        """
        Реализует рабочий процесс менеджера.

        Параметры:
        Нет.

        Возвращает:
        Строку с результатом работы (митингом).
        """
        return self.start_meeting()

    def show_info(self) -> str:
        """
        Красиво представляет информацию о менеджере.

        Параметры:
        Нет.

        Возвращает:
        Строку с данными сотрудника и количеством подчиненных.
        """
        return super().show_info() + f" | Подчиненных: {self.subordinates}"


class Developer(Employee):
    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float, languages: list[str]):
        """Инициализирует разработчика."""
        super().__init__(name, gender, age, "Разработчик", salary, expenses)
        self.languages = languages

    def write_code(self) -> str:
        """Пишет код на случайном языке."""
        lang = random.choice(self.languages) if self.languages else "псевдокоде"
        return f"{self._name} яростно пишет код на {lang}."

    def work(self) -> str:
        """Реализация абстрактного метода работы."""
        return self.write_code()

    def show_info(self) -> str:
        """Добавляет информацию о языках."""
        return super().show_info() + f" | Языки: {', '.join(self.languages)}"

class Designer(Employee):
    def __init__(self, name: str, gender: str, age: int, salary: float, expenses: float, tools: list[str]):
        """Инициализирует дизайнера."""
        super().__init__(name, gender, age, "Дизайнер", salary, expenses)
        self.tools = tools

    def make_layout(self) -> str:
        """Создает макет."""
        tool = random.choice(self.tools) if self.tools else "карандашом"
        return f"{self._name} рисует красивый макет, используя {tool}."

    def work(self) -> str:
        """Реализация абстрактного метода работы."""
        return self.make_layout()

    def show_info(self) -> str:
        """Добавляет информацию об инструментах."""
        return super().show_info() + f" | Инструменты: {', '.join(self.tools)}"


if __name__ == '__main__':
    print("1. Создание сотрудников (и смерть от долгов)")
    bankrupt = Developer("Иван", "М", 25, salary=50000, expenses=80000, languages=["Python"])

    manager = Manager("Кукуцаполь", "М", 35, salary=120000, expenses=50000)
    manager.add_worker()
    manager.add_worker()

    dev = Developer("Алексей", "М", 28, salary=150000, expenses=60000, languages=["Python", "C++", "Go"])

    designer = Designer("Жозефина", "Ж", 24, salary=90000, expenses=40000, tools=["Figma", "Photoshop"])

    print("\n2. Полиморфный вызов красивого представления (show_info)")
    team = [bankrupt, manager, dev, designer]
    for worker in team:
        print(worker.show_info())

    print("\n3. Полиморфный вызов метода работы (work)")
    for worker in team:
        if worker.is_alive:
            print(worker.work())

    print("\n4. Расчет накоплений до пенсии")
    for worker in team:
        if worker.is_alive:
            savings = worker.calc_retirement_savings()
            print(f"{worker._name} накопит до пенсии ({RETIREMENT_AGE} лет): {savings} руб.")


"""
Модуль для управления сотрудниками компании.
Содержит классы Person, Employee и их наследники: Manager, Developer, Designer.
Демонстрирует принципы ООП: наследование, полиморфизм, инкапсуляцию.

Абстрактный метод — это метод, объявленный в базовом классе с помощью декоратора
@abstractmethod из модуля abc без собственной реализации. Он ОБЯЗАН быть
переопределён в каждом классе-наследнике. Используется для задания общего
интерфейса и гарантии того, что все наследники реализуют требуемое поведение,
что обеспечивает полиморфизм.
"""

from abc import ABC, abstractmethod
import random

PENSION = 60

class Person:
    """Базовый класс, представляющий человека с именем, полом и возрастом."""

    def __init__(self, name, gender, age):
        """
        Инициализация человека с валидацией полей.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        """
        self._name = name
        self._gender = gender
        self._age = age

    @property
    def name(self):
        """
        Возвращает имя человека.

        :return: имя человека
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Устанавливает имя с валидацией: должно быть непустой строкой.

        :param value: значение имени
        """
        if not isinstance(value, str):
            raise ValueError('Имя должно быть строкой!')
        if not value.strip():
            raise ValueError('Не вводите пустую строку!')
        self._name = value
        
    @property
    def gender(self):
        """
        Возвращает пол человека.

        :return: пол человека
        """
        return self._gender

    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол с валидацией: 'мужской' или 'женский'.

        :param value: значение пола
        """
        if not isinstance(value, str):
            raise ValueError('Пол должен быть строкой!')
        if value not in ('мужской', 'женский'):
            raise ValueError('Введите пол (мужской/женский)')
        self._gender = value

    @property
    def age(self):
        """
        Возвращает возраст человека.

        :return: возраст человека
        """
        return self._age

    @age.setter
    def age(self, value):
        """
        Устанавливает возраст с валидацией: целое число от 0 до 100.

        :param value: значение возраста
        """
        if not isinstance(value, int):
            raise ValueError('Возраст должен быть целым числом')
        if value < 0 or value > 100:
            raise ValueError('Возраст не может быть меньше 0 или больше 100')
        self._age = value

    def __str__(self):
        """
        Возвращает строковое представление человека.

        :return: строка с информацией о человеке
        """
        return f'Имя человека: {self.name}, пол: {self.gender}, возраст: {self.age}'

    def coming_of_age(self):
        """
        Проверяет совершеннолетие человека (возраст >= 18).

        :return: True, если возраст >= 18, иначе False
        """
        return self.age >= 18

    @classmethod
    def construct_person(cls, name, gender, age):
        """
        Классовый метод для создания объекта Person через переменные.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :return: новый объект класса Person
        """
        return cls(name, gender, age)

class Employee(Person, ABC):
    """Абстрактный класс сотрудника, наследующий Person.
    Добавляет должность, зарплату, расходы и статус жизни."""

    def __init__(self, name, gender, age, position, salary, average_monthly_expenses):
        """
        Инициализация сотрудника с валидацией полей.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :param position: должность сотрудника
        :param salary: зарплата сотрудника
        :param average_monthly_expenses: среднемесячные расходы
        """
        super().__init__(name, gender, age)
        self._position = position
        self._salary = salary
        self._average_monthly_expenses = average_monthly_expenses
        self.__alive = True

    @property
    def position(self):
        """
        Возвращает должность сотрудника.

        :return: должность сотрудника
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Устанавливает должность с валидацией: непустая строка.

        :param value: значение должности
        """
        if not isinstance(value, str):
            raise ValueError('Должность должна быть строкой!')
        if not value.strip():
            raise ValueError('Должность не может быть пустой строкой!')
        self._position = value

    @property
    def salary(self):
        """
        Возвращает зарплату сотрудника.

        :return: зарплата сотрудника
        """
        return self._salary

    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату с валидацией: неотрицательное число.

        :param value: значение зарплаты
        """
        if not isinstance(value, (int, float)):
            raise ValueError('Зарплата должна быть числом!')
        if value < 0:
            raise ValueError('Зарплата не может быть отрицательной!')
        self._salary = value

    @property
    def average_monthly_expenses(self):
        """
        Возвращает среднемесячные расходы сотрудника.

        :return: среднемесячные расходы
        """
        return self._average_monthly_expenses

    @average_monthly_expenses.setter
    def average_monthly_expenses(self, value):
        """
        Устанавливает расходы с валидацией: неотрицательное число.

        :param value: значение расходов
        """
        if not isinstance(value, (int, float)):
            raise ValueError('Расходы должны быть числом!')
        if value < 0:
            raise ValueError('Расходы не могут быть отрицательными!')
        self._average_monthly_expenses = value

    @property
    def alive(self):
        """
        Возвращает статус жизни сотрудника.

        :return: True, если сотрудник жив
        """
        return self.__alive

    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы. Должен быть реализован в наследниках.

        :return: строка с описанием выполняемой работы
        """
        pass

    def die(self):
        """Метод смерти сотрудника при превышении расходов над зарплатой."""
        self.__alive = False
        print(f'{self.name} умер, потому что тратит в месяц больше, чем получает')

    def income(self, months):
        """
        Рассчитывает приток денег за N месяцев.
        Если расходы > зарплаты, сотрудник умирает.

        :param months: количество месяцев
        :return: общий доход за указанный период
        """
        if not self.__alive:
            print(f'{self.name} уже мертв, он не может получать доход')
            return 0

        monthly_profit = self.salary - self.average_monthly_expenses

        if monthly_profit < 0:
            self.die()
            return 0

        total_income = monthly_profit * months
        return total_income

    def accumulation(self):
        """
        Рассчитывает накопления до пенсии (60 лет).
        Учитывает текущий возраст и ежемесячную прибыль.

        :return: общая сумма накоплений до пенсии
        """
        if not self.__alive:
            print(f'{self.name} мертв, накопления невозможны')
            return 0

        if self.age >= PENSION:
            print(f'{self.name} уже на пенсии')
            return 0

        years_to_retirement = PENSION - self.age
        months_to_retirement = years_to_retirement * 12

        monthly_profit = self.salary - self.average_monthly_expenses

        if monthly_profit < 0:
            print(f'{self.name} тратит больше, чем зарабатывает. Накоплений нет')
            self.die()
            return 0

        total_savings = monthly_profit * months_to_retirement
        return total_savings

    def __str__(self):
        """
        Возвращает строковое представление сотрудника.

        :return: строка с информацией о сотруднике
        """
        base_str = super().__str__()
        life_status = 'Жив' if self.__alive else 'Мертв'
        return (f'{base_str}, Должность: {self.position}, зарплата: {self.salary},'
                f'расходы: {self.average_monthly_expenses}, статус: {life_status}')

class Manager(Employee):
    """Класс менеджера с подчинёнными и возможностью проведения митингов."""

    def __init__(self, name, gender, age, position, salary, expenses, subordinates=None):
        """
        Инициализация менеджера со списком подчинённых.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :param position: должность
        :param salary: зарплата
        :param expenses: среднемесячные расходы
        :param subordinates: список подчинённых (по умолчанию пустой)
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.subordinates = subordinates if subordinates else []

    def add_subordinate(self, employee):
        """
        Добавляет сотрудника в список подчинённых.

        :param employee: сотрудник для добавления
        """
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        """
        Удаляет сотрудника из списка подчинённых.

        :param employee: сотрудник для удаления
        """
        self.subordinates.remove(employee)

    def hold_meeting(self):
        """Проводит митинг для всех подчинённых."""
        print(f'{self.name} проводит митинг для {len(self.subordinates)} подчинённых')

    def work(self):
        """
        Реализация метода работы для менеджера.

        :return: строка с описанием работы
        """
        return 'Управляю командой'

    def __str__(self):
        """
        Возвращает строковое представление менеджера.

        :return: строка с информацией о менеджере
        """
        return f'{super().__str__()}, подчинённые: {len(self.subordinates)}'

class Developer(Employee):
    """Класс разработчика со списком языков программирования."""

    def __init__(self, name, gender, age, position, salary, expenses, languages=None):
        """
        Инициализация разработчика со списком языков.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :param position: должность
        :param salary: зарплата
        :param expenses: среднемесячные расходы
        :param languages: список языков программирования (по умолчанию пустой)
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.languages = languages if languages else []

    def write_code(self):
        """Пишет код на случайном языке из списка."""
        if self.languages:
            print(f'{self.name} пишет код на {random.choice(self.languages)}')

    def work(self):
        """
        Реализация метода работы для разработчика.

        :return: строка с описанием работы
        """
        return 'Пишу код'

    def __str__(self):
        """
        Возвращает строковое представление разработчика.

        :return: строка с информацией о разработчике
        """
        return f'{super().__str__()}, языки: {", ".join(self.languages)}'

class Designer(Employee):
    """Класс дизайнера со списком инструментов."""

    def __init__(self, name, gender, age, position, salary, expenses, tools=None):
        """
        Инициализация дизайнера со списком инструментов.

        :param name: имя человека
        :param gender: пол человека
        :param age: возраст человека
        :param position: должность
        :param salary: зарплата
        :param expenses: среднемесячные расходы
        :param tools: список инструментов (по умолчанию пустой)
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.tools = tools if tools else []

    def create_mockup(self):
        """Создаёт макет с использованием инструментов."""
        print(f'{self.name} создаёт макет с помощью {", ".join(self.tools)}')

    def work(self):
        """
        Реализация метода работы для дизайнера.

        :return: строка с описанием работы
        """
        return 'Создаю дизайн'

    def __str__(self):
        """
        Возвращает строковое представление дизайнера.

        :return: строка с информацией о дизайнере
        """
        return f'{super().__str__()}, инструменты: {", ".join(self.tools)}'

if __name__ == '__main__':
    developer1 = Developer("Алексей", "мужской", 28, "Разработчик", 150000, 50000,
                           ["Python", "JavaScript", "Go"])

    developer2 = Developer("Мария", "женский", 25, "Разработчик", 120000, 40000,
                           ["Java", "Kotlin"])

    designer1 = Designer("Ольга", "женский", 30, "Дизайнер", 100000, 35000,
                         ["Figma", "Photoshop", "Illustrator"])

    manager1 = Manager("Иван", "мужской", 35, "Менеджер", 200000, 60000)

    manager1.add_subordinate(developer1)
    manager1.add_subordinate(developer2)
    manager1.add_subordinate(designer1)

    employees = [developer1, developer2, designer1, manager1]

    print("ДЕМОНСТРАЦИЯ ПОЛИМОРФИЗМА")
    print("\nКрасивое представление всех сотрудников:")
    for emp in employees:
        print(emp)

    print("\nПолиморфный вызов метода work():")
    for emp in employees:
        print(f"{emp.name}: {emp.work()}")

    print("\nДополнительные методы:")
    manager1.hold_meeting()

    developer1.write_code()
    developer2.write_code()

    designer1.create_mockup()

    print("\nФинансовые расчёты:")
    print(f"Доход {developer1.name} за 12 месяцев: {developer1.income(12)}")
    print(f"Накопления {developer1.name} до пенсии: {developer1.accumulation()}")

    print("\nПроверка совершеннолетия (метод класса Person):")
    for emp in employees:
        age_status = "совершеннолетний" if emp.coming_of_age() else "несовершеннолетний"
        print(f"{emp.name}: {age_status}")
        

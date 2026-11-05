#!/usr/bin/env python3
import random
from abc import ABC, abstractmethod

GENDERS = ("мужской", "женский")
MAX_AGE = 150
ADULT_AGE = 18
RETIREMENT_AGE = {"мужской": 65, "женский": 60}


def check_text(value: str, name: str) -> str:
    """
    Проверяет, что значение непустая строка.

    :param value: Проверяемое значение
    :param name: Название поля для сообщения об ошибке
    :return: Строка без пробелов по краям
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + ": ожидается непустая строка, получено "
                         + repr(value))
    return value.strip()


def check_int(value: int, name: str, minimum: int, maximum: int) -> int:
    """
    Проверяет, что значение целое число в заданных границах.

    :param value: Проверяемое значение
    :param name: Название поля для сообщения об ошибке
    :param minimum: Наименьшее допустимое значение
    :param maximum: Наибольшее допустимое значение
    :return: То же значение, если оно прошло проверку
    """
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(name + ": ожидается целое число, получено "
                         + repr(value))
    if value < minimum or value > maximum:
        raise ValueError(name + ": ожидается число от " + str(minimum)
                         + " до " + str(maximum) + ", получено "
                         + str(value))
    return value


def years_word(age: int) -> str:
    """
    Подбирает форму слова «год» к числу лет.

    :param age: Число лет
    :return: Слово «год», «года» или «лет»
    """
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        return "года"
    return "лет"


class Person:
    """
    Человек с именем, полом и возрастом.
    """

    def __init__(self, name: str, gender: str, age: int) -> None:
        """
        Создаёт человека, проверяя все три поля.

        :param name: Имя, непустая строка
        :param gender: Пол, одно из значений GENDERS
        :param age: Возраст от 0 до MAX_AGE
        """
        self.__name = check_text(name, "Имя")
        if gender not in GENDERS:
            raise ValueError("Пол: ожидается одно из " + ", ".join(GENDERS)
                             + ", получено " + repr(gender))
        self.__gender = gender
        self.__age = check_int(age, "Возраст", 0, MAX_AGE)

    @property
    def name(self) -> str:
        """
        Имя.

        :return: Имя
        """
        return self.__name

    @property
    def gender(self) -> str:
        """
        Пол.

        :return: Пол
        """
        return self.__gender

    @property
    def age(self) -> int:
        """
        Возраст в годах.

        :return: Возраст
        """
        return self.__age

    def introduce(self) -> str:
        """
        Представляет человека одной строкой.

        :return: Имя, пол и возраст с правильной формой слова «год»
        """
        return (self.__name + ", " + self.__gender + " пол, "
                + str(self.__age) + " " + years_word(self.__age))

    def is_adult(self) -> bool:
        """
        Проверяет совершеннолетие.

        :return: True, если возраст не меньше ADULT_AGE
        """
        return self.__age >= ADULT_AGE

    @classmethod
    def from_values(cls, name: str, gender: str, age: int) -> "Person":
        """
        Создаёт человека из отдельных переменных.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :return: Новый объект того класса, от которого вызван метод
        """
        return cls(name, gender, age)


class Employee(Person, ABC):
    """
    Сотрудник с должностью, зарплатой и расходами, работа у каждого своя.
    """

    def __init__(self, name: str, gender: str, age: int, position: str,
                 salary: int, expenses: int) -> None:
        """
        Создаёт сотрудника, проверяя рабочие поля.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность, непустая строка
        :param salary: Зарплата в месяц, целое число больше нуля
        :param expenses: Средние расходы в месяц, целое число не меньше нуля
        """
        super().__init__(name, gender, age)
        self.__position = check_text(position, "Должность")
        self.__salary = check_int(salary, "Зарплата", 1, 10 ** 9)
        self.__expenses = check_int(expenses, "Расходы", 0, 10 ** 9)

    @property
    def position(self) -> str:
        """
        Должность.

        :return: Должность
        """
        return self.__position

    @property
    def salary(self) -> int:
        """
        Зарплата в месяц.

        :return: Зарплата
        """
        return self.__salary

    @property
    def expenses(self) -> int:
        """
        Средние расходы в месяц.

        :return: Расходы
        """
        return self.__expenses

    def introduce(self) -> str:
        """
        Добавляет к представлению человека рабочие сведения.

        :return: Строка родителя, должность, зарплата и расходы
        """
        return (super().introduce() + ", должность " + self.__position
                + ", зарплата " + str(self.__salary) + ", расходы "
                + str(self.__expenses))

    @abstractmethod
    def work(self) -> str:
        """
        Описывает, что сотрудник делает на работе.

        :return: Строка с описанием работы
        """

    def money_flow(self, months: int) -> int:
        """
        Считает, сколько денег останется за несколько месяцев.

        :param months: Число месяцев, целое число больше нуля
        :return: Разница зарплаты и расходов, умноженная на число месяцев
        """
        check_int(months, "Число месяцев", 1, 1200)
        if self.__expenses > self.__salary:
            raise RuntimeError(self.name + " умер: тратит "
                               + str(self.__expenses)
                               + " в месяц при зарплате "
                               + str(self.__salary))
        return (self.__salary - self.__expenses) * months

    def savings_until_retirement(self) -> int:
        """
        Считает накопления до пенсионного возраста по полу.

        :return: Накопления за оставшиеся месяцы, 0 после пенсии
        """
        months = (RETIREMENT_AGE[self.gender] - self.age) * 12
        if months <= 0:
            return 0
        return self.money_flow(months)

    @classmethod
    def from_values(cls, name: str, gender: str, age: int, position: str,
                    salary: int, expenses: int) -> "Employee":
        """
        Создаёт сотрудника из отдельных переменных.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        :return: Новый объект того класса, от которого вызван метод
        """
        return cls(name, gender, age, position, salary, expenses)


class Manager(Employee):
    """
    Менеджер с подчинёнными и митингами.
    """

    def __init__(self, name: str, gender: str, age: int, position: str,
                 salary: int, expenses: int) -> None:
        """
        Создаёт менеджера без подчинённых.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.__subordinates = []

    @property
    def subordinates(self) -> list[str]:
        """
        Копия списка имён подчинённых.

        :return: Новый список имён
        """
        return list(self.__subordinates)

    def add_subordinate(self, name: str) -> None:
        """
        Добавляет подчинённого.

        :param name: Имя, которого ещё нет в списке
        :return: Ничего не возвращает (None)
        """
        name = check_text(name, "Имя подчинённого")
        if name in self.__subordinates:
            raise ValueError(name + " уже в списке подчинённых")
        self.__subordinates.append(name)

    def remove_subordinate(self, name: str) -> None:
        """
        Убирает подчинённого.

        :param name: Имя из списка подчинённых
        :return: Ничего не возвращает (None)
        """
        if name not in self.__subordinates:
            raise ValueError(name + " не числится подчинённым")
        self.__subordinates.remove(name)

    def hold_meeting(self) -> str:
        """
        Проводит митинг для подчинённых.

        :return: Строка с именами участников или сообщение, что их нет
        """
        if not self.__subordinates:
            return self.name + " хотел провести митинг, но подчинённых нет"
        return (self.name + " проводит митинг для: "
                + ", ".join(self.__subordinates))

    def introduce(self) -> str:
        """
        Добавляет к представлению число подчинённых.

        :return: Строка родителя и число подчинённых
        """
        return (super().introduce() + ", подчинённых "
                + str(len(self.__subordinates)))

    def work(self) -> str:
        """
        Описывает работу менеджера.

        :return: Строка с командой менеджера
        """
        if not self.__subordinates:
            return self.name + " руководит, но команда пока пуста"
        return (self.name + " руководит командой: "
                + ", ".join(self.__subordinates))


class Developer(Employee):
    """
    Разработчик со списком языков программирования.
    """

    def __init__(self, name: str, gender: str, age: int, position: str,
                 salary: int, expenses: int, languages: list[str]) -> None:
        """
        Создаёт разработчика, проверяя список языков.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        :param languages: Непустой список названий языков
        """
        super().__init__(name, gender, age, position, salary, expenses)
        if not languages:
            raise ValueError("Список языков не должен быть пустым")
        self.__languages = [check_text(language, "Язык")
                            for language in languages]

    @property
    def languages(self) -> list[str]:
        """
        Копия списка языков.

        :return: Новый список названий языков
        """
        return list(self.__languages)

    def introduce(self) -> str:
        """
        Добавляет к представлению языки.

        :return: Строка родителя и языки через запятую
        """
        return (super().introduce() + ", языки "
                + ", ".join(self.__languages))

    def work(self) -> str:
        """
        Описывает работу разработчика на случайном языке из списка.

        :return: Строка с выбранным языком
        """
        return self.name + " пишет код на " + random.choice(self.__languages)

    @classmethod
    def from_values(cls, name: str, gender: str, age: int, position: str,
                    salary: int, expenses: int,
                    languages: list[str]) -> "Developer":
        """
        Создаёт разработчика из отдельных переменных.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        :param languages: Список языков
        :return: Новый разработчик
        """
        return cls(name, gender, age, position, salary, expenses, languages)


class Designer(Employee):
    """
    Дизайнер со списком инструментов и макетами.
    """

    def __init__(self, name: str, gender: str, age: int, position: str,
                 salary: int, expenses: int, tools: list[str]) -> None:
        """
        Создаёт дизайнера, проверяя список инструментов.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        :param tools: Непустой список названий инструментов
        """
        super().__init__(name, gender, age, position, salary, expenses)
        if not tools:
            raise ValueError("Список инструментов не должен быть пустым")
        self.__tools = [check_text(tool, "Инструмент") for tool in tools]
        self.__layouts = []

    @property
    def tools(self) -> list[str]:
        """
        Копия списка инструментов.

        :return: Новый список названий инструментов
        """
        return list(self.__tools)

    @property
    def layouts(self) -> list[str]:
        """
        Копия списка названий созданных макетов.

        :return: Новый список названий
        """
        return list(self.__layouts)

    def make_layout(self, title: str) -> str:
        """
        Создаёт макет с названием и запоминает его.

        :param title: Название макета, непустая строка
        :return: Строка о созданном макете и инструменте
        """
        title = check_text(title, "Название макета")
        self.__layouts.append(title)
        return (self.name + " создаёт макет «" + title + "» в "
                + self.__tools[0])

    def introduce(self) -> str:
        """
        Добавляет к представлению инструменты.

        :return: Строка родителя и инструменты через запятую
        """
        return (super().introduce() + ", инструменты "
                + ", ".join(self.__tools))

    def work(self) -> str:
        """
        Описывает работу дизайнера.

        :return: Строка с числом готовых макетов
        """
        return (self.name + " рисует макеты, готово "
                + str(len(self.__layouts)))

    @classmethod
    def from_values(cls, name: str, gender: str, age: int, position: str,
                    salary: int, expenses: int,
                    tools: list[str]) -> "Designer":
        """
        Создаёт дизайнера из отдельных переменных.

        :param name: Имя
        :param gender: Пол
        :param age: Возраст
        :param position: Должность
        :param salary: Зарплата
        :param expenses: Расходы
        :param tools: Список инструментов
        :return: Новый дизайнер
        """
        return cls(name, gender, age, position, salary, expenses, tools)


def main() -> None:
    """
    Создаёт сотрудников разных типов и показывает работу классов.

    :return: Ничего не возвращает (None)
    """
    manager = Manager("Иван Петров", "мужской", 45, "руководитель отдела",
                      150000, 90000)
    manager.add_subordinate("Анна Смирнова")
    manager.add_subordinate("Олег Кузнецов")
    developer = Developer("Анна Смирнова", "женский", 28, "разработчик",
                          120000, 70000, ["Python", "Go", "SQL"])
    designer = Designer.from_values("Олег Кузнецов", "мужской", 33,
                                    "дизайнер", 100000, 60000,
                                    ["Figma", "Photoshop"])
    employees = [manager, developer, designer]
    print("Цепочка наследования Manager:",
          " -> ".join(cls.__name__ for cls in Manager.__mro__))
    print()
    print("Представление, каждая строка собрана через super():")
    for employee in employees:
        print(" ", employee.introduce())
    print()
    print("Работа:")
    for employee in employees:
        print(" ", employee.work())
    print()
    print("Недопустимые значения:")
    try:
        Person("", "мужской", 20)
    except ValueError as error:
        print("  ValueError:", error)
    try:
        Person("Иван", "другой", 20)
    except ValueError as error:
        print("  ValueError:", error)
    try:
        Person("Иван", "мужской", 200)
    except ValueError as error:
        print("  ValueError:", error)
    try:
        Developer("Иван", "мужской", 30, "стажёр", 0, 100, ["Python"])
    except ValueError as error:
        print("  ValueError:", error)
    try:
        Employee("Иван", "мужской", 30, "инженер", 1000, 500)
    except TypeError as error:
        print("  TypeError:", error)
    print()
    name = "Ольга"
    gender = "женский"
    age = 17
    teen = Person.from_values(name, gender, age)
    print(teen.introduce(), "совершеннолетие:", teen.is_adult())
    print(manager.name, "совершеннолетие:", manager.is_adult())
    print()
    print("Приток денег за 12 месяцев:")
    for employee in employees:
        print(" ", employee.name, employee.money_flow(12))
    spender = Developer("Пётр Сидоров", "мужской", 40, "стажёр", 50000,
                        80000, ["JavaScript"])
    try:
        spender.money_flow(6)
    except RuntimeError as error:
        print("  RuntimeError:", error)
    print()
    print("Накопления до пенсии:")
    for employee in employees:
        print(" ", employee.name, employee.savings_until_retirement())
    print()
    print(manager.hold_meeting())
    manager.remove_subordinate("Олег Кузнецов")
    print(manager.hold_meeting())
    print(manager.introduce())
    print(designer.make_layout("Главная страница"))
    print(designer.make_layout("Корзина"))
    print(designer.work())


main()

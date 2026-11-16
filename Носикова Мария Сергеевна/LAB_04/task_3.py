#!/usr/bin/env python3

from abc import ABC, abstractmethod

MIN_AGE = 0
MAX_AGE = 114
RETIREMENT_AGE = 62
GENDERS = ("мужской", "женский")


class Person(ABC):
    """
    Абстрактный класс человека.
    """
    def __init__(self, name, gender, age):
        """
        Инициализирует человека.

        :param name: Имя человека.
        :param gender: Пол человека.
        :param age: Возраст.
        :raises ValueError: Если параметры некорректны.
        """
        self._name = None
        self._gender = None
        self._age = None
        self.name = name
        self.gender = gender
        self.age = age


    @property
    def name(self):
        """
        Возвращает имя человека.
        """
        return self._name


    @name.setter
    def name(self, value):
        """
        Устанавливает имя.
        :param value: Имя человека.
        :raises ValueError: Если имя некорректно.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя не должно быть пустым")
        self._name = value.strip()


    @property
    def gender(self):
        """
        Возвращает пол человека.
        """    
        return self._gender


    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол.

        :param value: Пол человека.
        :raises ValueError: Если пол некорректен.
        """
        if not isinstance(value, str) or value.strip().lower() not in GENDERS:
            raise ValueError(f"Пол должен быть одним из: {GENDERS}")
        self._gender = value.strip().lower()


    @property
    def age(self):
        """
        Возвращает возраст человека.
        """
        return self._age 


    @age.setter
    def age(self, value):
        """
        Устанавливает возраст.

        :param value: Возраст человека.
        :raises ValueError: Если возраст некорректен.
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise ValueError("Возраст должно быть целым числом.")
        if not (MIN_AGE <= value <= MAX_AGE):
            raise ValueError(f"Возраст должен быть в диапазоне от {MIN_AGE} до {MAX_AGE}")
        self._age = value 


    def __str__(self):
        """
        Возвращает строку с информацией о человеке.
        """
        return f"Имя: {self._name}, Пол: {self._gender}, Возраст: {self._age} лет"


    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним.

        :return: True, если возраст >= 18, иначе False.
        """
        return self._age >= 18


    @classmethod
    def create_person(cls, name, gender, age):
        """
        Создаёт объект Person через переменные.

        :param name: Имя.
        :param gender: Пол.
        :param age: Возраст.
        :return: Новый объект Person.
        """
        return cls(name=name, gender=gender, age=age)


class Employee(Person):
    """
    Класс сотрудника — наследник Person.
    Добавляет должность, зарплату и расходы.
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        """
        Инициализирует сотрудника.

        :param name: Имя сотрудника.
        :param gender: Пол сотрудника.
        :param age: Возраст сотрудника.
        :param position: Должность сотрудника.
        :param salary: Зарплата сотрудника.
        :param expenses: Расходы в месяц.
        :raises ValueError: Если параметры некорректны.
        """
        super().__init__(name, gender, age)
        self._position = None
        self._salary = None
        self._expenses = None
        self.position = position
        self.salary = salary
        self.expenses = expenses


    @property
    def position(self):
        """
        Возвращает должность сотрудника.
        """
        return self._position


    @position.setter
    def position(self, value):
        """
        Устанавливает должность.

        :param value: Должность сотрудника.
        :raises ValueError: Если должность некорректна.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Должность должна быть непустой строкой.")
        self._position = value.strip()


    @property
    def salary(self):
        """
        Возвращает зарплату сотрудника.
        """
        return self._salary


    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату с валидацией.

        :param value: Зарплата сотрудника.
        :raises ValueError: Если зарплата некорректна.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Зарплата должна быть числом.")
        if value <= 0:
            raise ValueError("Зарплата должна быть положительным числом.")
        self._salary = value


    @property
    def expenses(self):
        """Возвращает расходы в месяц."""
        return self._expenses


    @expenses.setter
    def expenses(self, value):
        """
        Устанавливает расходы с валидацией.

        :param value: Расходы в месяц.
        :raises ValueError: Если расходы некорректны.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Расходы должны быть числом.")
        if value < 0:
            raise ValueError("Расходы не могут быть отрицательными.")
        self._expenses = value


    def __str__(self):
        """
        Возвращает строку с информацией о сотруднике.
        """
        return f"{super().__str__()}, Должность: {self._position}, Зарплата: {self._salary} руб., Расходы: {self._expenses} руб./мес."


    @abstractmethod
    def work(self):
        """
        Абстрактный метод работы. Должен быть переопределён в наследниках.
        """
        pass


    def income_for_months(self, months):
        """
        Оценивает приток денег за N месяцев.

        :param months: Количество месяцев.
        :return: Сумма притока денег.
        """
        try:
            months = int(months)
        except (ValueError, TypeError):
            raise ValueError("Количество месяцев должно быть целым числом.")
        if months <= 0:
            raise ValueError("Ошибка! Количество месяцев должно быть положительным.")
        return (self._salary - self._expenses) * months


    def savings_until_retirement(self):
        """
        Рассчитывает накопления до пенсии.

        :return: Сумма накоплений.
        """
        years_to_retirement = RETIREMENT_AGE - self.age
        if years_to_retirement <= 0:
            print(f"{self.name} уже достиг пенсионного возраста.")
            return 0
        monthly_savings = self._salary - self._expenses
        if monthly_savings <= 0:
            print(f"{self.name} не может копить: расходы превышают или равны зарплате.")
            return 0
        return monthly_savings * 12 * years_to_retirement


    def check_survival(self, months):
        """
        Симулирует жизнь сотрудника в течение N месяцев.
        Если расходы превышают зарплату, показывает, на каком месяце человек умирает.

        :param months: Количество месяцев.
        """
        try:
            months = int(months)
        except (ValueError, TypeError):
            raise ValueError("Количество месяцев должно быть целым числом.")
        if months <= 0:
            raise ValueError("Количество месяцев должно быть положительным.")
        balance = 0
        print(f"Симуляция жизни {self.name} на {months} месяцев:")
        print(f"Зарплата: {self._salary} руб./мес., Расходы: {self._expenses} руб./мес.")
        for month in range(1, months + 1):
            balance += self._salary - self._expenses
            print(f"Месяц {month}: Баланс = {balance} руб.")

            if balance < 0:
                print(f"{self.name} умер на {month}-м месяце! Не хватило денег((")
                return

        print(f"{self.name} живет нормально! Итоговый баланс: {balance} руб.")

class Manager(Employee):
    """
    Менеджер — наследник Employee. Добавляет список подчинённых.
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        """
        Инициализирует менеджера.

        :param name: Имя менеджера.
        :param gender: Пол менеджера.
        :param age: Возраст менеджера.
        :param position: Должность менеджера.
        :param salary: Зарплата менеджера.
        :param expenses: Расходы менеджера в месяц.
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.__subordinates = []  


    def add_subordinate(self, employee):
        """
        Добавляет подчинённого.

        :param employee: Объект сотрудника.
        """
        self.__subordinates.append(employee)
        print(f"{employee.name} добавлен в подчинение к {self.name}.")


    def remove_subordinate(self, employee):
        """
        Удаляет подчинённого.

        :param employee: Объект сотрудника.
        """
        if employee in self.__subordinates:
            self.__subordinates.remove(employee)
            print(f"{employee.name} удалён из подчинения {self.name}.")
        else:
            print(f"{employee.name} не является подчинённым {self.name}.")  


    def hold_meeting(self):
        """
        Проводит митинг для всех подчинённых.
        """
        if not self.__subordinates:
            print(f"{self.name} проводит митинг, но подчинённых нет.")
            return
        print(f"{self.name} проводит митинг для {len(self.__subordinates)} подчинённых:")
        for sub in self.__subordinates:
            print(f"  - {sub.name} ({sub.position})")

    def __str__(self):
        """
        Возвращает строку с информацией о менеджере.
        """
        return f"{super().__str__()}, Подчинённых: {len(self.__subordinates)}"

    def work(self):
        """
        Менеджер управляет командой.
        """
        print(f"{self.name} управляет командой из {len(self.__subordinates)} человек.")


class Developer(Employee):
    """
    Разработчик — наследник Employee. Добавляет список языков программирования.
    """

    def __init__(self, name, gender, age, position, salary, expenses, languages):
        """
        Инициализирует разработчика.

        :param name: Имя разработчика.
        :param gender: Пол разработчика.
        :param age: Возраст разработчика.
        :param position: Должность разработчика.
        :param salary: Зарплата разработчика.
        :param expenses: Расходы разработчика в месяц.
        :param languages: Список языков программирования.
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.__languages = languages


    def write_code(self):
        """
        Пишет код на случайном языке из списка.
        """
        if not self.__languages:
            print(f"{self.name} не знает ни одного языка программирования.")
            return
        lang = self.__languages[0]
        print(f"{self.name} пишет код на языке {lang}.")


    def __str__(self):
        """
        Возвращает строку с информацией о разработчике.
        """
        return f"{super().__str__()}, Языки: {', '.join(self.__languages)}"


    def work(self):
        """
        Разработчик пишет код.
        """
        self.write_code()


class Designer(Employee):
    """
    Дизайнер — наследник Employee. Добавляет список инструментов.
    """


    def __init__(self, name, gender, age, position, salary, expenses, tools):
        """
        Инициализирует дизайнера.

        :param name: Имя дизайнера.
        :param gender: Пол дизайнера.
        :param age: Возраст дизайнера.
        :param position: Должность дизайнера.
        :param salary: Зарплата дизайнера.
        :param expenses: Расходы дизайнера в месяц.
        :param tools: Список инструментов.
        """
        super().__init__(name, gender, age, position, salary, expenses)
        self.__tools = tools


    def create_mockup(self):
        """
        Создаёт макет с использованием случайного инструмента.
        """
        if not self.__tools:
            print(f"{self.name} не имеет инструментов для работы.")
            return
        tool = self.__tools[0]
        print(f"{self.name} создаёт макет с помощью {tool}.")


    def __str__(self):
        """
        Возвращает строку с информацией о дизайнере.
        """
        return f"{super().__str__()}, Инструменты: {', '.join(self.__tools)}"


    def work(self):
        """
        Дизайнер создаёт макеты.
        """
        self.create_mockup()


if __name__ == '__main__':
    print("\n Создание через конструктор: ")
    manager = Manager(
        name="Михаил",
        gender="мужской",
        age=28,
        position="Менеджер проектов",
        salary=150000,
        expenses=120000
    )
    developer = Developer(
        name="Николай",
        gender="мужской",
        age=36,
        position="Разработчик",
        salary=120000,
        expenses=80000,
        languages=["Python", "С++", "JavaScript"]
    )
    designer = Designer(
        name="Наташа",
        gender="женский",
        age=24,
        position="Дизайнер",
        salary=100000,
        expenses=95000,
        tools=["Figma", "Photoshop", "Illustrator"]
    )
    print(manager)
    print(developer)
    print(designer)

    print("\n Создание через create_person:")
    person = Person.create_person("Марина", "женский", 27)
    print(person)

    print("\n Проверка совершеннолетия: ")
    print(f"{manager.name} совершеннолетний: {manager.is_adult()}")
    print(f"{developer.name} совершеннолетняя: {developer.is_adult()}")

    print("\n Управление подчинёнными: ")
    manager.add_subordinate(developer)
    manager.add_subordinate(designer)

    print("\n Митинг:")
    manager.hold_meeting()

    print("\n Полиморфизм: get_info: ")
    employees = [manager, developer, designer]
    for emp in employees:
        print("-", emp)

    print("Полиморфизм: work: ")
    for emp in employees:
        emp.work()

    print("\n Приток денег за полгода:")
    for emp in employees:
        income = emp.income_for_months(6)
        print(f"- {emp.name}: {income} руб.")

    print("\n Накопления до пенсии: ")
    for emp in employees:
        savings = emp.savings_until_retirement()
        print(f"- {emp.name}: {savings} руб.")

    print("\nСимуляция жизни (6 месяцев):")
    manager.check_survival(6)

    print("\n Проверка выживания: ")
    bad_manager = Manager(
    name="Бедолага студент",
    gender="мужской",
    age=19,
    position="Стажёр",
    salary=30000,
    expenses=40000
    )
    bad_manager.check_survival(6)

    print("\n Валидация полей: ")
    print("Попытка создать человека с недопустимым возрастом:")
    try:
        bad_developer = Developer(
        name="Тест",
        gender="мужской",
        age=200,
        position="Тест",
        salary=50000,
        expenses=0,
        languages=["Python"]
        )
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("Попытка создать человека с недопустимым полом:")
    try:
        bad_developer_2 = Developer(
        name="Тест",
        gender="инопланетянин",
        age=25,
        position="Тест",
        salary=50000,
        expenses=0,
        languages=["Python"]
        )
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("Попытка создать сотрудника с отрицательной зарплатой:")
    try:
        вad_designer = Designer(
        name="Тест",
        gender="женский",
        age=50,
        position="Тест",
        salary=-1000,
        expenses=0,
        tools=["Fotoshop"]
        )
    except ValueError as e:
        print(f"Ошибка: {e}")

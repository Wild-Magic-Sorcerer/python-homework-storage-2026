#!/usr/bin/env python3

import random

VALID_GENDERS = ("мужской", "женский")
RETIREMENT_AGE = 60
class Person:
    """
    Базовый класс, представляющий человека
    Хранит Имя, пол и возраст человека
    """

    def __init__(self, name, gender, age):
        """
        Инициализирует объект человека
        :param name: Имя человека
        :param gender: Пол человека
        :param age: Возраст человека
        :return: Ничего не возвращает, создает объект Person с заданными параметрами
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
        Возвращает имя человека
        :return: Имя человека
        """
        return self._name
    @name.setter
    def name(self, value):
        """
        Устанавливает имя человека
        :param value: Новое значение имени
        :return: Ничего не возвращает, меняет приватную переменную __name
        """
        if type(value) is not str or not value.strip():
            raise ValueError("Имя не может быть пустой строкой!")
        self._name = value.strip()

    @property
    def gender(self):
        """
        Возвращает пол человека
        :return: Пол человека
        """
        return self._gender
    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол человека
        :param value: Новое значение пола
        :return: Ничего не возвращает, меняет приватную переменную __gender
        """
        if value not in VALID_GENDERS:
            raise ValueError("В Российской федерации есть только мужчина и женщина!!!!!!!!")
        self._gender = value

    @property
    def age(self):
        """
        Возвращает возраст человека
        :return: Возраст человека
        """
        return self._age
    @age.setter
    def age(self, value):
        """
        Устанавливает возраст человека
        :param value: Новое значение возраста
        :return: Ничего не возвращает, меняет приватную переменную __age
        """
        if type(value) is not int:
            raise TypeError (f"Возраст - это только цифры, а не Ваши загагулины: {type(value).__name__}")
        if not 0 <= value <= 115:
            raise ValueError("Возраст может быть только от 0 до 115, больше в России не живут...")
        self._age = value

    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним
        :return: True, Если возраст >= 18, иначе False
        """
        return self.age >= 18
    def __str__(self):
        """
        Возвращает строку с основной информацией о человеке
        :return: Строка содержащая информацию об имени, поле, возрасте и статус совершеннолетия
        """
        adult_status = "Совершеннолетний" if self.is_adult() else "Несовершеннолетний"
        return f"Person: имя = {self.name}, пол = {self.gender}, возраст = {self.age} ({adult_status})"

    @classmethod
    def random_person(cls, name, gender, age):
        """
        Создает объект Person из переданных переменных
        :param name: Имя человека
        :param gender: Пол человека
        :param age: Возраст человека
        :return: Новый объект Person
        """
        return cls(name=name, gender=gender, age=age)


class Employee(Person):
    """
    Класс сотрудника. Наследует Person
    Добавляет должность, зарплату, ежемесячные расходы
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Инициализирует объект сотрудника
        :param name: Имя сотрудника
        :param gender: Пол сотрудника
        :param age: Возраст сотрудника
        :param position: Должность сотрудника
        :param salary: Зарплата сотрудника
        :param monthly_expenses: Ежемесячные расходы сотрудника
        :return: Ничего не возвращает, создает объект Employee с заданными параметрами
        """
        Person.__init__(self, name, gender, age)
        self._position = position
        self._salary = salary
        self._monthly_expenses = monthly_expenses
        self.is_alive = True
        self.savings = 0.0
        self.position = position
        self.salary = salary
        self.monthly_expenses = monthly_expenses

    @property
    def position(self):
        """
        Возвращает должность сотрудника
        :return: Должность сотрудника
        """
        return self._position
    @position.setter
    def position(self, value):
        """
        Устанавливает должность сотрудника
        :param value: Новое значение должности
        :return: Ничего не возвращает, меняет приватную переменную __position
        """
        if type(value) is not str or not value.strip():
            raise ValueError ("Позиция не должна быть пустой!")
        self._position = value.strip()

    @property
    def salary(self):
        """
        Возвращает зарплату сотрудника
        :return: Зарплата сотрудника
        """
        return self._salary
    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату сотрудника
        :param value: Новое значение зарплаты
        :return: Ничего не возвращает, меняет приватную переменную __salary
        """
        if type(value) not in (int, float):
            raise TypeError("Зарплату получаем циферками, не фантиками!")
        if value <= 0:
            raise ValueError ("Зарплата отрицательной быть не может!")
        self._salary = float(value)

    @property
    def monthly_expenses(self):
        """
        Возвращает ежемесячные расходы сотрудника
        :return: Ежемесячные расходы
        """
        return self._monthly_expenses

    @monthly_expenses.setter
    def monthly_expenses(self, value):
        """
        Устанавливает ежемесячные расходы
        :param value: Новое значение расходов
        :return: Ничего не возвращает, меняет приватную переменную __monthly_expenses
        """
        if type(value) not in (int, float):
            raise TypeError("Расходы могут быть только цифрами!")
        if value < 0:
            raise ValueError("Расходы не могут быть отрицательными!")
        self._monthly_expenses = float(value)

    def work(self):
        """
        Возвращает строку, описывающую работу сотрудника
        :return: Описание работы сотрудника
        """
        return f"{self.name}(Работник) просто работает"

    def monthly_income(self):
        """
        Рассчитывает чистый месячный доход
        :return: Чистый месячный доход
        """
        return self.salary - self.monthly_expenses

    def check_survival(self):
        """
        Проверяет, может ли сотрудник выжить. Проверка доходов и расходов
        :return: Ничего не возвращает, выводит сообщение о смерти и обновляет переменную is_alive
        """
        if self.monthly_expenses > self.salary:
            self.is_alive = False
            print(f"{self.name} - умер, его расходы на WB ({self.monthly_expenses}) превысили зарплату ({self.salary}) за ним пришли коллекторы...")

    def calculate_money_savings(self):
        """
        Рассчитывает, сколько денег сотрудник накопит до пенсии
        :return: Сумма накоплений до пенсии
        """
        if not self.is_alive:
            print(f"{self.name} - помер, все накопления разобрали родственники.")
            return 0.0
        years_to_retirement = max(0, RETIREMENT_AGE - self.age)
        months_to_retirement = years_to_retirement * 12
        monthly_income = self.monthly_income()

        if monthly_income <= 0:
            print(f"{self.name} не сможет накопить: все заработанные деньги уходят на омаров")
            return 0.0

        total_savings = monthly_income * months_to_retirement
        print(f"{self.name} ({self.position}): до пенсии {years_to_retirement} лет, накопит {total_savings}")
        return total_savings

    def __str__(self):
        """
        Возвращает строку с информацией о сотруднике
        :return: Строка, содержащая информацию об имени, поле, возрасте, должности, зарплаты и расходов
        """
        base_info = super().__str__()
        status = "Выживает" if self.is_alive else "Помер"
        return f"{base_info}, должность = {self.position}, зарплата = {self.salary}, расходы = {self.monthly_expenses}, статус = {status}"

class Manager(Employee):
    """
    Класс Менеджера. Наследует Employee
    Добавляет список подчиненных
    Могут проводить митинги со своими подчиненными
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Инициализирует объект менеджера
        :param name: Имя менеджера
        :param gender: Пол менеджер
        :param age: Возраст менеджера
        :param position: Должность менеджера
        :param salary: Зарплата менеджера
        :param monthly_expenses: Расходы менеджера
        :return: Ничего не возвращает, создает объект Manager с пустым списком подчиненных
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._subordinates = []

    @property
    def subordinates(self):
        """
        Возвращает копию списка подчиненных
        :return: Копия списка подчиненных
        """
        return self._subordinates.copy()

    @subordinates.setter
    def subordinates(self, value):
        """
        Запрещает прямое изменение списка подчиненных

        :param value: Новое значение списка
        :return: Ничего не возвращает, выбрасывает исключение при попытке изменения
        """
        raise AttributeError("Список подчиненных нельзя изменить! Для этого используйте методы add_subordinates или remove_subordinates")

    def add_subordinates(self, employee):
        """
        Добавляет сотрудника в список подчиненных
        :param employee: Имя сотрудника, который становится подчиненным
        :return: Ничего не возвращает, добавляет собрудника в список подчиненных
        """
        if not isinstance(employee, Employee):
            raise TypeError ("Подчиненный должен быть рабом рабочего")
        self._subordinates.append(employee)
        print(f"{employee.name} добавлен в подчинение к {self.name}")

    def remove_subordinates(self, employee):
        """
        Удаляет сотрудника из списка подчиненных
        :param employee: Имя сотрудника, которого удаляют из списка подчиненных
        :return: Ничего не возвращает, удаляет сотрудника из списка подчиненных и выводит сообщение
        """
        if employee in self._subordinates:
            self._subordinates.remove(employee)
            print(f"{employee.name} Уволен из подчинения {self.name}")

    def conduct_meeting(self):
        """
        Проводит митинг со всеми подчиненными
        :return: Ничего не возвращает, вывод список присутствующих на митинге
        """
        if not self._subordinates:
            print(f"{self.name}проводит митинг, но нет соратников..")
            return
        print(f"{self.name} проводит митинг. Присутствуют:")
        for sub in self._subordinates:
            print(f" - {sub.name} ({sub.position})" )

    def work(self):
        """
        Возвращает строку, описывающую работу менеджера
        :return: Описание работы менеджера с указанием количества подчиненных
        """
        return f"{self.name} управляет командой из {len(self._subordinates)} человек"

    def __str__(self):
        """
        Возвращает строку с информацией о менеджере
        :return: Строка, содержащая информацию о менеджере и количестве его подчиненных
        """
        base = super().__str__()
        return f"{base}, подчиненных: {len(self._subordinates)}"

class Developer(Employee):
    """
    Класс разработчика. Наследует Employee
    Добавляет список языков программирования и метод для написания кода
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages):
        """
        Инициализирует объект разработчика
        :param name: Имя разработчика
        :param gender: Пол разработчика
        :param age: Возраст разработчика
        :param position: Должность разработчика
        :param salary: Зарплата разработчика
        :param monthly_expenses: Расходы разработчика
        :param languages: Список языков программирования
        :return: Ничего не возвращает, создает объект Developer с заданными языками
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._languages = None
        self.languages = languages

    @property
    def languages(self):
        """
        Возвращает копию списка языков программирования
        :return: Копия списка языков программирования
        """
        return self._languages.copy()
    @languages.setter
    def languages(self, value):
        """
        Устанавливает список языков программирования
        :param value: Новый список языков
        :return: Ничего не возвращает, меняет приватную переменную __languages
        """
        if type(value) is not list or not value:
            raise ValueError ("Список языков не может быть пустым!")
        self._languages = [str(lang).strip() for lang in value if str(lang).strip()]
        if not self._languages:
            raise ValueError("Список языков должен содержать хотя бы один элемент ")

    def code(self):
        """
        Возвращает строку о написании кода на случайном языке из списка
        :return: Описание написания кода на случайном языке
        """
        lang = random.choice(self._languages)
        return f" {self.name} пишет код на {lang}"

    def work(self):
        """
        Возвращает строку, описывающую работу разработчика
        :return: Результат вывода метода code()
        """
        return self.code()

    def __str__(self):
        """
        Возвращает строку с информацией о разработчике
        :return: Строка, содержащая информацию о разработчике и его языках
        """
        base = super().__str__()
        return f"{base}, языки: {', '.join(self._languages)}"


class Designer(Employee):
    """
    Класс дизайнера. Наследует Employee
    Добавляет список инструментов и метод для создания макетов
    """
    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools):
        """
        Инициализирует объект дизайнера
        :param name: Имя дизайнера
        :param gender: Пол дизайнера
        :param age: Возраст дизайнера
        :param position: Должность дизайнера
        :param salary: Зарплата дизайнера
        :param monthly_expenses: Расходы дизайнера
        :param tools: Список инструментов
        :return: Ничего не возвращает, создает объект Designer с заданными инструментами
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._tools = None
        self.tools = tools

    @property
    def tools(self):
        """
        Возвращает копию списка инструментов
        :return: Копия списков инструментов
        """
        return  self._tools.copy()
    @tools.setter
    def tools(self, value):
        """
        Устанавливает список инструментов
        :param value: Новый список инструментов
        :return: Ничего не возвращает, меняет приватную переменную __tools
        """
        if type(value) is not list or not value:
            raise ValueError ("Список инструментов не может быть пустым")
        self._tools = [str(tool).strip() for tool in value if str(tool).strip()]
        if not self._tools:
            raise ValueError("Список инструментов должен содержать хотя бы один элемент")

    def create_design(self):
        """
        Возвращает строку о создании макета в случайном инструменте из списка
        :return: Описание создания макета в случайном инструменте
        """
        tool = random.choice(self._tools)
        return f"{self.name} создает макет в {tool}"

    def work(self):
        """
        Возвращает строку, описывающую работу дизайнера
        :return: Результат вывода метода create_design()
        """
        return self.create_design()

    def __str__(self):
        """
        Возвращает строку с информацией о дизайнере
        :return: Строка с информацией о дизайнере и его инструментах
        """
        base = super().__str__()
        return f"{base}, инструменты: {', '.join(self._tools)}"


if __name__ == '__main__':
    manager = Manager("Алексей", "мужской",35, "Руководитель группы", 150000, 60000)
    developer = Developer("Мария", "женский", 28, "Старший разработчик", 180000, 70000,
                          ["Python", "JavaScript", "Go"])
    designer = Designer("Иван", "мужской", 30, "UI/UX Дизайнер", 120000, 50000,
                        ["Figma", "Photoshop", "Illustrator"])

    print(manager)
    print(developer)
    print(designer)

    person = Person.random_person("Ольга", "женский", 42)
    print(person)

    validation_case = [
        ("Пустое имя", lambda: Person("", "мужской", 25)),
        ("Некорректный пол", lambda: Person("Тест", "инопланетянин", 25)),
        ("Отрицательный возраст", lambda: Person("Тест", "мужской", -5)),
        ("Возраст > 120", lambda: Person("Тест", "мужской", 150)),
        ("Отрицательная зарплата", lambda: Employee("Тест", "мужской", 25, "Разработчик", -1000, 500)),
        ("Пустой список языков", lambda: Developer("Тест", "мужской", 25, "Разработчик", 1000, 500, [])),
    ]

    for description, action in validation_case:
        try:
            action()
            print("Все плохо, все сломалось - придется смотреть все заново")
        except (ValueError,TypeError) as e:
            print(e)

    adult = Person("Взрослый", "мужской", 25)
    child = Person("Ребёнок","женский", 10)

    print(f"  {adult.name}: совершеннолетний? {adult.is_adult()}")
    print(f"  {child.name}: совершеннолетний? {child.is_adult()}")

    employees = (manager, developer, designer)
    for emp in employees:
        print(f"  {emp}")

    for emp in employees:
        print(emp.work())

    junior_dev = Developer("Петр", "мужской", 22, "Младший Разработчик", 80000, 40000, ["Python"])
    manager.add_subordinates(developer)
    manager.add_subordinates(junior_dev)
    manager.add_subordinates(designer)
    manager.conduct_meeting()
    manager.remove_subordinates(junior_dev)
    print(f"  Осталось подчинённых: {len(manager.subordinates)}")

    for emp in employees:
        emp.calculate_money_savings()

    reckless = Manager("Транжира", "мужской", 40, "Исполнительный директор", 100000, 150000)
    reckless.check_survival()
    print(f"  Статус: {'Выжил' if reckless.is_alive else 'помер'}")

    print("  Вызов get_info() у Designer:")
    print(f"    {designer}")
    print("  Цепочка вызовов: Designer.__str__() -> Employee.__str__() -> Person.__str__()")

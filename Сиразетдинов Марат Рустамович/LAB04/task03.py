from abc import ABC, abstractmethod
import random

ADULT_NUMBER = 18
RETIREMENT_AGE = 65
MONTHS_IN_YEAR = 12


class Person:
    """
    Базовый класс, описывающий человека.

    :param name: имя человека
    :param gender: пол (М или Ж)
    :param age: возраст
    """

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @property
    def name(self):
        """
        Возвращает имя человека
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Устанавливает имя с проверкой на непустую строку

        :param value: новое имя
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Имя должно быть непустой строкой')
        self.__name = value.strip()

    @property
    def gender(self):
        """
        Возвращает пол человека
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол с проверкой корректного значения

        :param value: пол (М или Ж)
        """
        if not isinstance(value, str) or value.strip().upper() not in ('М', 'Ж'):
            raise ValueError("Пол должен быть указан как 'М' или 'Ж'")
        self.__gender = value.strip().upper()

    @property
    def age(self):
        """
        Возвращает возраст человека
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Устанавливает возраст с проверкой диапазона

        :param value: возраст в годах
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError('Возраст должен быть целым числом')
        if not (0 <= value <= 120):
            raise ValueError('Возраст должен быть от 0 до 120 лет')
        self.__age = value

    def get_info(self):
        """
        Возвращает строку с основной информацией о человеке

        :return: строка с описанием персоны
        """
        return (
            f'{self.__class__.__name__}: \n'
            f'Имя: {self.name}, пол: {self.gender}, возраст: {self.age} лет'
        )

    def is_adult(self):
        """
        Проверяет, является ли человек совершеннолетним

        :return: True, если возраст > 18
        """
        return self.age >= ADULT_NUMBER

    @classmethod
    def create_person(cls, name, gender, age):
        """
        Классовый метод для создания объекта Person через переменные

        :param name: имя человека
        :param gender: пол ('М' или 'Ж')
        :param age: возраст
        :return: новый объект класса
        """
        return cls(name, gender, age)


class Employee(Person, ABC):
    """
    Абстрактный класс сотрудника — наследник Person

    :param name: имя сотрудника
    :param gender: пол ('М' или 'Ж')
    :param age: возраст
    :param position: должность
    :param salary: ежемесячная зарплата
    :param expenses: усреднённые расходы в месяц
    """

    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age)
        self.position = position
        self.salary = salary
        self.expenses = expenses
        self.__is_alive = True

        if self.expenses > self.salary:
            self.__is_alive = False
            raise RuntimeError(
                f'Сотрудник {self.name} умер: расходы ({self.expenses}) '
                f'превышают зарплату ({self.salary})'
            )

    @property
    def position(self):
        """
        Возвращает должность сотрудника.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Устанавливает должность с проверкой.

        :param value: название должности
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Должность должна быть непустой строкой')
        self.__position = value.strip()

    @property
    def salary(self):
        """
        Возвращает зарплату сотрудника
        """
        return self.__salary

    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату с проверкой на положительное число

        :param value: размер зарплаты
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Зарплата должна быть числом')
        if value <= 0:
            raise ValueError('Зарплата должна быть больше нуля')
        self.__salary = float(value)

    @property
    def expenses(self):
        """
        Возвращает ежемесячные расходы сотрудника.
        """
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        """
        Устанавливает расходы с проверкой на неотрицательное число

        :param value: сумма расходов в месяц
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Расходы должны быть числом')
        if value < 0:
            raise ValueError('Расходы не могут быть отрицательными')
        self.__expenses = float(value)

    @abstractmethod
    def work(self):
        """
        Абстрактный метод, описывающий рабочий процесс сотрудника
        """
        pass

    def calculate_cashflow(self, months):
        """
        Рассчитывает чистый приток денег за N месяцев

        :param months: количество месяцев
        :return: накопленная сумма за указанный период
        """
        if (
            not isinstance(months, int)
            or isinstance(months, bool)
            or months <= 0
        ):
            raise ValueError('Количество месяцев должно быть целым числом > 0')
        monthly_profit = self.salary - self.expenses
        return round(monthly_profit * months, 2)

    def calculate_pension_savings(self):
        """
        Рассчитывает сумму, которую сотрудник скопит до пенсии

        :return: итоговые накопления до пенсии
        """
        if self.age >= RETIREMENT_AGE:
            return 0.0
        months_left = (RETIREMENT_AGE - self.age) * MONTHS_IN_YEAR
        return self.calculate_cashflow(months_left)

    def get_info(self):
        """
        Возвращает строку с информацией о сотруднике

        :return: строка с описанием сотрудника
        """
        base_info = super().get_info()
        return f'{base_info}\nДолжность: {self.position}, зарплата: {self.salary} руб., расходы: {self.expenses} руб.'


class Manager(Employee):
    """
    Класс менеджера — наследник Employee.

    :param name: имя менеджера
    :param gender: пол
    :param age: возраст
    :param salary: зарплата
    :param expenses: расходы в месяц
    :param subordinates: начальный список подчинённых
    """

    def __init__(self, name, gender, age, salary, expenses, subordinates=None):
        super().__init__(name, gender, age, 'Менеджер', salary, expenses)
        self.__subordinates = []
        if subordinates:
            for person in subordinates:
                self.add_subordinate(person)

    @property
    def subordinates(self):
        """
        Возвращает копию списка подчинённых
        """
        return self.__subordinates.copy()

    def add_subordinate(self, employee):
        """
        Добавляет сотрудника в список подчинённых

        :param employee: объект сотрудника
        """
        if not isinstance(employee, Employee):
            raise ValueError('Подчинённый должен быть объектом Employee')
        if employee not in self.__subordinates:
            self.__subordinates.append(employee)

    def remove_subordinate(self, employee):
        """
        Удаляет сотрудника из списка подчинённых

        :param employee: объект сотрудника для удаления
        """
        if employee in self.__subordinates:
            self.__subordinates.remove(employee)

    def hold_meeting(self):
        """
        Проводит митинг для текущих подчинённых

        :return: строка с отчётом о проведении митинга
        """
        if not self.__subordinates:
            return f'Менеджер {self.name} проводит митинг в одиночестве.'
        names = ', '.join(emp.name for emp in self.__subordinates)
        return f'Менеджер {self.name} проводит митинг для: {names}'

    def work(self):
        """
        Реализация рабочего процесса менеджера

        :return: описание работы менеджера
        """
        return f'{self.name} управляет командой из {len(self.__subordinates)} чел. и ставит задачи'

    def get_info(self):
        """
        Возвращает полную информацию о менеджере

        :return: строка с описанием менеджера
        """
        base_info = super().get_info()
        return f'{base_info} \nПодчинённых: {len(self.__subordinates)} чел'


class Developer(Employee):
    """
    Класс разработчика — наследник Employee

    :param name: имя разработчика
    :param gender: пол ('М' или 'Ж')
    :param age: возраст
    :param salary: зарплата
    :param expenses: расходы в месяц
    :param languages: список языков программирования
    """

    def __init__(self, name, gender, age, salary, expenses, languages):
        super().__init__(name, gender, age, 'Разработчик', salary, expenses)
        if not isinstance(languages, (list, tuple)) or not languages:
            raise ValueError('Нужно передать непустой список языков')
        self.__languages = [str(lang).strip() for lang in languages]

    @property
    def languages(self):
        """
        Возвращает копию списка языков программирования
        """
        return self.__languages.copy()

    def write_code(self):
        """
        Пишет код на случайном языке из списка навыков разработчика

        :return: строка с результатом работы
        """

        def hold_meeting(self):
            """
            Проводит митинг для текущих подчинённых

            :return: строка с отчётом о проведении митинга
            """
            if not self.__subordinates:
                return f'Менеджер {self.name} проводит митинг в одиночестве.'
            names = ', '.join(emp.name for emp in self.__subordinates)
            return f'Менеджер {self.name} проводит митинг для: {names}'

        def work(self):
            """
            Реализация рабочего процесса менеджера

            :return: описание работы менеджера
            """
            return f'{self.name} управляет командой из {len(self.__subordinates)} чел. и ставит задачи'


        def get_info(self):
            """
            Возвращает полную информацию о менеджере

            :return: строка с описанием менеджера
            """
            base_info = super().get_info()
            return f'{base_info} \nПодчинённых: {len(self.__subordinates)} чел'

    class Developer(Employee):
        """
        Класс разработчика — наследник Employee

        :param name: имя разработчика
        :param gender: пол
        :param age: возраст
        :param salary: зарплата
        :param expenses: расходы в месяц
        :param languages: список языков программирования
        """

        def __init__(self, name, gender, age, salary, expenses, languages):
            super().__init__(name, gender, age, 'Разработчик', salary, expenses)
            if not isinstance(languages, (list, tuple)) or not languages:
                raise ValueError('Нужно передать непустой список языков')
            self.__languages = [str(lang).strip() for lang in languages]

        @property
        def languages(self):
            """
            Возвращает копию списка языков программирования
            """
            return self.__languages.copy()

        def write_code(self):
            """
            Пишет код на случайном языке из списка навыков разработчика

            :return: строка с результатом работы
            """
            chosen_lang = random.choice(self.__languages)
            return f'Разработчик {self.name} пишет код на языке {chosen_lang}.'

        def work(self):
            """
            Реализация рабочего процесса разработчика

            :return: описание работы разработчика
            """
            return self.write_code()

        def get_info(self):
            """
            Возвращает полную информацию о разработчике

            :return: строка с описанием разработчика
            """
            base_info = super().get_info()
            langs = ', '.join(self.__languages)
            return f'{base_info} \nЯзыки программирования: {langs}'

    class Designer(Employee):
        """
        Класс дизайнера — наследник Employee

        :param name: имя дизайнера
        :param gender: пол
        :param age: возраст
        :param salary: зарплата
        :param expenses: расходы в месяц
        :param tools: список инструментов дизайна
        """

        def __init__(self, name, gender, age, salary, expenses, tools):
            super().__init__(name, gender, age, 'Дизайнер', salary, expenses)
            if not isinstance(tools, (list, tuple)) or not tools:
                raise ValueError('Нужно передать непустой список инструментов')
            self.__tools = [str(tool).strip() for tool in tools]

        @property
        def tools(self):
            """
            Возвращает копию списка инструментов дизайнера
            """
            return self.__tools.copy()

        def create_mockup(self, project_name='нового сайта'):
            """
            Создаёт макет с использованием инструментов дизайнера

            :param project_name: название проекта для макета
            :return: строка с описанием созданного макета
            """
            tool = random.choice(self.__tools)
            return f'Дизайнер {self.name} создаёт макет {project_name} в программе {tool}.'

        def work(self):
            """
            Реализация рабочего процесса дизайнера

            :return: описание работы дизайнера
            """
            return self.create_mockup()

        def get_info(self):
            """
            Возвращает полную информацию о дизайнере

            :return: строка с описанием дизайнера
            """
            base_info = super().get_info()
            tools_str = ', '.join(self.__tools)
            return f'{base_info} \nИнструменты: {tools_str}'


    if __name__ == '__main__':
        print('\nПроверка:')
        person = Person.create_person('Алексей', 'М', 17)
        print(person.get_info())
        print(f'Совершеннолетний: {"Да" if person.is_adult() else "Нет"}')

        print('\nСоздание сотрудников и проверка финансовых методов:')
        dev = Developer('Илья', 'М', 28, 180000, 70000, ['Python','Java', 'C++'])
        designer = Designer('Екатерина', 'Ж', 25, 130000, 55000, ['Figma', 'Adobe'])
        manager = Manager('Ольга', 'Ж', 34, 210000, 90000, [dev])

        manager.add_subordinate(designer)
        print(manager.hold_meeting())
        print(
            f'Приток {dev.name} за 6 мес.: {dev.calculate_cashflow(6)} руб.'
            f'До пенсии: {dev.calculate_pension_savings()} руб.'
        )

        print('\nПроверка сдохни или умри:')
        try:
            unlucky = Developer('Максик', 'М', 30, 80000, 95000, ['JavaScript'])
        except RuntimeError as err:
            print(f'Событие: {err}')

        print('\nПроверка работы super по всей цепочке:')
        staff = [manager, dev, designer]

        for emp in staff:
            print(emp.get_info())
            print(f'Работа: {emp.work()}')


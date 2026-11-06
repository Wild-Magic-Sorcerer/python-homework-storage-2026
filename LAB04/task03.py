#!/usr/bin/env python3

import random


ADULT_NUMBER = 18
RETIREMENT_AGE = 65
MONTHS_IN_YEAR = 12


class Person:
    """
    Родительский класс, в котором находятся основные характеристики человека.
    """
    def __init__(self, name, gender, age):
        """
        Базовый конструктор класса Person.

        :param name: Имя человека.

        :param gender: Пол человека.

        :param age: Возраст человека.
        """
        if self.check_string(name):
            self._name = name
        else:
            raise ValueError('Имя должно быть непустой строкой')

        if self.check_string(gender):
            self._gender = gender
        else:
            raise ValueError('Пол должен быть непустой строкой')

        if type(age) == int and age >= 0:
            self._age = age
        else:
            raise ValueError('Возраст должен быть целым неотрицательным числом')


    @staticmethod
    def check_string(value):
        """
        Метод для проверки строкового значения.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) == str and value


    @staticmethod
    def check_value(value):
        """
        Метод для проверки числового значения.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) in (int, float)


    @property
    def name(self):
        """
        Метод, который позволяет прочитать имя человека.

        :return: Имя человека.
        """
        return self._name


    @property
    def gender(self):
        """
        Метод, который позволяет прочитать пол человека.

        :return: Пол человека.
        """
        return self._gender


    @property
    def age(self):
        """
        Метод, который позволяет прочитать возраст человека.

        :return: Возраст человека.
        """
        return self._age


    def adult(self):
        """
        Метод для проверки совершеннолетия человека.

        :return: True, если человеку исполнилось 18 лет.
        """
        return self._age >= ADULT_NUMBER


    @classmethod
    def create_person(cls, name, gender, age):
        """
        Метод, который создает объект класса из переменных.

        :param name: Имя человека.

        :param gender: Пол человека.

        :param age: Возраст человека.

        :return: Новый объект класса.
        """
        return cls(name=name, gender=gender, age=age)


    def __str__(self):
        """
        Метод, который "красиво" представляет человека.

        :return: Строка с информацией о человеке.
        """
        return f'Имя: {self._name}, 'f'пол: {self._gender}, 'f'возраст: {self._age}'


class Employee(Person):
    """
    Дочерний класс с характеристиками работника, который наследует класс Person.
    """
    def __init__(self,name,gender,age,position,salary,expenses):
        """
        Базовый конструктор класса Employee.

        :param name: Имя сотрудника.

        :param gender: Пол сотрудника.

        :param age: Возраст сотрудника.

        :param position: Должность сотрудника.

        :param salary: Зарплата сотрудника.

        :param expenses: Средние расходы сотрудника в месяц.
        """
        super().__init__(name=name, gender=gender, age=age)

        if self.check_string(position):
            self._position = position

        else:
            raise ValueError('Должность должна быть непустой строкой')

        if self.check_value(salary) and salary > 0:
            self._salary = salary

        else:
            raise ValueError('Зарплата должна быть положительным числом')

        if self.check_value(expenses) and expenses >= 0:
            self._expenses = expenses

        else:
            raise ValueError('Расходы должны быть неотрицательным числом')


    @property
    def position(self):
        """
        Метод, который позволяет прочитать должность.

        :return: Должность сотрудника.
        """
        return self._position


    @property
    def salary(self):
        """
        Метод, который позволяет прочитать зарплату.

        :return: Зарплата сотрудника.
        """
        return self._salary


    @property
    def expenses(self):
        """
        Метод, который позволяет прочитать средние расходы.

        :return: Средние расходы сотрудника в месяц.
        """
        return self._expenses


    def work(self):
        """
        Абстрактный метод работы сотрудника.

        :raises NotImplementedError: Если метод не переопределен в дочернем классе.
        """
        raise NotImplementedError('В дочернем классе должен быть переопределен метод work()')


    def money_for_months(self, months):
        """
        Метод, который рассчитывает приток денежек за N месяцев.

        :param months: Количество месяцев.

        :return: Сумма накопленных денежек.
        """
        return (self._salary - self._expenses) * months


    def are_you_alive(self):
        """
        Метод, который проверяет, не превышают ли расходы зарплату.
        """
        if self._expenses > self._salary:
            print('Все ушло на додеп, наступила смерть.')


    def money_until_retirement(self):
        """
        Метод, который рассчитывает, сколько денежек сотрудник накопит до пенсии.

        :return: Сумма накопленных денежек до пенсии.

        :raises ValueError: Если сотрудник уже достиг пенсионного возраста.
        """
        if self._age >= RETIREMENT_AGE:
            raise ValueError('Сотрудник уже достиг пенсионного возраста')

        months = (RETIREMENT_AGE - self._age) * MONTHS_IN_YEAR

        return self.money_for_months(months)


    def __str__(self):
        """
        Метод, который "красиво" представляет сотрудника.

        :return: Строка с информацией о сотруднике.
        """

        return f'{super().__str__()}, 'f'должность: {self._position}, 'f'зарплата: {self._salary}, 'f'расходы: {self._expenses}'


class Manager(Employee):
    """
    Дочерний класс с характеристиками менеджера, который наследует класс Employee.
    """
    def __init__(self, name, gender, age,
                 position, salary, expenses,subordinates):
        """
        Базовый конструктор класса Manager.

        :param name: Имя менеджера.

        :param gender: Пол менеджера.

        :param age: Возраст менеджера.

        :param position: Должность менеджера.

        :param salary: Зарплата менеджера.

        :param expenses: Средние расходы в месяц.

        :param subordinates: Список подчиненных.
        """
        super().__init__(name=name, gender=gender, age=age,
                         position=position, salary=salary, expenses=expenses)
        if type(subordinates) == list:
            self._subordinates = subordinates.copy()


    @property
    def subordinates(self):
        """
        Метод, который возвращает копию списка подчиненных.

        :return: Копия списка подчиненных.
        """
        return self._subordinates.copy()


    def add_subordinate(self, subordinate):
        """
        Метод для добавления подчиненного.

        :param subordinate: Новый подчиненный.
        """
        self._subordinates.append(subordinate)


    def remove_subordinate(self, subordinate):
        """
        Метод для удаления подчиненного.

        :param subordinate: Подчиненный для удаления.
        """
        if subordinate in self._subordinates:
            self._subordinates.remove(subordinate)
        else:
            raise ValueError('Такого подчиненного нет')


    def meeting(self):
        """
        Метод для проведения митинга с подчиненными.
        """
        return f'{self._name} проводит митинг ' f'для: {self._subordinates}'


    def work(self):
        """
        Переопределенный метод работы менеджера.

        :return: Строка с описанием работы менеджера.
        """
        return self.meeting()


    def __str__(self):
        """
        Метод, который красиво представляет менеджера.

        :return: Строка с информацией о менеджере.
        """
        return f'{super().__str__()}, 'f'подчиненные: {self._subordinates}'


class Developer(Employee):
    """
    Дочерний класс с характеристиками разработчика, который наследует класс Employee.
    """
    def __init__( self, name, gender, age,
                  position, salary, expenses, languages):
        """
        Базовый конструктор класса Developer.

        :param name: Имя разработчика.

        :param gender: Пол разработчика.

        :param age: Возраст разработчика.

        :param position: Должность разработчика.

        :param salary: Зарплата разработчика.

        :param expenses: Средние расходы в месяц.

        :param languages: Список языков программирования.
        """
        super().__init__(name=name, gender=gender, age=age,
                         position=position, salary=salary, expenses=expenses)

        if type(languages) == list and languages:
            self._languages = languages.copy()


    @property
    def languages(self):
        """
        Метод, который возвращает копию списка языков.

        :return: Копия списка языков программирования.
        """
        return self._languages.copy()


    def write_code(self):
        """
        Метод, который выбирает случайный язык программирования.

        :return: Строка с выбранным языком программирования.
        """
        language = random.choice(self._languages)

        return f'{self._name} пишет код на языке {language}'


    def work(self):
        """
        Переопределенный метод работы разработчика.

        :return: Строка с описанием работы разработчика.
        """
        return self.write_code()


    def __str__(self):
        """
        Метод, который красиво представляет разработчика.

        :return: Строка с информацией о разработчике.
        """
        return f'{super().__str__()}, 'f'языки программирования: {self._languages}'


class Designer(Employee):
    """
   Дочерний класс с характеристиками дизайнера, который наследует класс Employee.
    """
    def __init__(self, name, gender, age,
                 position, salary, expenses, tools):
        """
        Базовый конструктор класса Designer.

        :param name: Имя дизайнера.

        :param gender: Пол дизайнера.

        :param age: Возраст дизайнера.

        :param position: Должность дизайнера.

        :param salary: Зарплата дизайнера.

        :param expenses: Средние расходы в месяц.

        :param tools: Список инструментов дизайнера.
        """
        super().__init__(name=name, gender=gender, age=age,
                         position=position, salary=salary, expenses=expenses)

        if type(tools) == list and tools:
            self._tools = tools.copy()


    @property
    def tools(self):
        """
        Метод, который возвращает копию списка инструментов.

        :return: Копия списка инструментов.
        """
        return self._tools.copy()


    def create_layout(self):
        """
        Метод для создания макета.

        :return: Строка о создании макета.
        """
        return f'{self._name} создает макет'


    def work(self):
        """
        Переопределенный метод работы дизайнера.

        :return: Строка с описанием работы дизайнера.
        """
        return self.create_layout()


    def __str__(self):
        """
        Метод, который красиво представляет дизайнера.

        :return: Строка с информацией о дизайнере.
        """
        return f'{super().__str__()}, 'f'инструменты: {self._tools}'


if __name__ == '__main__':
    manager_1 = Manager(name='Лиза', gender='Ж', age=23,
                        position='Manager', salary=120000,
                        expenses=60000, subordinates=['Славик', 'Марк'])

    developer_1 = Developer(name='Сережа', gender='М', age=26,
                            position='Developer', salary=150000,
                            expenses=70000, languages=['Python', 'Java', 'C++'])

    designer_1 = Designer(name='Юля', gender='Ж', age=20,
                          position='Designer', salary=110000,
                          expenses=50000, tools=['Figma', 'Photoshop'])

    employees = (manager_1, developer_1, designer_1)

    for employee in employees:  #полиморфный __str__() + super()
        print(employee)

    for employee in employees:  #полиморфный work()
        result = employee.work()
        print(result)
        

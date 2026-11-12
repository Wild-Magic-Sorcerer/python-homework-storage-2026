from abc import abstractmethod, ABC
import random

class Person:
    '''
    Класс для любого человека.
    '''
    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age

    @property
    def name(self):
        '''
        Метод, возвращающий имя человека.
        :return: self._name
        :raises ValueError: Если вместо должности указана пустая строка.
        '''
        if self._name == "":
            raise ValueError("Каждого человека как-то зовут, введите что-то!")
        return self._name

    @property
    def gender(self):
        '''
        Метод, возвращающий пол человека.
        :return: self._gender
        '''
        if self._gender == "male" or self._gender == "female":
            return self._gender
        else:
            raise ValueError("Вы ввели что-то странное вместо пола, такого не бывает!")

    @property
    def age(self):
        '''
        Метод, возвращающий возраст человека.
        :return: self._age
        '''
        if self._age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        else:
            return self._age


    def introduce(self):
        '''
        Метод, позволяющий представить человека.
        :return: Строка с информацией о человеке.
        '''
        return f"This is a {self._gender} named {self._name} who is {self._age} old."

    def adulthood(self):
        '''
        Метод, позволяющий оценить совершеннолетие человека.
        :return: "child" или "adult"
        '''
        if self._age >= 18:
            return "adult"
        else:
            return "child"

    @classmethod
    def design_a_person(cls, name, gender, age):
        '''
        Классовый метод, позволяющий сконструировать персону через переменные.
        :param name: Имя нового человека.
        :param gender: Пол нового человека.
        :param age: Возраст нового человека.
        :return: Новый объект класса Person.
        '''
        return cls(name, gender, age)

class Employee(Person):
    '''
    Класс для работника. Наследует характеристики класса Person.
    '''
    def __init__(self, name, gender, age, position, salary, avg_expenses):
        super().__init__(name, gender, age)
        self._position = position
        self._salary = salary
        self._expenses = avg_expenses
        if self._expenses > self._salary:
            print(f"Работник {self._name} умер, потому что тратил слишком много.")

    @property
    def position(self):
        '''
        Метод, возвращающий должность человека.
        :return: self._position
        :raises ValueError: Если вместо должности указана пустая строка.
        '''
        if self._position == "":
            raise ValueError("У каждого работника есть своя должность!")
        return self._position

    @property
    def salary(self):
        '''
        Метод, возвращающий зарплату человека.
        :return: self._salary
        :raises ValueError: Если зарплата меньше 0.
        '''
        if self._salary <= 0:
            raise ValueError("Каждому работнику должны что-то платить, зарплата не может быть нулевой или отрицательной!")
        return self._salary

    @property
    def expenses(self):
        '''
        Метод, возвращающий расходы человека.
        :return: self._expenses
        :raises ValueError: Если расходы меньше или равны 0.
        '''
        if self._expenses <= 0:
            raise ValueError("К сожалению, расходы не могут быть <= 0.")
        return self._expenses

    @abstractmethod
    def work(self):
        '''
        Абстрактный метод для работы, пока не делающий ничего.
        :return: None
        '''
        pass

    def profit(self, months):
        '''
        Метод, позволяющий оценить приток денег за данное количество месяцев.
        :param months: Количество месяцев.
        :return: profit
        :raises ValueError: Если количество месяцев отрицательно.
        '''
        if months < 0:
            profit = (self._salary - self._expenses) * months
            return profit
        else:
            raise ValueError("Количество месяцев не может быть отрицательным!")

    def before_pension(self):
        '''
        Метод, позволяющий рассчитать, сколько человек скопит денег до пенсии.
        :return: money
        '''
        if self.gender == "female":
            if self._age >= 59:
                return "Вы уже претендуете на пенсию!"
            else:
                money = (self._salary - self._expenses) * (59 - self._age) * 12
        else:
            if self._age >= 64:
                return "Вы уже претендуете на пенсию!"
            else:
                money = (self._salary - self._expenses) * (64 - self._age) * 12
        return money


class Manager(Employee):
    '''
    Класс для менеджера. Наследует характеристики класса Employee.
    '''
    def __init__(self, name, gender, age, position, salary, avg_expenses, workers):
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._workers = workers

    def hire_workers(self, worker):
        self._workers.append(worker)

    def fire_workers(self, worker):
        self._workers.remove(worker)

    def work(self):
        '''
        Метод, показывающий работу менеджера.
        :return: Строка, сообщающая о проведении митинга.
        '''
        return f"Проводится митинг для {self._workers}"

class Developer(Employee):
    '''
    Класс для разработчика. Наследует характеристики класса Employee.
    '''
    def __init__(self, name, gender, age, position, salary, avg_expenses, languages):
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._languages = languages

    def work(self):
        '''
        Метод, показывающий работу разработчика.
        :return: Строка, указывающая, на каком языке программирования сейчас пишет разработчик.
        '''
        lang = random.choice(self._languages)
        return f"Разработчик пишет код на языке {lang}."

class Designer(Employee):
    '''
    Класс для дизайнера. Наследует характеристики класса Employee.
    '''
    def __init__(self, name, gender, age, position, salary, avg_expenses, instruments):
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._instruments = instruments

    def work(self):
        '''
        Метод, показывающий работу дизайнера.
        :return: Строка с указанием о создании макета.
        '''
        return f"Создаётся макет при помощи набора инструментов: {self._instruments}."

if __name__ == '__main__':
    print("Проверка, что дочерние класса адекватно использует методы класса Person:")
    Kate = Employee("Kate", "female", 35, "engineer", 36000, 15000)
    Tom = Manager("Tom", "male", 30, "manager", 25000, 20000, ["Fai", "Lucy"])
    Max = Developer("Max", "male", 30, "developer", 70000, 9000, ["Python", "Rust"])
    Sveta = Designer("Sveta", "female", 18, "junior",3500, 1000, "brush, pen")
    print(Kate.introduce())
    print("Tom ребёнок или взрослый?", Tom.adulthood())
    print(Max.introduce())
    print("Sveta ребёнок или взрослый?", Sveta.adulthood())
    for worker in [Tom, Max, Sveta]:
        print(worker.work())

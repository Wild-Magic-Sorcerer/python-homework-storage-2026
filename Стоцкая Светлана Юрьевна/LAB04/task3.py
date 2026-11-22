from abc import abstractmethod
import random

MALE_GENDER = "male"
FEMALE_GENDER = "female"
M_PENSION_AGE = 64
FEM_PENSION_AGE = 59

class Person:
    """
    Класс для любого человека.
    """
    def __init__(self, name, gender, age):
        """
        Метод-конструктор класса Person.
        :param name: Имя человека.
        :param gender: Пол человека.
        :param age: Возраст человека.
        :return: None
        """
        self._name = name
        self._gender = gender
        self._age = age
        self._death = False

    @property
    def name(self):
        """
        Метод, возвращающий имя человека.
        :return: Имя человека.
        :raises ValueError: Если вместо должности указана пустая строка и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._name.strip() == "":
            raise ValueError("Каждого человека как-то зовут, введите что-то!")
        return self._name

    @property
    def gender(self):
        """
        Метод, возвращающий пол человека.
        :return: Пол человека.
        :raises ValueError: Если что-то странное вместо пола и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._gender == MALE_GENDER or self._gender == FEMALE_GENDER:
            return self._gender
        else:
            raise ValueError("Вы ввели что-то странное вместо пола, такого не бывает!")

    @property
    def age(self):
        """
        Метод, возвращающий возраст человека.
        :return: Возраст человека.
        :raises ValueError: Если возраст отрицательный и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        else:
            return self._age

    def __str__(self):
        """
        Метод, позволяющий представить человека.
        :return: Строка с информацией о человеке.
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        return f"This is a {self._gender} named {self._name} who is {self._age} old."

    def adulthood(self):
        """
        Метод, позволяющий оценить совершеннолетие человека.
        :return: "child" или "adult"
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._age >= 18:
            return "adult"
        else:
            return "child"

    @classmethod
    def design_a_person(cls, some_dict):
        """
        Классовый метод, позволяющий сконструировать персону из словаря.
        :param some_dict: Словарь, описывающий объект, который должен быть создан.
        :return: Новый объект класса Person.
        """
        name = some_dict.get("name", "")
        gender = some_dict.get("gender", 0)
        age = some_dict.get("age", -1)
        return cls(name, gender, age)

class Employee(Person):
    """
    Класс для работника. Наследует характеристики класса Person.
    """
    def __init__(self, name, gender, age, position, salary, avg_expenses):
        """
        Метод-конструктор класса Employee.
        :param name: Имя работника.
        :param gender: Пол работника.
        :param age: Возраст работника.
        :param position: Должность работника.
        :param salary: Зарплата работника.
        :param avg_expenses: Средние расходы работника за месяц.
        :return: None
        """
        super().__init__(name, gender, age)
        self._position = position
        self._salary = salary
        self._expenses = avg_expenses
        if self._expenses > self._salary:
            self._death = True
            print(f"Работник {self._name} умер, потому что тратил слишком много.")
        else:
            self._death = False

    @property
    def position(self):
        """
        Метод, возвращающий должность человека.
        :return: Должность человека.
        :raises ValueError: Если вместо должности указана пустая строка и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._position == "":
            raise ValueError("У каждого работника есть своя должность!")
        return self._position

    @property
    def salary(self):
        """
        Метод, возвращающий зарплату человека.
        :return: Зарплата человека.
        :raises ValueError: Если зарплата меньше 0 и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._salary <= 0:
            raise ValueError("Каждому работнику должны что-то платить, зарплата не может быть нулевой или отрицательной!")
        return self._salary

    @property
    def expenses(self):
        """
        Метод, возвращающий расходы человека.
        :return: Средние расходы человека за месяц.
        :raises ValueError: Если расходы меньше или равны 0 и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self._expenses <= 0:
            raise ValueError("К сожалению, расходы не могут быть <= 0.")
        return self._expenses

    @abstractmethod
    def work(self):
        """
        Абстрактный метод для работы, пока не делающий ничего.
        :return: None
        """
        pass

    def profit(self, months):
        """
        Метод, позволяющий оценить приток денег за данное количество месяцев.
        :param months: Количество месяцев.
        :return: Приток денег за сколько-то месяцев.
        :raises ValueError: Если количество месяцев отрицательно и если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if months < 0:
            profit = (self._salary - self._expenses) * months
            return profit
        else:
            raise ValueError("Количество месяцев не может быть отрицательным!")

    def before_pension(self):
        """
        Метод, позволяющий рассчитать, сколько человек скопит денег до пенсии.
        :return: Сумма накопленных денег.
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        if self.gender == FEMALE_GENDER:
            if self._age >= FEM_PENSION_AGE:
                return "Вы уже претендуете на пенсию!"
            else:
                money = (self._salary - self._expenses) * (FEM_PENSION_AGE - self._age) * 12
        else:
            if self._age >= M_PENSION_AGE:
                return "Вы уже претендуете на пенсию!"
            else:
                money = (self._salary - self._expenses) * (M_PENSION_AGE - self._age) * 12
        return money

class Manager(Employee):
    """
    Класс для менеджера. Наследует характеристики класса Employee.
    """
    def __init__(self, name, gender, age, position, salary, avg_expenses, workers):
        """
        Метод-конструктор класса Manager.
        :param name: Имя менеджера.
        :param gender: Пол менеджера.
        :param age: Возраст менеджера.
        :param position: Должность менеджера.
        :param salary: Зарплата менеджера.
        :param avg_expenses: Средние расходы менеджера за месяц.
        :param workers: Подчинённые менеджера.
        :return: None
        """
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._workers = workers

    def hire_workers(self, worker):
        """
        Метод, позволяющий менеджеру набирать работников.
        :param worker: Человек, которого взяли на работу.
        :return: None
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        self._workers.append(worker)

    def fire_workers(self, worker):
        """
        Метод, позволяющий менеджеру выгонять работников.
        :param worker: Человек, которого выгнали с работы.
        :return: None
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        self._workers.remove(worker)

    def work(self):
        """
        Метод, показывающий работу менеджера.
        :return: Строка, сообщающая о проведении митинга.
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        return f"Проводится митинг для {self._workers}"

class Developer(Employee):
    """
    Класс для разработчика. Наследует характеристики класса Employee.
    """
    def __init__(self, name, gender, age, position, salary, avg_expenses, languages):
        """
        Метод-конструктор класса Developer.
        :param name: Имя разработчика.
        :param gender: Пол разработчика.
        :param age: Возраст разработчика.
        :param position: Должность разработчика.
        :param salary: Зарплата разработчика.
        :param avg_expenses: Средние расходы разработчика.
        :param languages: Языки, на которых разработчик умеет программировать.
        :return: None
        """
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._languages = languages

    def work(self):
        """
        Метод, показывающий работу разработчика.
        :return: Строка, указывающая, на каком языке программирования сейчас пишет разработчик.
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        lang = random.choice(self._languages)
        return f"Разработчик пишет код на языке {lang}."

class Designer(Employee):
    """
    Класс для дизайнера. Наследует характеристики класса Employee.
    """
    def __init__(self, name, gender, age, position, salary, avg_expenses, instruments):
        """
        Метод-конструктор класса Designer.
        :param name: Имя дизайнера.
        :param gender: Пол дизайнера.
        :param age: Возраст дизайнера.
        :param position: Должность дизайнера.
        :param salary: Зарплата дизайнера.
        :param avg_expenses: Средние расходы дизайнера.
        :param instruments: Инструменты, которыми владеет дизайнер.
        :return: None
        """
        super().__init__(name, gender, age, position, salary, avg_expenses)
        self._instruments = instruments

    def work(self):
        """
        Метод, показывающий работу дизайнера.
        :return: Строка с указанием о создании макета.
        :raises ValueError: Если человек умер.
        """
        if self._death:
            raise ValueError("Этот человек умер!!!")
        return f"Создаётся макет при помощи набора инструментов: {self._instruments}."

if __name__ == '__main__':
    print("Проверка, что дочерние класса адекватно использует методы класса Person:")
    kate = Employee("Kate", "female", 35, "engineer", 36000, 15000)
    tom = Manager("Tom", "male", 30, "manager", 25000, 20000, ["Fai", "Lucy"])
    maxim = Developer("Max", "male", 30, "developer", 70000, 9000, ["Python", "Rust"])
    sveta = Designer("Sveta", "female", 18, "junior",3500, 1000, "brush, pen")
    print(kate)
    print("Tom ребёнок или взрослый?", tom.adulthood())
    print(maxim)
    print("Sveta ребёнок или взрослый?", sveta.adulthood())
    for worker in (tom, maxim, sveta):
        print(worker.work())

import random


class Person:
    """Человек: имя, пол, возраст"""
    VALID_GENDERS = ("м", "ж")

    def __init__(self, name, gender, age):
        """
        Создает человека с параметрами:
        :param name: имя
        :param gender: пол (м/ж)
        :param age: возраст >=0
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        if gender not in self.VALID_GENDERS:
            raise ValueError(f"Пол должен быть одним из: {self.VALID_GENDERS}")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом")
        self.__name = name
        self.__gender = gender
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @classmethod
    def create(cls, name, gender, age):
        """Публичный метод создания персоны через переменные."""
        return cls(name, gender, age)

    def is_adult(self):
        """Проверка на совершеннолетие (18+)"""
        return self.age >= 18

    def introduce(self):
        """Представление человека"""
        return f"{self.name} ({self.gender}), {self.age} лет"


class Employee(Person):
    """Сотрудник: должность, зарплата, расходы"""
    def __init__(self, name, gender, age, position, salary, expenses):
        """
        Создает сотрудника с параметрами
        :param name: имя
        :param gender: гендер (м/ж)
        :param age: возраст >=0
        :param position: должность
        :param salary: зарплата >0
        :param expenses: расходы (не больше зарплаты, иначе смерть)
        """
        super().__init__(name, gender, age)
        if not isinstance(position, str) or not position.strip():
            raise ValueError("Должность должна быть непустой строкой")
        if salary <= 0:
            raise ValueError("Зарплата должна быть > 0")
        if expenses < 0:
            raise ValueError("Расходы не могут быть отрицательными")
        if expenses > salary:
            raise ValueError("Сотрудник тратит больше, чем зарабатывает и он умирает")
        self.__position = position
        self.__salary = salary
        self.__expenses = expenses

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    @property
    def expenses(self):
        return self.__expenses

    def work(self):
        """Абстрактный метод"""
        raise NotImplementedError("Наследник должен перераспределить")

    def money_inflow(self, months):
        """Сколько денег придёт за N месяцев (зарплата × N)"""
        if months <= 0:
            raise ValueError("Количество месяцев должно быть > 0")
        return self.salary * months

    def savings_until_retirement(self, retirement_age=65):
        """Сколько накопит до пенсии"""
        if self.age >= retirement_age:
            return 0
        years_left = retirement_age - self.age
        monthly_savings = self.salary - self.expenses
        return monthly_savings * 12 * years_left

    def introduce(self):
        return (f"{super().introduce()} +  должность: {self.position}, зарплата: {self.salary}")


class Manager(Employee):
    """Менеджер: список подчинённых, митинги"""

    def __init__(self, name, gender, age, position, salary, expenses):
        super().__init__(name, gender, age, position, salary, expenses)
        self.__subordinates = []

    @property
    def subordinates(self):
        return list(self.__subordinates)

    def add_subordinate(self, person):
        if not isinstance(person, Person):
            raise TypeError("Подчинённый должен быть Person")
        if person not in self.__subordinates:
            self.__subordinates.append(person)

    def remove_subordinate(self, person):
        if person in self.__subordinates:
            self.__subordinates.remove(person)

    def hold_meeting(self):
        if not self.__subordinates:
            return f"{self.name} проводит митинг, но подчинённых нет"
        names = ", ".join(p.name for p in self.__subordinates)
        return f"{self.name} проводит митинг для: {names}"

    def subordinate_count(self):
        return len(self.__subordinates)

    def work(self):
        return f"{self.name} управляет {self.subordinate_count()} подчинёнными"

    def introduce(self):
        return super().introduce()+ f" подчинённых: {self.subordinate_count()}"

class Developer(Employee):
    """Разработчик: языки программирования, пишет код."""

    def __init__(self, name, gender, age, position, salary, expenses, languages):
        """

        :param name: имя
        :param gender: пол (м/ж)
        :param age: возраст
        :param position: должность
        :param salary: зп
        :param expenses: траты
        :param languages: хотя бы один язык програмирования
        """
        super().__init__(name, gender, age, position, salary, expenses)
        if not languages:
            raise ValueError("Нужен хотя бы один язык программирования")
        self.__languages = list(languages)

    @property
    def languages(self):
        return list(self.__languages)

    def work(self):
        lang = random.choice(self.__languages)
        return f"{self.name} пишет код на {lang}"

    def introduce(self):
        langs = ", ".join(self.languages)
        return super().introduce() + f", языки: {langs}"



class Designer(Employee):
    """Дизайнер: инструменты, макеты"""

    def __init__(self, name, gender, age, position, salary, expenses, tools):
        super().__init__(name, gender, age, position, salary, expenses)
        if not tools:
            raise ValueError("Нужен хотя бы один инструмент")
        self.__tools = list(tools)

    @property
    def tools(self):
        return list(self.__tools)

    def work(self):
        tool = random.choice(self.__tools)
        return f"{self.name} создаёт макет в {tool}"

    def create_model(self):
        return self.work()

    def introduce(self):
        tools = ", ".join(self.tools)
        return super().introduce() + f" инструменты: {tools}"

#ДЕМОНСТРАЦИЯ
#1. полиморфный вызов методов красивого представления;

manager = Manager("Анна", "ж", 35, "Руководитель", 150000, 80000)
developer = Developer("Иван", "м", 28, "Разработчик", 120000, 60000,["Python", "JavaScript", "С++"])
designer = Designer("Мария", "ж", 30, "Дизайнер", 100000, 50000,["Figma", "Photoshop", "Illustrator"])

employees = [manager, developer, designer]
print("1. Представление сотрудников:")
for e in employees:
    print(f"  {e.introduce()}")

#2.полиморфный вызов метода работы, который нужно добавить в базовый класс Employee и переопределить в наследниках;

print("2. Работа сотрудников:")
for e in employees:
    print(f" {e.work()}")
#3.корректную работу super() во всей цепочке наследования.
#это видно по представлению













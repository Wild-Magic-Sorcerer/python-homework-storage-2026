#!/usr/bin/env python3

class Person:
    """Базовый класс для описания человека."""
    
    DEFAULT_GENDER_MALE = 'М'
    DEFAULT_GENDER_FEMALE = 'Ж'

    def __init__(self, name, gender, age):
        """
        Инициализация человека.
        :param name: Имя человека.
        :param gender: Пол ('М' или 'Ж').
        :param age: Возраст.
        :raises ValueError: Если имя пустое, пол некорректен или возраст вне диапазона 0-150.
        """
        if not name:
            raise ValueError("Имя не может быть пустым!")
            
        # Используем константы и кортеж вместо списка
        if gender not in (self.DEFAULT_GENDER_MALE, self.DEFAULT_GENDER_FEMALE):
            raise ValueError("Пол должен быть 'М' или 'Ж'!")
            
        if age < 0 or age > 150:
            raise ValueError("Некорректный возраст!")

        # Защищенные переменные (одно подчеркивание)
        self._name = name
        self._gender = gender
        self._age = age

    @property
    def name(self):
        """Возвращает имя человека."""
        return self._name

    @property
    def age(self):
        """Возвращает возраст человека."""
        return self._age

    def check_adulthood(self):
        """
        Проверяет, является ли человек совершеннолетним.
        :return: True, если возраст >= 18, иначе False.
        """
        return self._age >= 18

    def __str__(self):
        """
        Строковое представление человека (вместо introduce).
        :return: Строка с приветствием.
        """
        return f"Привет, меня зовут {self._name}, мне {self._age} лет, мой пол: {self._gender}."


class Employee(Person):
    """Класс сотрудника."""
    
    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Инициализация сотрудника.
        :param position: Должность.
        :param salary: Зарплата.
        :param monthly_expenses: Ежемесячные расходы.
        :raises ValueError: Если зарплата или расходы отрицательные.
        """
        super().__init__(name, gender, age)
        
        if salary < 0 or monthly_expenses < 0:
            raise ValueError("Зарплата и расходы не могут быть отрицательными!")

        self._position = position
        self._salary = salary
        self._monthly_expenses = monthly_expenses
        self._is_alive = True

    def work(self):
        """
        Абстрактный метод работы. 
        :raises NotImplementedError: Всегда, так как должен быть переопределен в наследниках.
        """
        raise NotImplementedError("Наследники должны реализовать метод work()")

    def calculate_cash_flow(self, months):
        """
        Расчет накоплений за N месяцев.
        :param months: Количество месяцев.
        :return: Строка с результатом накоплений или сообщением о смерти.
        """
        if self._monthly_expenses > self._salary:
            self._is_alive = False
            return "Сотрудник потратил больше, чем заработал, и умер от голода."

        total_income = (self._salary - self._monthly_expenses) * months
        return f"За {months} мес. накоплено: {total_income}"

    def calculate_savings_until_pension(self, pension_age=65):
        """
        Расчет накоплений до пенсии.
        :param pension_age: Пенсионный возраст (по умолчанию 65).
        :return: Строка с результатом накоплений.
        """
        if not self._is_alive:
            return "Сотрудник мертв, копить некому."

        years_left = pension_age - self._age
        if years_left <= 0:
            return "Уже на пенсии."

        months_left = years_left * 12
        if self._monthly_expenses > self._salary:
            self._is_alive = False
            return "Сотрудник умрет раньше пенсии из-за долгов."

        savings = (self._salary - self._monthly_expenses) * months_left
        return f"До пенсии осталось {years_left} лет. Накопит: {savings}"

    def __str__(self):
        """
        Строковое представление сотрудника.
        :return: Базовая информация плюс должность.
        """
        base_info = super().__str__()
        return f"{base_info} Должность: {self._position}."


class Manager(Employee):
    """Класс Менеджер."""
    
    def __init__(self, name, gender, age, position, salary, monthly_expenses, subordinates=None):
        """
        Инициализация менеджера.
        :param subordinates: Список подчиненных (по умолчанию пустой).
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._subordinates = subordinates if subordinates is not None else []

    def work(self):
        """
        Реализация метода работы.
        :return: Описание процесса работы.
        """
        return f"Менеджер {self._name} управляет процессами."

    def conduct_meeting(self):
        """
        Проведение митинга.
        :return: Описание митинга.
        """
        return f"Менеджер {self._name} проводит митинг."

    def __str__(self):
        """
        Строковое представление менеджера.
        :return: Информация о менеджере и подчиненных.
        """
        base_info = super().__str__()
        return f"{base_info} В подчинении: {len(self._subordinates)} чел."


class Developer(Employee):
    """Класс Разработчик."""
    
    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages=None):
        """
        Инициализация разработчика.
        :param languages: Список языков программирования.
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._languages = languages if languages is not None else []

    def work(self):
        """
        Реализация метода работы.
        :return: Описание процесса работы.
        """
        return f"Разработчик {self._name} пишет код."

    def write_random_code(self):
        """
        Пишет код на языке из списка.
        :return: Описание процесса написания кода.
        """
        if not self._languages:
            return "Не знает языков программирования."
        return f"Разработчик {self._name} пишет код на {self._languages[0]}."

    def __str__(self):
        """
        Строковое представление разработчика.
        :return: Информация о разработчике и его языках.
        """
        base_info = super().__str__()
        langs = ", ".join(self._languages) if self._languages else "нет"
        return f"{base_info} Языки: {langs}."


class Designer(Employee):
    """Класс Дизайнер."""
    
    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools=None):
        """
        Инициализация дизайнера.
        :param tools: Список инструментов (Figma, Photoshop и т.д.).
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self._tools = tools if tools is not None else []

    def work(self):
        """
        Реализация метода работы.
        :return: Описание процесса работы.
        """
        return f"Дизайнер {self._name} рисует макеты."

    def create_layout(self):
        """
        Создает макет.
        :return: Описание процесса создания макета.
        """
        if not self._tools:
            return "Нет инструментов для работы."
        return f"Дизайнер {self._name} создал макет, используя {self._tools[0]}."

    def __str__(self):
        """
        Строковое представление дизайнера.
        :return: Информация о дизайнере и его инструментах.
        """
        base_info = super().__str__()
        tools = ", ".join(self._tools) if self._tools else "нет"
        return f"{base_info} Инструменты: {tools}."


if __name__ == '__main__':
    print("--- Демонстрация работы ---")
    designer1 = Designer("Анна", "Ж", 25, "UX/UI", 80000, 40000, ["Figma", "Photoshop"])
    print(designer1.work())
    print(designer1)
    print(designer1.create_layout())

    print("\nПроверка, если инструментов нет:")
    designer2 = Designer("Олег", "М", 30, "Junior", 50000, 20000)
    print(designer2.create_layout())

    print("\nПроверка накоплений и СМЕРТИ:")
    print(f"Анна за 5 месяцев: {designer1.calculate_cash_flow(5)}")

    poor_guy = Developer("Вася", "М", 22, "Junior", 30000, 40000, ["Python"])
    print(f"Вася за 1 месяц: {poor_guy.calculate_cash_flow(1)}")

    print("\nРасчет до пенсии:")
    print(designer1.calculate_savings_until_pension())
    print(poor_guy.calculate_savings_until_pension())

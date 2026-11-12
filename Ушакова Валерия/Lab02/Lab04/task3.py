#!/usr/bin/env python3


class Person:
    def __init__(self, name, gender, age):
        if not name:
            raise ValueError("Имя не может быть пустым!")
        if gender not in ['М', 'Ж']:
            raise ValueError("Пол должен быть 'М' или 'Ж'!")
        if age < 0 or age > 150:
            raise ValueError("Некорректный возраст!")

        self.name = name
        self.gender = gender
        self.age = age

    def introduce(self):
        return f"Привет, меня зовут {self.name}, мне {self.age} лет, мой пол: {self.gender}."

    def check_adulthood(self):
        return self.age >= 18

    @classmethod
    def from_variables(cls, name, gender, age):
        return cls(name, gender, age)


class Employee(Person):
    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        super().__init__(name, gender, age)

        if salary < 0 or monthly_expenses < 0:
            raise ValueError("Зарплата и расходы не могут быть отрицательными!")

        self.position = position
        self.salary = salary
        self.monthly_expenses = monthly_expenses
        self.is_alive = True


    def work(self):
        raise NotImplementedError("Наследники должны реализовать метод work()")

    def calculate_cash_flow(self, months):
        if self.monthly_expenses > self.salary:
            self.is_alive = False
            return "Сотрудник потратил больше, чем заработал, и умер от голода."

        total_income = (self.salary - self.monthly_expenses) * months
        return f"За {months} мес. накоплено: {total_income}"

    def calculate_savings_until_pension(self, pension_age=65):
        if not self.is_alive:
            return "Сотрудник мертв, копить некому."

        years_left = pension_age - self.age
        if years_left <= 0:
            return "Уже на пенсии."

        months_left = years_left * 12
        if self.monthly_expenses > self.salary:
            self.is_alive = False
            return "Сотрудник умрет раньше пенсии из-за долгов."

        savings = (self.salary - self.monthly_expenses) * months_left
        return f"До пенсии ({pension_age} лет) осталось {years_left} лет. Накопит: {savings}"


class Manager(Employee):
    def __init__(self, name, gender, age, position, salary, monthly_expenses, subordinates=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def work(self):
        return f"Менеджер {self.name} управляет процессами."

    def introduce(self):
        base_info = super().introduce()
        return f"{base_info} Я менеджер, у меня {len(self.subordinates)} подчиненных."

    def conduct_meeting(self):
        return f"Менеджер {self.name} проводит работу с {len(self.subordinates)} подчиненными."


class Developer(Employee):
    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        if languages is None:
            self.languages = []
        else:
            self.languages = languages

    def work(self):
        return f"Разработчик {self.name} пишет код."

    def introduce(self):
        base_info = super().introduce()
        return f"{base_info} Я разработчик, знаю языки: {', '.join(self.languages)}."

    def write_random_code(self):
        if not self.languages:
            return "Не знает языков программирования."
        current_lang = self.languages[0]
        return f"Разработчик {self.name} пишет код на {current_lang}."


class Designer(Employee):
    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        if tools is None:
            self.tools = []
        else:
            self.tools = tools

    def work(self):
        return f"Дизайнер {self.name} рисует макеты."

    def introduce(self):
        base_info = super().introduce()
        return f"{base_info} Я дизайнер, владею инструментами: {', '.join(self.tools)}."

    def create_layout(self):
        if not self.tools:
            return "Нет инструментов для работы."
        current_tool = self.tools[0]
        return f"Дизайнер {self.name} создал макет, используя {current_tool}."


if __name__ == '__main__':
    print("1. Демонстрация работы Дизайнера")
    designer1 = Designer(
        name="Анна",
        gender="Ж",
        age=25,
        position="UX/UI",
        salary=80000,
        monthly_expenses=40000,
        tools=["Figma", "Photoshop"]
    )
    print(designer1.work(),designer1.introduce(), designer1.create_layout() )

    print("\n 2. Проверка на случай, если инструментов нет")
    designer2 = Designer("Олег", "М", 30, "Junior", 50000, 20000)
    print(designer2.create_layout())

    print("\n3. Демонстрация полиморфизма и прочего")
    manager = Manager("Алексей", "М", 35, "PM", 100000, 50000, ["Иван", "Петр"])
    developer = Developer("Ольга", "Ж", 25, "Backend", 80000, 40000, ["Python", "C++"])

    staff = [manager, developer, designer1]
    for person in staff:
        print(person.introduce())
        print(person.work())

    print("\n4. Проверка накоплений и СМЕРТИ ")
    print(f"Анна накопит за 5 месяцев: {designer1.calculate_cash_flow(5)}")
    poor_guy = Developer("Вася", "М", 22, "Junior", 30000, 40000, ["Python"])
    print(f"Вася за 1 месяц: {poor_guy.calculate_cash_flow(1)}")

    print("\n 5. Расчет до пенсии")
    print(designer1.calculate_savings_until_pension())
    print(poor_guy.calculate_savings_until_pension())
    designer2 = Designer("Андрей", "М", 30, "Junior", 50000, 20000)
    print(designer2.create_layout())

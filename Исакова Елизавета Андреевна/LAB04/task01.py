"""
Модуль для работы с транспортными средствами.
Демонстрирует наследование, инкапсуляцию и полиморфизм.
"""

class Transport:
    """Базовый класс транспортного средства."""
    def __init__(self, speed, capacity):
        """Инициализация транспорта со скоростью и ёмкостью."""
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """Возвращает скорость транспорта."""
        return self.__speed

    @speed.setter
    def speed(self, value):
        """Устанавливает скорость с валидацией."""
        if value < 0:
            raise ValueError('Скорость не может быть меньше 0!')
        self.__speed = value

    @property
    def capacity(self):
        """Возвращает ёмкость транспорта."""
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """Устанавливает ёмкость с валидацией."""
        if value < 1:
            raise ValueError('Ёмкость не может быть равна 0 и меньше!')
        self.__capacity = value

    def get_info(self):
        """Возвращает строку с основными характеристиками."""
        return f'Скорость: {self.__speed}, ёмкость: {self.__capacity}'

    def high_speed(self, limit):
        """Проверяет, превышает ли скорость заданный лимит."""
        return self.__speed > limit

    @classmethod
    def from_dict(cls, some_dict):
        """Создаёт объект транспорта из словаря."""
        some_speed = some_dict['speed']
        some_capacity = some_dict['capacity']
        return cls(some_speed, some_capacity)

class Bus(Transport):
    """Класс автобуса с маршрутом."""
    def __init__(self, speed, capacity, route):
        """Инициализация автобуса с маршрутом."""
        super().__init__(speed, capacity)
        self.__route = route

    @property
    def route(self):
        """Возвращает маршрут автобуса."""
        return self.__route

class Truck(Transport):
    """Класс грузовика с грузоподъёмностью."""
    PRICE_PER_TON = 10

    def __init__(self, speed, capacity, carrying_capacity):
        """Инициализация грузовика с грузоподъёмностью."""
        super().__init__(speed, capacity)
        self.__carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self):
        """Возвращает грузоподъёмность грузовика."""
        return self.__carrying_capacity

    def transportation_cost(self, distance):
        """Рассчитывает стоимость перевозки на заданное расстояние."""
        return distance * self.__carrying_capacity * self.PRICE_PER_TON

class Taxi(Transport):
    """Класс такси с тарифом."""
    def __init__(self, speed, capacity, tariff):
        """Инициализация такси с тарифом."""
        super().__init__(speed, capacity)
        self.__tariff = tariff

    @property
    def tariff(self):
        """Возвращает тариф такси."""
        return self.__tariff

    def cost_of_the_trip(self, distance):
        """Рассчитывает стоимость поездки на заданное расстояние."""
        return distance * self.__tariff

if __name__ == '__main__':
    print('\nСоздание объектов через конструктор')
    car1 = Transport(50, 10)
    print(car1.get_info())

    bus = Bus(60, 40, 'Дом - Университет')
    print(f"Автобус: {bus.get_info()}, маршрут: {bus.route}")

    truck = Truck(50, 10, 5)
    print(f"Грузовик: {truck.get_info()}, грузоподъёмность: {truck.carrying_capacity} т")

    taxi = Taxi(60, 4, 8)
    print(f"Такси: {taxi.get_info()}, тариф: {taxi.tariff} руб/км")

    print('\nСоздание объектов через метод from_dict')
    di_ct = {'speed': 10, 'capacity': 4}
    car2 = Transport.from_dict(di_ct)
    print(car2.get_info())

    print('\nПопытка задать недопустимые значения')
    try:
        bad_transport = Transport(-50, 10)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        bad_bus = Bus(60, 0, "№99")
    except ValueError as e:
        print(f"Ошибка: {e}")

    print('\nВызов методов без создания объекта')
    result = Transport.from_dict({'speed': 120, 'capacity': 8})
    print(result.get_info())

    print('\nПолиморфный вызов методов')
    transports = [bus, truck, taxi]

    for t in transports:
        print(t.get_info())
        print(f'Превышает ли скорость 55? {t.high_speed(55)}')

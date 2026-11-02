"""
Модуль для работы с транспортными средствами.
Демонстрирует наследование, инкапсуляцию и полиморфизм.
"""

PRICE_PER_TON = 10

class Transport:
    """Базовый класс транспортного средства."""
    def __init__(self, speed, capacity):
        """
        Инициализация транспорта со скоростью и ёмкостью.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта
        """
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        """
        Возвращает скорость транспорта.

        :return: скорость транспорта
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость с валидацией.

        :param value: значение скорости
        """
        if value < 0:
            raise ValueError('Скорость не может быть меньше 0!')
        self._speed = value

    @property
    def capacity(self):
        """
        Возвращает ёмкость транспорта.

        :return: ёмкость транспорта
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает ёмкость с валидацией.

        :param value: значение ёмкости
        """
        if value < 1:
            raise ValueError('Ёмкость не может быть равна 0 и меньше!')
        self._capacity = value

    def get_info(self):
        """
        Возвращает строку с основными характеристиками.

        :return: строка с характеристиками
        """
        return f'Скорость: {self._speed}, ёмкость: {self._capacity}'

    def high_speed(self, limit):
        """
        Проверяет, превышает ли скорость заданный лимит.

        :param limit: лимит скорости
        :return: True, если скорость превышает лимит
        """
        return self._speed > limit

    @classmethod
    def from_dict(cls, some_dict):
        """
        Создаёт объект транспорта из словаря.

        :param some_dict: словарь с данными
        :return: объект транспорта
        """
        some_speed = some_dict.get('speed')
        some_capacity = some_dict.get('capacity')
        return cls(some_speed, some_capacity)

class Bus(Transport):
    """Класс автобуса с маршрутом."""
    def __init__(self, speed, capacity, route):
        """
        Инициализация автобуса с маршрутом.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта
        :param route: маршрут автобуса
        """
        super().__init__(speed, capacity)
        self._route = route

    @property
    def route(self):
        """
        Возвращает маршрут автобуса.

        :return: маршрут автобуса
        """
        return self._route

    @route.setter
    def route(self, value):
        """
        Устанавливает маршрут автобуса.

        :param value: маршрут
        """
        self._route = value

class Truck(Transport):
    """Класс грузовика с грузоподъёмностью."""

    def __init__(self, speed, capacity, carrying_capacity):
        """
        Инициализация грузовика с грузоподъёмностью.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта
        :param carrying_capacity: грузоподъёмность
        """
        super().__init__(speed, capacity)
        self._carrying_capacity = carrying_capacity

    @property
    def carrying_capacity(self):
        """
        Возвращает грузоподъёмность грузовика.

        :return: грузоподъёмность
        """
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, value):
        """
        Устанавливает грузоподъёмность грузовика.

        :param value: грузоподъёмность
        """
        self._carrying_capacity = value

    def transportation_cost(self, distance):
        """
        Рассчитывает стоимость перевозки на заданное расстояние.

        :param distance: расстояние
        :return: стоимость перевозки
        """
        return distance * self._carrying_capacity * PRICE_PER_TON

class Taxi(Transport):
    """Класс такси с тарифом."""
    def __init__(self, speed, capacity, tariff):
        """
        Инициализация такси с тарифом.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта
        :param tariff: тариф
        """
        super().__init__(speed, capacity)
        self._tariff = tariff

    @property
    def tariff(self):
        """
        Возвращает тариф такси.

        :return: тариф
        """
        return self._tariff

    @tariff.setter
    def tariff(self, value):
        """
        Устанавливает тариф такси.

        :param value: тариф
        """
        self._tariff = value

    def cost_of_the_trip(self, distance):
        """
        Рассчитывает стоимость поездки на заданное расстояние.

        :param distance: расстояние
        :return: стоимость поездки
        """
        return distance * self._tariff

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
    transports = (bus, truck, taxi)

    for t in transports:
        print(t.get_info())
        print(f'Превышает ли скорость 55? {t.high_speed(55)}')
        

#!/usr/bin/env python3

class Transport:
    """
    Базовый класс для описания транспорта.
    Хранит скорость и ёмкость транспорта (приватные атрибуты),
    предоставляет доступ к ним через свойства с валидацией.
    """
    def __init__(self, speed, capacity):
        """
        Конструктор класса Transport.
        Параметры:
            speed (int | float): скорость транспорта (км/ч).
            capacity (int): ёмкость транспорта (количество людей/груза).
        Возвращает:
            None
        """
        self.__speed = None
        self.__capacity = None
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Свойство для чтения значения скорости.
        Параметры:
            Нет.
        Возвращает:
            int | float: текущая скорость транспорта.
        """
        return self.__speed

    @speed.setter
    def speed(self, value):
        """
        Сеттер скорости с валидацией.
        Параметры:
            value (int | float): новое значение скорости.
        Возвращает:
            None
        Исключения:
            ValueError: если значение не положительное число.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self.__speed = value

    @property
    def capacity(self):
        """
        Свойство для чтения значения ёмкости.
        Параметры:
            Нет.
        Возвращает:
            int: текущая ёмкость транспорта.
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """
        Сеттер ёмкости с валидацией.
        Параметры:
            value (int): новое значение ёмкости.
        Возвращает:
            None
        Исключения:
            ValueError: если значение не целое положительное число.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Ёмкость должна быть целым положительным числом")
        self.__capacity = value

    def get_info(self):
        """
        Возвращает строку с основными характеристиками транспорта.
        Параметры:
            Нет.
        Возвращает:
            str: строка с описанием скорости и ёмкости.
        """
        return f"Скорость: {self.speed} км/ч, Ёмкость: {self.capacity}"

    def is_faster_than(self, threshold):
        """
        Проверяет, превышает ли скорость транспорта заданное значение.
        Параметры:
            threshold (int | float): пороговое значение скорости.
        Возвращает:
            bool: True, если скорость больше порога, иначе False.
        """
        return self.speed > threshold

    @classmethod
    def from_dict(cls, data):
        """
        Классовый метод для создания объекта Transport из словаря.
        Параметры:
            data (dict): словарь с ключами 'speed' и 'capacity'.
        Возвращает:
            Transport: новый объект класса Transport.
        """
        return cls(data["speed"], data["capacity"])


class Bus(Transport):
    """
    Класс автобуса, наследующий Transport.
    Добавляет маршрут автобуса.
    """
    def __init__(self, speed, capacity, route):
        """
        Конструктор класса Bus.
        Параметры:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            route (str): маршрут автобуса.
        Возвращает:
            None
        """
        super().__init__(speed, capacity)
        self.__route = route

    @property
    def route(self):
        """
        Свойство для чтения маршрута.
        Параметры:
            Нет.
        Возвращает:
            str: маршрут автобуса.
        """
        return self.__route

    @route.setter
    def route(self, value):
        """
        Сеттер маршрута с валидацией.
        Параметры:
            value (str): новый маршрут.
        Возвращает:
            None
        Исключения:
            ValueError: если маршрут пустой.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Маршрут должен быть непустой строкой")
        self.__route = value

    def get_info(self):
        """
        Возвращает расширенную информацию об автобусе (включая маршрут).
        Параметры:
            Нет.
        Возвращает:
            str: строка с характеристиками и маршрутом.
        """
        return f"{super().get_info()}, Маршрут: {self.route}"


class Truck(Transport):
    """
    Класс грузовика, наследующий Transport.
    Добавляет грузоподъёмность и расчёт стоимости перевозки.
    """
    def __init__(self, speed, capacity, load_capacity, price_per_ton_km):
        """
        Конструктор класса Truck.
        Параметры:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            load_capacity (int | float): грузоподъёмность в тоннах.
            price_per_ton_km (int | float): цена за тонно-километр.
        Возвращает:
            None
        """
        super().__init__(speed, capacity)
        self.__load_capacity = load_capacity
        self.__price_per_ton_km = price_per_ton_km

    @property
    def load_capacity(self):
        """
        Свойство для чтения грузоподъёмности.
        Параметры:
            Нет.
        Возвращает:
            int | float: грузоподъёмность в тоннах.
        """
        return self.__load_capacity

    def calculate_transport_cost(self, distance_km, weight_tons):
        """
        Рассчитывает стоимость перевозки груза.
        Параметры:
            distance_km (int | float): расстояние в км.
            weight_tons (int | float): вес груза в тоннах.
        Возвращает:
            float: стоимость перевозки.
        Исключения:
            ValueError: если вес груза превышает грузоподъёмность.
        """
        if weight_tons > self.load_capacity:
            raise ValueError("Вес груза превышает грузоподъёмность")
        return distance_km * weight_tons * self.__price_per_ton_km

    def get_info(self):
        """
        Возвращает расширенную информацию о грузовике.
        Параметры:
            Нет.
        Возвращает:
            str: строка с характеристиками и грузоподъёмностью.
        """
        return f"{super().get_info()}, Грузоподъёмность: {self.load_capacity} т"


class Taxi(Transport):
    """
    Класс такси, наследующий Transport.
    Добавляет тариф и расчёт стоимости поездки.
    """

    def __init__(self, speed, capacity, tariff_per_km):
        """
        Конструктор класса Taxi.
        Параметры:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            tariff_per_km (int | float): тариф за км.
        Возвращает:
            None
        """
        super().__init__(speed, capacity)
        self.__tariff_per_km = tariff_per_km

    @property
    def tariff_per_km(self):
        """
        Свойство для чтения тарифа за км.
        Параметры:
            Нет.
        Возвращает:
            int | float: тариф за километр.
        """
        return self.__tariff_per_km

    def calculate_ride_cost(self, distance_km):
        """
        Рассчитывает стоимость поездки.
        Параметры:
            distance_km (int | float): расстояние в км.
        Возвращает:
            float: стоимость поездки.
        """
        return distance_km * self.tariff_per_km

    def get_info(self):
        """
        Возвращает расширенную информацию о такси.
        Параметры:
            Нет.
        Возвращает:
            str: строка с характеристиками и тарифом.
        """
        return f"{super().get_info()}, Тариф: {self.tariff_per_km} за км"

if __name__ == "__main__":
    bus = Bus(60, 40, "Маршрут №5")
    print(bus.get_info())
    truck_data = {"speed": 80, "capacity": 2}
    truck_base = Transport.from_dict(truck_data)
    print("Transport из словаря:", truck_base.get_info())
    try:
        bus.speed = -10
    except ValueError as e:
        print("Ошибка скорости:", e)
    try:
        bus.capacity = 0
    except ValueError as e:
        print("Ошибка ёмкости:", e)
    print("Проверка метода is_faster_than без объекта:", Transport.is_faster_than.__name__)
    taxi = Taxi(90, 4, 25)
    truck = Truck(70, 1, 10, 5)
    transports = [bus, truck, taxi]
    for t in transports:
        print(t.get_info())
    print("Truck быстрее 50 км/ч?", truck.is_faster_than(50))
    print("Стоимость перевозки:", truck.calculate_transport_cost(100, 5))
    print("Стоимость поездки такси:", taxi.calculate_ride_cost(10))

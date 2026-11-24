#!/usr/bin/env python3

DEFAULT_SPEED = 60
DEFAULT_CAPACITY = 10

class Transport:
    """
    Базовый класс для описания транспорта.

    Attributes:
        _speed: скорость транспорта (км/ч).
        _capacity: ёмкость транспорта.
    """

    def __init__(self, speed, capacity):
        """
        Конструктор класса Transport.

        Args:
            speed (int | float): скорость транспорта (км/ч).
            capacity (int): ёмкость транспорта.

        Returns:
            None

        Raises:
            ValueError: если speed не положительное число или capacity
                        не целое положительное число.
        """
        self._speed = None
        self._capacity = None
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Свойство для чтения значения скорости.

        Args:
            None

        Returns:
            int | float: текущая скорость транспорта.
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Сеттер скорости с валидацией.

        Args:
            value (int | float): новое значение скорости.

        Returns:
            None

        Raises:
            ValueError: если значение не положительное число.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Скорость должна быть положительным числом")
        self._speed = value

    @property
    def capacity(self):
        """
        Свойство для чтения значения ёмкости.

        Args:
            None

        Returns:
            int: текущая ёмкость транспорта.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Сеттер ёмкости с валидацией.

        Args:
            value (int): новое значение ёмкости.

        Returns:
            None

        Raises:
            ValueError: если значение не целое положительное число.
        """
        if type(value) is not int or value <= 0:
            raise ValueError("Ёмкость должна быть целым положительным числом")
        self._capacity = value

    def __str__(self):
        """
        Возвращает строковое представление транспорта.

        Args:
            None

        Returns:
            str: строка с описанием скорости и ёмкости.
        """
        return f"Скорость: {self.speed} км/ч, Ёмкость: {self.capacity}"

    def is_faster_than(self, threshold):
        """
        Проверяет, превышает ли скорость транспорта заданное значение.

        Args:
            threshold (int | float): пороговое значение скорости.

        Returns:
            bool: True, если скорость больше порога, иначе False.
        """
        return self.speed > threshold

    @classmethod
    def from_dict(cls, data):
        """
        Классовый метод для создания объекта Transport из словаря.

        Args:
            data (dict): словарь с ключами 'speed' и 'capacity'.

        Returns:
            Transport: новый объект класса Transport.
        """
        speed = data.get("speed", DEFAULT_SPEED)
        capacity = data.get("capacity", DEFAULT_CAPACITY)
        return cls(speed, capacity)


class Bus(Transport):
    """
    Класс автобуса, наследующий Transport.
    Добавляет маршрут автобуса.

    Attributes:
        _route: маршрут автобуса.
    """

    def __init__(self, speed, capacity, route):
        """
        Конструктор класса Bus.

        Args:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            route (str): маршрут автобуса.

        Returns:
            None

        Raises:
            ValueError: если маршрут пустой.
        """
        super().__init__(speed, capacity)
        self.route = route

    @property
    def route(self):
        """
        Свойство для чтения маршрута.

        Args:
            None

        Returns:
            str: маршрут автобуса.
        """
        return self._route

    @route.setter
    def route(self, value):
        """
        Сеттер маршрута с валидацией.

        Args:
            value (str): новый маршрут.

        Returns:
            None

        Raises:
            ValueError: если маршрут пустой.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Маршрут должен быть непустой строкой")
        self._route = value

    def __str__(self):
        """
        Возвращает расширенную строку об автобусе.

        Args:
            None

        Returns:
            str: строка с характеристиками и маршрутом.
        """
        return f"{super().__str__()}, Маршрут: {self.route}"


class Truck(Transport):
    """
    Класс грузовика, наследующий Transport.
    Добавляет грузоподъёмность и расчёт стоимости перевозки.

    Attributes:
        _load_capacity: грузоподъёмность в тоннах.
        _price_per_ton_km: цена за тонно-километр.
    """

    def __init__(self, speed, capacity, load_capacity, price_per_ton_km):
        """
        Конструктор класса Truck.

        Args:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            load_capacity (int | float): грузоподъёмность в тоннах.
            price_per_ton_km (int | float): цена за тонно-километр.

        Returns:
            None
        """
        super().__init__(speed, capacity)
        self._load_capacity = load_capacity
        self._price_per_ton_km = price_per_ton_km

    @property
    def load_capacity(self):
        """
        Свойство для чтения грузоподъёмности.

        Args:
            None

        Returns:
            int | float: грузоподъёмность в тоннах.
        """
        return self._load_capacity

    def calculate_transport_cost(self, distance_km, weight_tons):
        """
        Рассчитывает стоимость перевозки груза.

        Args:
            distance_km (int | float): расстояние в км.
            weight_tons (int | float): вес груза в тоннах.

        Returns:
            float: стоимость перевозки.

        Raises:
            ValueError: если вес груза превышает грузоподъёмность.
        """
        if weight_tons > self.load_capacity:
            raise ValueError("Вес груза превышает грузоподъёмность")
        return distance_km * weight_tons * self._price_per_ton_km

    def __str__(self):
        """
        Возвращает расширенную строку о грузовике.

        Args:
            None

        Returns:
            str: строка с характеристиками и грузоподъёмностью.
        """
        return f"{super().__str__()}, Грузоподъёмность: {self.load_capacity} т"


class Taxi(Transport):
    """
    Класс такси, наследующий Transport.
    Добавляет тариф и расчёт стоимости поездки.

    Attributes:
        _tariff_per_km: тариф за километр.
    """

    def __init__(self, speed, capacity, tariff_per_km):
        """
        Конструктор класса Taxi.

        Args:
            speed (int | float): скорость.
            capacity (int): ёмкость.
            tariff_per_km (int | float): тариф за км.

        Returns:
            None
        """
        super().__init__(speed, capacity)
        self._tariff_per_km = tariff_per_km

    @property
    def tariff_per_km(self):
        """
        Свойство для чтения тарифа за км.

        Args:
            None

        Returns:
            int | float: тариф за километр.
        """
        return self._tariff_per_km

    def calculate_ride_cost(self, distance_km):
        """
        Рассчитывает стоимость поездки.

        Args:
            distance_km (int | float): расстояние в км.

        Returns:
            float: стоимость поездки.
        """
        return distance_km * self.tariff_per_km

    def __str__(self):
        """
        Возвращает расширенную строку о такси.

        Args:
            None

        Returns:
            str: строка с характеристиками и тарифом.
        """
        return f"{super().__str__()}, Тариф: {self.tariff_per_km} за км"


if __name__ == "__main__":
    bus = Bus(60, 40, "Маршрут №5")
    print(bus)

    truck_data = {"speed": 80, "capacity": 2}
    truck_base = Transport.from_dict(truck_data)
    print("Transport из словаря:", truck_base)

    try:
        bus.speed = -10
    except ValueError as e:
        print("Ошибка скорости:", e)

    try:
        bus.capacity = 0
    except ValueError as e:
        print("Ошибка ёмкости:", e)

    taxi = Taxi(90, 4, 25)
    truck = Truck(70, 1, 10, 5)
    transports = [bus, truck, taxi]

    for t in transports:
        print(t)

    print("Truck быстрее 50 км/ч?", truck.is_faster_than(50))
    print("Стоимость перевозки:", truck.calculate_transport_cost(100, 5))
    print("Стоимость поездки такси:", taxi.calculate_ride_cost(10))
    

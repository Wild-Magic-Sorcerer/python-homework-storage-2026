#!/usr/bin/env python3


class Transport:
    """Класс для описания транспортного средства."""

    FAST_THRESHOLD = 100

    def __init__(self, speed, capacity):
        """
        Инициализация транспорта.

        :param speed: Скорость.
        :param capacity: Вместимость.
        :raises ValueError: Если скорость или вместимость отрицательные.
        """
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        if capacity < 0:
            raise ValueError("Вместимость не может быть отрицательной!")

        self.__speed = speed
        self.__capacity = capacity

    @property
    def speed(self):
        """Возвращает скорость."""
        return self.__speed

    @property
    def capacity(self):
        """Возвращает вместимость."""
        return self.__capacity

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость.
        :param value: Новая скорость.
        :raises ValueError: Если значение отрицательное.
        """
        if value < 0:
            raise ValueError("Ошибка: Скорость не может быть отрицательной!")
        self.__speed = value

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает вместимость.
        :param value: Новая вместимость.
        :raises ValueError: Если значение отрицательное.
        """
        if value < 0:
            raise ValueError("Ошибка: Вместимость не может быть отрицательной!")
        self.__capacity = value

    def is_fast(self, threshold=None):
        """
        Проверяет скорость.
        :param threshold: Порог (по умолчанию FAST_THRESHOLD).
        :return: True или False.
        """
        if threshold is None:
            threshold = self.FAST_THRESHOLD
        return self.speed > threshold

    @classmethod
    def from_dict(cls, data: dict):
        """
        Создает объект из словаря.
        :param data: Словарь.
        :return: Объект Transport.
        """
        return cls(data.get('speed', 0), data.get('capacity', 0))

    def __str__(self):
        """Возвращает строковое представление (вместо get_info)."""
        return f"Скорость: {self.speed} км/ч, Вместимость: {self.capacity} чел."


class Bus(Transport):
    def __init__(self, speed, capacity, route):
        """
        Инициализация автобуса.
        :param route: Маршрут.
        """
        super().__init__(speed, capacity)
        self._route = route 
    def __str__(self):
        base_info = super().__str__()
        return f"Автобус: {base_info}, Маршрут: {self._route}"


class Truck(Transport):
    def __init__(self, speed, capacity, payload):
        """
        Инициализация грузовика.
        :param payload: Грузоподъемность.
        """
        super().__init__(speed, capacity)
        self._payload = payload

    def __str__(self):
        base_info = super().__str__()
        return f"Грузовик: {base_info}, Грузоподъемность: {self._payload} т."

    def calc_shipping_cost(self, distance, price_per_km_ton=15):
        """1            Расчет стоимости.
        :param distance: Расстояние.
        :param price_per_km_ton: Цена за км/тонну.
        :return: Стоимость.
        """
        return distance * self._payload * price_per_km_ton


class Taxi(Transport):
    def __init__(self, speed, capacity, tariff):
        """
        Инициализация такси.
        :param tariff: Тариф.
        """
        super().__init__(speed, capacity)
        self._tariff = tariff

    def __str__(self):
        base_info = super().__str__()
        return f"Такси: {base_info}, Тариф: {self._tariff} руб/км."

    def calc_trip_cost(self, distance):
        """
        Расчет стоимости поездки.
        :param distance: Расстояние.
        :return: Стоимость.
        """
        return distance * self._tariff


if __name__ == '__main__':
    print("1. Создание через конструктор и через классовый метод ")
    my_car = Transport(90, 5)
    print(f"Конструктор: {my_car}")

    data = {'speed': 120, 'capacity': 3}
    fast_car = Transport.from_dict(data)
    print(f"Из словаря: {fast_car}")

    print("\n2. Попытка задать недопустимую скорость/вместимость")
    try:
        Transport(-50, 5)
    except ValueError as e:
        print(f" {e}")

    try:
        Transport(50, -5)
    except ValueError as e:
        print(f" {e}")

    print("\n3. Вызов методов без создания объекта")
    auto_from_class = Transport.from_dict({'speed': 60, 'capacity': 20})
    print(f"Создано без прямого вызова конструктора: {auto_from_class}")

    print("\n4. Полиморфный вызов методов")
    bus1 = Bus(70, 40, "Маршрут №30")
    truck1 = Truck(80, 2, 10)
    taxi1 = Taxi(100, 4, 30)

    transport_list = (bus1, truck1, taxi1)

    for t in transport_list:
        print(t)

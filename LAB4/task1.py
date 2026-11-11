#!/usr/bin/env python3
# Задание 1 — Transport / Bus / Truck / Taxi
from abc import ABC

SPEED_MAX = 280
CAP_MAX = 180


class Transport:
    """
    Класс транспортного средства.

    :param speed: скорость транспорта (км/ч)
    :param capacity: вместимость транспорта (количество мест)
    """
    def __init__(self, speed, capacity):
        self.__speed = 0
        self.__capacity = 2
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Возвращает текущую скорость транспорта.
        """
        return self.__speed

    @speed.setter
    def speed(self, v):
        """
        Устанавливает скорость с проверкой диапазона 10..SPEED_MAX.

        :param v: новое значение скорости
        """
        try:
            v = int(v)
        except (TypeError, ValueError):
            print("Скорость должна быть целым числом"); return
        if not 10 <= v <= SPEED_MAX:
            print(f"Скорость от 10 до {SPEED_MAX}"); return
        self.__speed = v

    @property
    def capacity(self):
        """
        Возвращает текущую вместимость транспорта.
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, v):
        """
        Устанавливает вместимость с проверкой диапазона 2..CAP_MAX.

        :param v: новое значение вместимости
        """
        try:
            v = int(v)
        except (TypeError, ValueError):
            print("Вместимость должна быть целым числом"); return
        if not 2 <= v <= CAP_MAX:
            print(f"Вместимость от 2 до {CAP_MAX}"); return
        self.__capacity = v

    def get_info(self):
        """
        Возвращает строку с характеристиками транспорта.

        :return: строка с описанием
        """
        return f"Скорость: {self.__speed} км/ч\nМест: {self.__capacity}"

    def is_speed_exceeded(self, mark):
        """
        Проверяет, превышает ли скорость заданную отметку.

        :param mark: пороговое значение скорости
        :return: True, если скорость выше порога
        """
        return self.__speed > mark

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект Transport из словаря.

        :param data: словарь с ключами speed и capacity
        :return: новый объект Transport
        """
        return cls(data["speed"], data["capacity"])


class Bus(Transport):
    """
    Автобус — наследник Transport.

    :param speed: скорость (км/ч)
    :param capacity: вместимость (мест)
    :param route: маршрут автобуса
    """
    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.__route = route

    @property
    def route(self):
        """
        Возвращает маршрут автобуса.
        """
        return self.__route

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект Bus из словаря.

        :param data: словарь с ключами speed, capacity, route
        :return: новый объект Bus
        """
        return cls(data["speed"], data["capacity"], data["route"])

    def get_info(self):
        """
        Возвращает строку с характеристиками автобуса.

        :return: строка с описанием
        """
        return f"{super().get_info()},\nМаршрут: {self.__route}"


class Truck(Transport):
    """
    Грузовик — наследник Transport.

    :param speed: скорость (км/ч)
    :param capacity: вместимость (мест)
    :param load_capacity: грузоподъёмность (т)
    """
    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    @staticmethod
    def calculate_delivery_cost(distance, price_per_km):
        """
        Рассчитывает стоимость перевозки.

        :param distance: расстояние (км)
        :param price_per_km: цена за километр
        :return: стоимость перевозки
        """
        return distance * price_per_km

    def get_info(self):
        """
        Возвращает строку с характеристиками грузовика.

        :return: строка с описанием
        """
        return f"{super().get_info()},\nГрузоподъёмность: {self.load_capacity} т"

class Taxi(Transport):
    """
    Такси — наследник Transport.

    :param speed: скорость (км/ч)
    :param capacity: вместимость (мест)
    :param rate: тариф за километр
    """
    def __init__(self, speed, capacity, rate):
        super().__init__(speed, capacity)
        self.rate = rate

    def calculate_trip_cost(self, distance):
        """
        Рассчитывает стоимость поездки.

        :param distance: расстояние (км)
        :return: стоимость поездки
        """
        return distance * self.rate

    def get_info(self):
        """
        Возвращает строку с характеристиками такси.

        :return: строка с описанием
        """
        return f"{super().get_info()},\nТариф: {self.rate} руб./км"


if __name__ == "__main__":
    print("Создание объектов:")
    bus = Bus(80, 60, "Москва — Тула")
    truck = Truck(50, 2, 13.2)
    taxi = Taxi(90, 4, 25.5)
    for t in (bus, truck, taxi):
        print(t.get_info())

    print("\nИз словаря:")
    print(Bus.from_dict({"speed": 72, "capacity": 48, "route": "Москва — Калуга"}).get_info())
    print(Transport.from_dict({"speed": 110, "capacity": 5}).get_info())

    print("\nНекорректные данные:")
    print(Transport(5, 1).get_info())
    print(Transport(999, 22).get_info())

    print("\nВызов без объекта:")
    try:
        Transport.get_info()
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\nПолиморфизм:")
    fleet = [bus, truck, taxi]
    for t in fleet:
        print("--", t.get_info())

    print("\nПревышение скорости (70):")
    for t in fleet:
        print(f"- {t.__class__.__name__}: {'да' if t.is_speed_exceeded(70) else 'нет'}")

    print("\nСтоимость:")
    print(f"Грузовик 180 км: {truck.calculate_delivery_cost(180, 20.5)} руб.")
    print(f"Такси 120 км: {taxi.calculate_trip_cost(120)} руб.")
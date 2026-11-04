#!/usr/bin/env python3

min_speed = 0
min_capacity = 1
speed_threshold = 60


class Transport:
    """Базовый класс транспорта."""

    def __init__(self, speed, capacity):
        """Инициализация с проверкой."""
        if speed < min_speed:
            raise ValueError("скорость не может быть отрицательной")
        if capacity < min_capacity:
            raise ValueError("ёмкость должна быть больше нуля")
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        return self._speed

    @property
    def capacity(self):
        return self._capacity

    def get_info(self):
        """Выводит характеристики транспорта."""
        return f"транспорт: скорость {self.speed} км/ч, ёмкость {self.capacity} чел."

    def is_fast(self):
        return self.speed > speed_threshold

    @classmethod
    def from_dict(cls, data):
        return cls(data["speed"], data["capacity"])


class Bus(Transport):
    """Автобус."""

    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.route = route

    def get_info(self):
        return f"автобус. {super().get_info()}. маршрут: {self.route}"


class Truck(Transport):
    """Грузовик."""

    def __init__(self, speed, capacity, max_weight, cost_per_km):
        super().__init__(speed, capacity)
        self.max_weight = max_weight
        self.cost_per_km = cost_per_km

    @classmethod
    def from_dict(cls, data):
        return cls(data["speed"], data["capacity"], data["max_weight"], data["cost_per_km"])

    def calculate_delivery_cost(self, distance):
        return distance * self.cost_per_km

    def get_info(self):
        return f"грузовик. {super().get_info()}. грузоподъёмность: {self.max_weight} т."


class Taxi(Transport):
    """Такси."""

    def __init__(self, speed, capacity, tariff):
        super().__init__(speed, capacity)
        self.tariff = tariff

    def calculate_trip_cost(self, distance):
        return distance * self.tariff

    def get_info(self):
        return f"такси. {super().get_info()}. тариф: {self.tariff} руб/км."


if __name__ == "__main__":
    # 1. Создание через конструктор
    avtobus = Bus(50, 30, "№15")
    taksi = Taxi(80, 4, 20)

    # 2. Создание через классовый метод
    gruzovik = Truck.from_dict({"speed": 70, "capacity": 2, "max_weight": 10, "cost_per_km": 50})
    print(f"Создан грузовик: {gruzovik.get_info()}")

    # 3. Вызов метода БЕЗ создания объекта (сразу у класса)
    print(f"\nВызов from_dict напрямую у класса: {Transport.from_dict({'speed': 10, 'capacity': 5}).get_info()}")

    # 4. Попытка задать недопустимые значения
    print("\n--- проверки ошибок ---")
    try:
        Bus(-10, 30, "№1")
    except ValueError as oshibka:
        print(f"ошибка скорости: {oshibka}")

    try:
        Bus(50, 0, "№2")
    except ValueError as oshibka:
        print(f"ошибка ёмкости: {oshibka}")

    # 5. Полиморфный вызов
    print("\n--- полиморфизм ---")
    for transport in [avtobus, gruzovik, taksi]:
        print(transport.get_info())
        if transport.is_fast():
            print("  -> быстрый!")

#!/usr/bin/env python3


class Transport:
    def __init__(self, speed, capacity):
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        if capacity < 0:
            raise ValueError("Вместимость не может быть отрицательной!")

        self.__speed = speed
        self.__capacity = capacity

    @property
    def speed(self):
        return self.__speed

    @property
    def capacity(self):
        return self.__capacity

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Ошибка: Скорость не может быть отрицательной!")
        self.__speed = value

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Ошибка: Вместимость не может быть отрицательной!")
        self.__capacity = value

    def get_info(self):
        return f"Скорость: {self.speed} км/ч, Вместимость: {self.capacity} чел."

    def is_fast(self, threshold=100):
        return self.speed > threshold

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('speed', 0), data.get('capacity', 0))


class Bus(Transport):
    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.route = route

    def get_info(self):
        base_info = super().get_info()
        return f"Автобус: {base_info}, Маршрут: {self.route}"


class Truck(Transport):
    def __init__(self, speed, capacity, payload):
        super().__init__(speed, capacity)
        self.payload = payload

    def get_info(self):
        base_info = super().get_info()
        return f"Грузовик: {base_info}, Грузоподъемность: {self.payload} т."

    # Уникальный метод расчета стоимости перевозки
    def calc_shipping_cost(self, distance, price_per_km_ton=15):
        return distance * self.payload * price_per_km_ton


class Taxi(Transport):
    def __init__(self, speed, capacity, tariff):
        super().__init__(speed, capacity)
        self.tariff = tariff

    def get_info(self):
        base_info = super().get_info()
        return f"Такси: {base_info}, Тариф: {self.tariff} руб/км."

    def calc_trip_cost(self, distance):
        return distance * self.tariff


if __name__ == '__main__':
    print("1. Создание через конструктор и через классовый метод ")
    my_car = Transport(90, 5)
    print(f"Конструктор: {my_car.get_info()}")

    data = {'speed': 120, 'capacity': 3}
    fast_car = Transport.from_dict(data)
    print(f"Из словаря: {fast_car.get_info()}")

    print("\n 2. Попытка задать недопустимую скорость/вместимость")
    try:
        Transport(-50, 5)
    except ValueError as e:
        print(f" {e}")

    try:
        Transport(50, -5)
    except ValueError as e:
        print(f" {e}")

    print("\n 3. Вызов методов без создания объекта")
    auto_from_class = Transport.from_dict({'speed': 60, 'capacity': 20})
    print(f"Создано без прямого вызова конструктора: {auto_from_class.get_info()}")

    print("\n4. Полиморфный вызов методов")
    bus1 = Bus(70, 40, "Маршрут №30")
    truck1 = Truck(80, 2, 10)
    taxi1 = Taxi(100, 4, 30)

    transport_list = [bus1, truck1, taxi1]
    for t in transport_list:
        print(t.get_info())

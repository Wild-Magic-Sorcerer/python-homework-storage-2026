#!/usr/bin/env python3
TRUCK_RATE = 50
SPEED_LIMIT = 90


class Transport:
    """
    Транспортное средство со скоростью и вместимостью.
    """

    def __init__(self, speed: int, capacity: int) -> None:
        """
        Создаёт транспорт, проверяя скорость и вместимость.

        :param speed: Максимальная скорость, км/ч
        :param capacity: Вместимость, число мест
        """
        self.speed = speed
        self.capacity = capacity

    @staticmethod
    def check_positive(value: int, name: str) -> int:
        """
        Проверяет, что значение целое и больше нуля.

        :param value: Проверяемое значение
        :param name: Название величины для сообщения об ошибке
        :return: То же значение, если оно прошло проверку
        """
        if type(value) is not int or value <= 0:
            raise ValueError(name + ": ожидается целое число больше нуля, "
                             + "получено " + repr(value))
        return value

    @property
    def speed(self) -> int:
        """
        Максимальная скорость, км/ч.

        :return: Скорость
        """
        return self.__speed

    @speed.setter
    def speed(self, value: int) -> None:
        """
        Обновляет скорость после проверки.

        :param value: Новое значение
        :return: Ничего не возвращает (None)
        """
        self.__speed = self.check_positive(value, "Скорость")

    @property
    def capacity(self) -> int:
        """
        Вместимость, число мест.

        :return: Вместимость
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """
        Обновляет вместимость после проверки.

        :param value: Новое значение
        :return: Ничего не возвращает (None)
        """
        self.__capacity = self.check_positive(value, "Вместимость")

    def __str__(self) -> str:
        """
        Собирает строку с основными характеристиками.

        :return: Строка с названием класса, скоростью и вместимостью
        """
        speed = f"скорость {self.__speed} км/ч"
        return f"{type(self).__name__}: {speed}, мест {self.__capacity}"

    def is_speeding(self, limit: int) -> bool:
        """
        Проверяет, превышает ли скорость заданную отметку.

        :param limit: Отметка скорости, км/ч
        :return: True, если скорость строго больше отметки
        """
        return self.__speed > limit

    @classmethod
    def from_dict(cls, data: dict) -> "Transport":
        """
        Создаёт объект из словаря с ключами speed и capacity.

        :param data: Словарь с характеристиками
        :return: Новый объект того класса, от которого вызван метод
        """
        return cls(data.get("speed"), data.get("capacity"))


class Bus(Transport):
    """
    Автобус с маршрутом из остановок.
    """

    def __init__(self, speed: int, capacity: int) -> None:
        """
        Создаёт автобус без маршрута.

        :param speed: Максимальная скорость, км/ч
        :param capacity: Число мест
        """
        super().__init__(speed, capacity)
        self.__route = []

    def make_route(self, stops: list[str]) -> None:
        """
        Задаёт маршрут автобуса по списку остановок.

        :param stops: Непустой список названий остановок
        :return: Ничего не возвращает (None)
        """
        self.route = stops

    @property
    def route(self) -> list[str]:
        """
        Остановки маршрута.

        :return: Список остановок автобуса
        """
        return self.__route

    @route.setter
    def route(self, value: list[str]) -> None:
        """
        Обновляет маршрут после проверки.

        :param value: Новое значение
        :return: Ничего не возвращает (None)
        """
        if not isinstance(value, list) or not value:
            raise ValueError("Маршрут должен содержать хотя бы одну остановку")
        for stop in value:
            if not isinstance(stop, str) or not stop.strip():
                raise ValueError("Остановка должна иметь непустое название")
        self.__route = [stop.strip() for stop in value]

    def __str__(self) -> str:
        """
        Добавляет к характеристикам маршрут.

        :return: Строка родителя и маршрут через тире
        """
        if self.__route:
            route = " - ".join(self.__route)
        else:
            route = "не задан"
        return super().__str__() + ", маршрут " + route

    @classmethod
    def from_dict(cls, data: dict) -> "Bus":
        """
        Создаёт автобус из словаря, ключ route необязателен.

        :param data: Словарь с ключами speed, capacity и route
        :return: Новый автобус
        """
        bus = cls(data.get("speed"), data.get("capacity"))
        if "route" in data:
            bus.make_route(data.get("route"))
        return bus


class Truck(Transport):
    """
    Грузовик с грузоподъёмностью и расчётом стоимости перевозки.
    """

    def __init__(self, speed: int, capacity: int, load_capacity: int) -> None:
        """
        Создаёт грузовик, проверяя грузоподъёмность.

        :param speed: Максимальная скорость, км/ч
        :param capacity: Число мест в кабине
        :param load_capacity: Грузоподъёмность, тонн
        """
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self) -> int:
        """
        Грузоподъёмность, тонн.

        :return: Грузоподъёмность
        """
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, value: int) -> None:
        """
        Обновляет грузоподъёмность после проверки.

        :param value: Новое значение
        :return: Ничего не возвращает (None)
        """
        self.__load_capacity = self.check_positive(value, "Грузоподъёмность")

    def delivery_cost(self, distance: int, weight: int) -> int:
        """
        Считает стоимость перевозки груза.

        :param distance: Расстояние, км
        :param weight: Вес груза, тонн, не больше грузоподъёмности
        :return: Стоимость в рублях по тарифу за тонно-километр
        """
        self.check_positive(distance, "Расстояние")
        self.check_positive(weight, "Вес груза")
        if weight > self.__load_capacity:
            raise ValueError("Вес груза " + str(weight) + " т больше "
                             + "грузоподъёмности "
                             + str(self.__load_capacity) + " т")
        return distance * weight * TRUCK_RATE

    def __str__(self) -> str:
        """
        Добавляет к характеристикам грузоподъёмность.

        :return: Строка родителя и грузоподъёмность
        """
        capacity = f"грузоподъёмность {self.__load_capacity} т"
        return f"{super().__str__()}, {capacity}"

    @classmethod
    def from_dict(cls, data: dict) -> "Truck":
        """
        Создаёт грузовик из словаря.

        :param data: Словарь с ключами speed, capacity и load_capacity
        :return: Новый грузовик
        """
        return cls(data.get("speed"), data.get("capacity"),
                   data.get("load_capacity"))


class Taxi(Transport):
    """
    Такси с тарифом и расчётом стоимости поездки.
    """

    def __init__(self, speed: int, capacity: int, tariff: int) -> None:
        """
        Создаёт такси, проверяя тариф.

        :param speed: Максимальная скорость, км/ч
        :param capacity: Число мест для пассажиров
        :param tariff: Тариф, рублей за километр
        """
        super().__init__(speed, capacity)
        self.tariff = tariff

    @property
    def tariff(self) -> int:
        """
        Тариф, рублей за километр.

        :return: Тариф
        """
        return self.__tariff

    @tariff.setter
    def tariff(self, value: int) -> None:
        """
        Обновляет тариф после проверки.

        :param value: Новое значение
        :return: Ничего не возвращает (None)
        """
        self.__tariff = self.check_positive(value, "Тариф")

    def trip_cost(self, distance: int) -> int:
        """
        Считает стоимость поездки.

        :param distance: Расстояние, км
        :return: Стоимость в рублях
        """
        self.check_positive(distance, "Расстояние")
        return distance * self.__tariff

    def __str__(self) -> str:
        """
        Добавляет к характеристикам тариф.

        :return: Строка родителя и тариф
        """
        return f"{super().__str__()}, тариф {self.__tariff} руб/км"

    @classmethod
    def from_dict(cls, data: dict) -> "Taxi":
        """
        Создаёт такси из словаря.

        :param data: Словарь с ключами speed, capacity и tariff
        :return: Новое такси
        """
        return cls(data.get("speed"), data.get("capacity"), data.get("tariff"))


if __name__ == "__main__":
    bus = Bus(80, 40)
    bus.make_route(["Вокзал", "Рынок", "Университет"])
    truck = Truck(90, 2, 10)
    taxi = Taxi.from_dict({"speed": 120, "capacity": 4, "tariff": 35})
    print("Через конструктор:", bus)
    print("Через конструктор:", truck)
    print("Через from_dict:", taxi)
    print("Маршрут автобуса:", bus.route)
    print("Перевозка 8 т на 150 км:", truck.delivery_cost(150, 8), "руб")
    print("Поездка на такси 12 км:", taxi.trip_cost(12), "руб")
    print()
    print("Недопустимые значения:")
    for speed, capacity in [(0, 4), (120, -5), ("быстро", 4)]:
        try:
            Transport(speed, capacity)
        except ValueError as error:
            print("  ValueError:", error)
    bus.speed = 85
    try:
        bus.speed = -10
    except ValueError as error:
        print("  ValueError:", error)
    print("Скорость после попытки записать -10:", bus.speed, "км/ч")
    try:
        truck.delivery_cost(100, 12)
    except ValueError as error:
        print("  ValueError:", error)
    print()
    print("Вызовы без создания объекта:")
    print("  Transport.check_positive(60, 'Скорость') ->",
          Transport.check_positive(60, "Скорость"))
    print("  Taxi.from_dict(...) ->",
          Taxi.from_dict({"speed": 100, "capacity": 3,
                          "tariff": 40}))
    print()
    print("Полиморфный обход списка:")
    for vehicle in [bus, truck, taxi]:
        print(" ", vehicle)
        print("    превышает", SPEED_LIMIT, "км/ч:",
              vehicle.is_speeding(SPEED_LIMIT))

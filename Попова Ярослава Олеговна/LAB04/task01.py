#!/usr/bin/env python3

class Transport:
    """
    Базовый класс для транспортных средств.
    """
    DEFAULT_SPEED = 0.0
    DEFAULT_CAPACITY = 0

    def __init__(self, speed: float = DEFAULT_SPEED, capacity: int = DEFAULT_CAPACITY):
        """
        Инициализирует базовый объект транспорта.

        :param speed: Скорость транспорта.
        :param capacity: Вместимость (количество пассажиров или единиц груза).
        """
        self._speed = 0.0
        self._capacity = 0

        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self) -> float:
        """
        Свойство для получения скорости.

        :return: Текущая скорость транспорта.
        """
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Скорость должна быть больше нуля.")
        self._speed = value

    @property
    def capacity(self) -> int:
        """
        Свойство для получения вместимости.

        :return: Текущая вместимость транспорта.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Вместимость должна быть больше нуля.")
        self._capacity = value

    def __str__(self) -> str:
        """
        Формирует строковое представление транспорта.

        :return: Строка с информацией о скорости и вместимости.
        """
        return f"Транспорт (Скорость: {self.speed} км/ч, Вместимость: {self.capacity})"

    def is_speeding(self, limit: float) -> bool:
        """
        Проверяет, превышает ли скорость заданную отметку.

        :param limit: Ограничение скорости для проверки.
        :return: True, если скорость выше лимита, иначе False.
        """
        return self.speed > limit

    @staticmethod
    def check_rules() -> str:
        """
        Статический метод для демонстрации вызова без создания объекта.

        :return: Строка с общим правилом для всего транспорта.
        """
        return "Правило: соблюдайте ПДД!"

    @classmethod
    def from_dict(cls, data: dict) -> "Transport":
        """
        Альтернативный конструктор: создает объект из словаря.

        :param data: Словарь с данными для создания объекта.
        :return: Новый экземпляр класса.
        """
        speed = float(data.get("speed", cls.DEFAULT_SPEED))
        capacity = int(data.get("capacity", cls.DEFAULT_CAPACITY))
        return cls(speed=speed, capacity=capacity)


class Bus(Transport):
    """
    Класс автобуса, наследующий Transport.
    """

    def __init__(self, speed: float, capacity: int, route: str):
        """
        Инициализирует автобус.

        :param speed: Скорость автобуса.
        :param capacity: Вместимость пассажиров.
        :param route: Маршрут автобуса.
        """
        self._route = ""
        super().__init__(speed, capacity)
        self.route = route

    @property
    def route(self) -> str:
        """
        Свойство для получения маршрута.

        :return: Текущий маршрут.
        """
        return self._route

    @route.setter
    def route(self, value: str) -> None:
        if not value:
            raise ValueError("Маршрут не может быть пустым.")
        self._route = value

    def __str__(self) -> str:
        """
        Формирует строковое представление автобуса.

        :return: Строка с информацией об автобусе.
        """
        base_info = super().__str__()
        return f"[Автобус] {base_info}, Маршрут: {self.route}"


class Truck(Transport):
    """
    Класс грузовика, наследующий Transport.
    """
    COST_PER_TON_KM = 10.0

    def __init__(self, speed: float, capacity: int, load_capacity: float):
        """
        Инициализирует грузовик.

        :param speed: Скорость грузовика.
        :param capacity: Вместимость (места в кабине).
        :param load_capacity: Грузоподъемность в тоннах.
        """
        self._load_capacity = 0.0
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self) -> float:
        """
        Свойство для получения грузоподъемности.

        :return: Грузоподъемность в тоннах.
        """
        return self._load_capacity

    @load_capacity.setter
    def load_capacity(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Грузоподъемность должна быть больше нуля.")
        self._load_capacity = value

    def calculate_cost(self, distance: float) -> float:
        """
        Рассчитывает стоимость перевозки груза.

        :param distance: Расстояние в километрах.
        :return: Итоговая стоимость перевозки.
        """
        return distance * self.load_capacity * self.COST_PER_TON_KM

    def __str__(self) -> str:
        """
        Формирует строковое представление грузовика.

        :return: Строка с информацией о грузовике.
        """
        base_info = super().__str__()
        return f"[Грузовик] {base_info}, Грузоподъемность: {self.load_capacity} т."


class Taxi(Transport):
    """
    Класс такси, наследующий Transport.
    """

    def __init__(self, speed: float, capacity: int, tariff: float):
        """
        Инициализирует такси.

        :param speed: Скорость такси.
        :param capacity: Вместимость пассажиров.
        :param tariff: Тариф за один километр.
        """
        self._tariff = 0.0
        super().__init__(speed, capacity)
        self.tariff = tariff

    @property
    def tariff(self) -> float:
        """
        Свойство для получения тарифа.

        :return: Тариф такси.
        """
        return self._tariff

    @tariff.setter
    def tariff(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Тариф должен быть больше нуля.")
        self._tariff = value

    def calculate_trip_cost(self, distance: float) -> float:
        """
        Рассчитывает стоимость поездки на такси.

        :param distance: Расстояние в километрах.
        :return: Итоговая стоимость поездки.
        """
        return distance * self.tariff

    def __str__(self) -> str:
        """
        Формирует строковое представление такси.

        :return: Строка с информацией о такси.
        """
        base_info = super().__str__()
        return f"[Такси] {base_info}, Тариф: {self.tariff} у.е./км"


if __name__ == '__main__':
    print("1. Создание через конструктор и через метод (from_dict)")
    taxi = Taxi(speed=80.0, capacity=4, tariff=25.0)
    print(taxi)

    data_dict = {"speed": 120.0, "capacity": 50}
    train = Transport.from_dict(data_dict)
    print(f"Создано из словаря: {train}\n")

    print("2. Попытка задать недопустимую скорость")
    try:
        bad_bus = Bus(speed=-10.0, capacity=30, route="101A")
    except ValueError as e:
        print(f"Поймана ошибка валидации: {e}\n")

    print("3. Вызов методов без создания объекта")
    print(f"Вызов статического метода: {Transport.check_rules()}\n")

    print("4. Полиморфный вызов методов для списка")
    fleet = [
        Bus(speed=60.0, capacity=40, route="Центр - Вокзал"),
        Truck(speed=90.0, capacity=2, load_capacity=5.5),
        Taxi(speed=70.0, capacity=4, tariff=30.0)
    ]

    for vehicle in fleet:
        print(vehicle)


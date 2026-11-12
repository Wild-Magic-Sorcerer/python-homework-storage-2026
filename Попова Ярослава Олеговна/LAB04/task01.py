#!/usr/bin/env python3

class Transport:
    def __init__(self, speed: float, capacity: int):
        """
        Инициализирует базовый объект транспорта.

        Параметры:
        speed — скорость транспорта.
        capacity — вместимость (количество пассажиров или единиц груза).

        Возвращает:
        None
        """
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self) -> float:
        """
        Свойство для получения скорости.

        Параметры:
        Нет.

        Возвращает:
        Текущую скорость транспорта.
        """
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:
        """
        Сеттер для скорости с валидацией.

        Параметры:
        value — новое значение скорости.

        Возвращает:
        None
        """
        if value <= 0:
            raise ValueError("Скорость должна быть больше нуля.")
        self._speed = value

    @property
    def capacity(self) -> int:
        """
        Свойство для получения вместимости.

        Параметры:
        Нет.

        Возвращает:
        Текущую вместимость транспорта.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """
        Сеттер для вместимости с валидацией.

        Параметры:
        value — новое значение вместимости.

        Возвращает:
        None
        """
        if value <= 0:
            raise ValueError("Вместимость должна быть больше нуля.")
        self._capacity = value

    def get_info(self) -> str:
        """
        Формирует строку с основными характеристиками транспорта.

        Параметры:
        Нет.

        Возвращает:
        Строку с информацией о скорости и вместимости.
        """
        return f"Транспорт (Скорость: {self.speed} км/ч, Вместимость: {self.capacity})"

    def is_speeding(self, limit: float) -> bool:
        """
        Проверяет, превышает ли скорость заданную отметку.

        Параметры:
        limit — ограничение скорости для проверки.

        Возвращает:
        True, если скорость выше лимита, иначе False.
        """
        return self.speed > limit

    @staticmethod
    def check_rules() -> str:
        """
        Статический метод для демонстрации вызова без создания объекта.

        Параметры:
        Нет.

        Возвращает:
        Строку с общим правилом для всего транспорта.
        """
        return "Правило: соблюдайте ПДД!"

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Transport":
        """
        Альтернативный конструктор: создает объект из словаря.

        Параметры:
        data — словарь с данными для создания объекта.

        Возвращает:
        Новый экземпляр класса.
        """
        speed = float(data.get("speed", 0.0))
        capacity = int(data.get("capacity", 0))
        return cls(speed=speed, capacity=capacity)


class Bus(Transport):
    def __init__(self, speed: float, capacity: int, route: str):
        """
        Инициализирует автобус.

        Параметры:
        speed — скорость автобуса.
        capacity — вместимость пассажиров.
        route — маршрут автобуса.

        Возвращает:
        None
        """
        super().__init__(speed, capacity)
        self.route = route

    def get_info(self) -> str:
        """
        Формирует строку с характеристиками автобуса.

        Параметры:
        Нет.

        Возвращает:
        Строку с информацией об автобусе.
        """
        base_info = super().get_info()
        return f"[Автобус] {base_info}, Маршрут: {self.route}"


class Truck(Transport):
    def __init__(self, speed: float, capacity: int, load_capacity: float):
        """
        Инициализирует грузовик.

        Параметры:
        speed — скорость грузовика.
        capacity — вместимость (места в кабине).
        load_capacity — грузоподъемность в тоннах.

        Возвращает:
        None
        """
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    def calculate_cost(self, distance: float) -> float:
        """
        Рассчитывает стоимость перевозки груза.

        Параметры:
        distance — расстояние в километрах.

        Возвращает:
        Итоговую стоимость перевозки.
        """
        # Произвольная формула: 10 у.е. за каждый километр на каждую тонну
        return distance * self.load_capacity * 10.0

    def get_info(self) -> str:
        """
        Формирует строку с характеристиками грузовика.

        Параметры:
        Нет.

        Возвращает:
        Строку с информацией о грузовике.
        """
        base_info = super().get_info()
        return f"[Грузовик] {base_info}, Грузоподъемность: {self.load_capacity} т."


class Taxi(Transport):
    def __init__(self, speed: float, capacity: int, tariff: float):
        """
        Инициализирует такси.

        Параметры:
        speed — скорость такси.
        capacity — вместимость пассажиров.
        tariff — тариф за один километр.

        Возвращает:
        None
        """
        super().__init__(speed, capacity)
        self.tariff = tariff

    def calculate_trip_cost(self, distance: float) -> float:
        """
        Рассчитывает стоимость поездки на такси.

        Параметры:
        distance — расстояние в километрах.

        Возвращает:
        Итоговую стоимость поездки.
        """
        return distance * self.tariff

    def get_info(self) -> str:
        """
        Формирует строку с характеристиками такси.

        Параметры:
        Нет.

        Возвращает:
        Строку с информацией о такси.
        """
        base_info = super().get_info()
        return f"[Такси] {base_info}, Тариф: {self.tariff} у.е./км"


if __name__ == '__main__':
    print("1. Создание через конструктор и через метод (from_dict)")
    taxi = Taxi(speed=80.0, capacity=4, tariff=25.0)
    print(taxi.get_info())

    data_dict = {"speed": 120.0, "capacity": 50}
    train = Transport.from_dict(data_dict)
    print(f"Создано из словаря: {train.get_info()}\n")

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
        print(vehicle.get_info())


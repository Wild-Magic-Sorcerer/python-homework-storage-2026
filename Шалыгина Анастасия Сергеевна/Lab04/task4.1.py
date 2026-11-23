#!/usr/bin/env python3


SPEED_LIMIT = 120
DEFAULT_COST_PER_KG = 50.0

class Transport:
    """
    Базовый класс для всех видов транспорта

    Хранит приватные переменные скорости и ёмкости
    """

    def __init__(self, speed, capacity):
        """
        Инициализирует транспортное средство

        :param speed: Скорость транспорта в км/ч
        :param capacity: Вместимость транспорта
        :return: Ничего не возвращает, инициализирует объект
        """
        self._speed = None
        self._capacity = None
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Возвращает текущую скорость транспорта
        :return: Скорость в км/ч
        """
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость
        :param value: Новое значение скорости
        :return: Ничего не возвращает, изменяет защищенную переменную _speed
        """
        if type(value) is not int:
            raise TypeError(f"Скорость может быть только целой циферкой!! Получено: {type(value).__name__}")
        if value < 0:
            raise ValueError(f"Внимание! Задний ход задается не отрицательным значением: {value}")
        self._speed = value

    @property
    def capacity(self):
        """
        Возвращает текущую ёмкость транспорта
        :return: Вместимость
        """
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает новую ёмкость
        :param value: Новое значение ёмкости
        :return: Ничего не возвращает, изменяет защищенную переменную _capacity
        """
        if type(value) is not int:
            raise TypeError(f"Ёмкость должна быть целым числом! Было получено: {type(value).__name__}")
        if value <= 0:
            raise ValueError(f"Ёмкость должна быть положительной! А было получено: {value}")
        self._capacity = value

    def __str__(self):
        """
        Возвращает строку с основными характеристиками транспорта
        :return:Строка со скоростью и ёмкостью
        """
        return f"Транспорт: скорость = {self.speed} км/ч, ёмкость транспорта = {self.capacity}"

    def check_speed(self, limit = None):
        """
        Проверяет, превышает ли текущая скорость заданный порог
        :param limit: Порог скорости для сравнения, если не указан используется SPEED_LIMIT (120 км/ч)
        :return: True, если скорость превышает порог, иначе False
        """
        doorstep = limit if limit is not None else SPEED_LIMIT
        return self.speed > doorstep

    @classmethod
    def from_dict(cls, data_dict):
        """
        Создает объект транспорта из словаря
        :param data_dict: словарь с ключами 'speed' и 'capacity'
        :return: Новый объект транспорта
        """
        speed = data_dict.get('speed')
        capacity = data_dict.get('capacity')
        if speed is None or capacity is None:
            raise KeyError("Словарь должен содержать хоть какие-то ключи 'speed' и 'capacity'")
        return cls(speed=speed, capacity = capacity)

class Bus(Transport):
    """
    Класс Автобус. Наследует Transport и добавляет маршрут.

    """
    def __init__(self, speed, capacity, route):
        """
        Инициализирует автобус
        :param speed: Скорость автобуса в км/ч
        :param capacity: Вместимость автобуса
        :param route: Маршрут автобуса
        :return: Ничего не возвращает, инициализирует объект
        """
        super().__init__(speed, capacity)
        self._route = None
        self.route = route

    @property
    def route(self):
        """
        Возвращает маршрут автобуса
        :return: Название маршрута
        """
        return self._route

    @route.setter
    def route(self, value):
        """
        Устанавливает маршрут
        :param value: Новый маршрут
        :return: Ничего не возвращает, изменяет защищенную переменную _route
        """
        if type(value) is not str or not value.strip():
            raise ValueError ("Маршрут не может быть пустым...")
        self._route = value.strip()

    def __str__(self):
        """
        Возвращает строку с характеристикой автобуса
        :return: Строка содержащая информацию о скорости, вместимости и маршрута автобуса
        """
        return f"Bus: Скорость:{self.speed} км/ч, ёмкость: {self.capacity}, Маршрут: '{self.route}'"

class Truck(Transport):
    """
    Класс грузовик. Наследует Transport и добавляет грузоподъёмность
    """

    def __init__(self, speed, capacity, max_load):
        """
        Инициализирует грузовик
        :param speed: скорость грузовика в км/ч
        :param capacity: Вместимость грузовика
        :param max_load: Грузоподъёмность грузовика в кг
        :return: Ничего не возвращает, инициализирует объект
        """
        super().__init__(speed, capacity)
        self._max_load = None
        self.max_load = max_load

    @property
    def max_load(self):
        """
        Возвращает грузоподъемность грузовика
        :return: Максимальный вес груза в кг
        """
        return self._max_load

    @max_load.setter
    def max_load(self, value):
        """
        Устанавливает грузоподъёмность
        :param value: Новое значение грузоподъемности
        :return: Ничего не возвращает, изменяет защищенную переменную _max_load
        """
        if type(value) not in(int, float):
            raise TypeError(f"Грузоподъемность должна быть числом, а Вы ввели: {type(value).__name__}")
        if value <= 0:
            raise ValueError ("Вы должны хоть положить что-то, а не красть машину........")
        self._max_load = float(value)

    def calculate_price_transit(self, weight):
        """
        Рассчитывает стоимость перевозки груза
        :param weight: Вес груза в кг
        :return: Стоимость перевозки в рублях
        """
        if weight <= 0:
            raise ValueError ("Напомним, красть машину не хорошо... Положите что-то в нее")
        if weight > self.max_load:
            raise ValueError (f"Машинка не может увезти столько. Ваш вес товара: {weight} кг, а машинка может принять только: {self.max_load}кг")
        return weight * DEFAULT_COST_PER_KG

    def __str__(self):
        """
        Возвращает строку с характеристикой грузовика
        :return: Строка, содержащая информацию о скорости, вместимости и грузоподъемности грузовика
        """
        return f"Truck: speed = {self.speed} км/ч, capacity = {self.capacity}, max_load = {self.max_load} кг"

class Taxi(Transport):

    def __init__(self, speed, capacity, rate_per_km):
        """
        Класс такси. Наследует Transport и добавляет тариф за километр
        :param speed: Скорость в км/ч
        :param capacity: Вместимость такси
        :param rate_per_km: Тариф за километр в рублях
        :return: Ничего не возвращает, инициализирует объект
        """
        super().__init__(speed, capacity)
        self._rate_per_km = None
        self.rate_per_km = rate_per_km

    @property
    def rate_per_km(self):
        """
        Возвращает тариф за километр
        :return: Стоимость одного километра в рублях
        """
        return self._rate_per_km

    @rate_per_km.setter
    def rate_per_km(self, value):
        """
        Устанавливает тариф
        :param value: Новый тариф
        :return: Ничего не возвращает, изменяет защищенную переменную _rate_per_km
        """
        if type(value) not in (int, float):
            raise TypeError (f"Тариф должен быть числом, а было получен: {type(value).__name__}")
        if value < 0:
            raise ValueError ("Тариф не может быть отрицательным!!")
        self._rate_per_km = float(value)

    def calculate_price_tax(self, distance):
        """
        Рассчитывает стоимость поездки
        :param distance: Расстояние в км
        :return: Стоимость поездки в рублях
        """
        if distance < 0:
            raise ValueError ("Расстояние не может быть отрицательным!")
        return distance * self.rate_per_km

    def __str__(self):
        """
        Возвращает строку с характеристиками такси
        :return: Строка, содержащая информацию о скорости, вместимости и тарифом такси
        """
        return f"Taxi: Скорость = {self.speed}км/ч, емкость = {self.capacity}, ставка за км = {self.rate_per_km} руб/км"


if __name__ == '__main__':
    bus = Bus(speed=60, capacity=50, route="Санкт-Петербург - Петрозаводск")
    truck = Truck(speed=80, capacity=2, max_load=100.0)
    taxi = Taxi(speed=90, capacity=4, rate_per_km=35.0)
    print(bus)
    print(truck)
    print(taxi)

    data = {"speed": 60, "capacity": 2}
    transport = Transport.from_dict(data)
    print(f"Создали из словаря: {transport}")

    invalid_cases = [("Отрицательная скорость", lambda: Transport(speed = -10, capacity = 5)),
                      ("Скорость не int", lambda: Transport(speed = 'fast', capacity = 5)),
                     ("Нулевая ёмкость", lambda: Transport(speed = 50, capacity = 0)),
                     ("Ёмкость не int", lambda: Transport(speed = 50, capacity = 'many'))]
    for description, action in invalid_cases:
        try:
            action()
            print(f"{description}: ошибка не возникла")
        except (ValueError, TypeError) as e:
            print(f"{description}: перехвачено → {e}")

    print(f"Максимальная скорость у транспорта: {SPEED_LIMIT}")
    print(f"Стоимость перевозки за кг у грузовика: {DEFAULT_COST_PER_KG}")

    new_transport = Transport.from_dict({"speed":55, "capacity":5})
    print(f"Был создан через словарь без экземпляра: {new_transport}")

    alls = [
        Bus(speed= 60, capacity= 40, route= "Маршрут №1"),
        Truck(speed= 70, capacity= 2, max_load = 2000.0),
        Taxi(speed= 90, capacity= 4, rate_per_km= 40.0),
        Bus(speed= 50, capacity= 50, route= "Маршрут №2")
    ]
    for vehicle in alls:
        print(f"{vehicle}")

    for vehicle in alls:
        excess = vehicle.check_speed()
        print(f"{vehicle.__class__.__name__}(speed = {vehicle.speed})")

    for vehicle in alls:
        if isinstance(vehicle, Truck):
            cost = vehicle.calculate_price_transit(weight=1000.0)
            print(f"  {vehicle.__class__.__name__}: перевозка 1000 кг = {cost} руб.")
        elif isinstance(vehicle, Taxi):
            cost = vehicle.calculate_price_tax(distance=30.0)
            print(f"  {vehicle.__class__.__name__}: стоимость поездки 30 км = {cost} руб.")

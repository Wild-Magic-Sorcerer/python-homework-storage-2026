#!/usr/bin/env python3

MAX_SPEED = 300
MIN_SPEED = 0
MAX_CAPACITY = 200
MIN_CAPACITY = 1

class Transport:
    """
    Класс транспортного средства.
    """
    def __init__(self, speed, capacity):
        """
        Инициализирует транспортное средство.
        
        :param speed: Скорость транспорта (км/ч).
        :param capacity: Вместимость транспорта (количество мест).
        :raises ValueError: Если скорость или вместимость некорректны.
        """
        self._speed = MIN_SPEED
        self._capacity = MIN_CAPACITY
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Возвращает текущую скорость транспорта
        """
        return self._speed


    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость и проверяет её корректность. 

        :param value: Новое значение скорости.
        :raises ValueError: Если значение некорректно.
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            raise ValueError("Значение скорости должно быть целым числом.")
        if not (MIN_SPEED <= value <= MAX_SPEED):
            raise ValueError(f"Скорость должна быть в диапазоне от {MIN_SPEED} до {MAX_SPEED}")
        self._speed = value


    @property
    def capacity(self):
        """
        Возвращает текущую вместимость транспорта
        """
        return self._capacity


    @capacity.setter 
    def capacity(self, value):
        """
        Устанавливает вместимость и проверяет её корректность.

        :param value: Новое значение вместимости
        """
        try:
            value = int(value)
        except (ValueError, TypeError):
            print(f"Ошибка!\n Вместимость жолжна быть целым числом.")
            return
        if value < MIN_CAPACITY or value > MAX_CAPACITY:
            print(f"Ошибка:\n вместимость должна быть в диапазоне от {MIN_CAPACITY} до {MAX_CAPACITY}")
            return
        self._capacity = value


    def __str__(self):
        """
        Возвращает строку с характеристиками транспорта
        """ 
        return f"Скорость: {self._speed} км/ч \n Вместимость: {self._capacity}"


    def is_speed_exceeded(self, limit):
        """
        Проверка предела разрешенной скорости. 

        :param limit: Пороговое значение скорости
        :return: True, если скорость выше порога, иначе - False
        """ 
        return self._speed > limit


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект Transort из словаря. Необходимо для уникальных параметров для этого дочернего класса.

        :param data: Словарь с ключами "speed", "capacity"
        :return: Новый объект Transport
        """
        return cls(speed = data["speed"], capacity = data["capacity"])


class Bus(Transport):
    """
    Автобус - наследник Transport.
    Добавляет маршрут.
    """
    def __init__(self, speed, capacity, route):
        """
        Инициализирует автобус.

        :param speed: Скорость (км/ч).
        :param capacity: Вместимость (количество мест).
        :param route: Маршрут автобуса.
        """
        super().__init__(speed, capacity)
        self.__route = route
        self.route = route
    

    @property
    def route(self):
        """
        Возвращает маршрут автобуса
        """
        return self.__route


    @route.setter
    def route(self, value):
        """
        Устанавливает маршрут.

        :param value: Маршрут автобуса.
        :raises ValueError: Если маршрут некорректен.
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Маршрут должен быть непустой строкой.")
        self.__route = value.strip()


    @classmethod
    def from_dict(cls, data):
        """
        Создает объект Bus из словаря

        :param data: Словарь с ключами "speed", "capacity", "route"
        :return: Новый объект Bus
        """
        return cls(
            speed=data["speed"],
            capacity=data["capacity"],
            route=data["route"]
        )
    

    def __str__(self):
        """
        Возвращает строку с характеристиками автобуса
        """
        return f"{super().__str__()},\n Маршрут: {self.__route}"


class Truck(Transport):
    """
    Грузовик - наследник Transort.
    Добавляет грузоподъемность.
    """

    def __init__(self, speed, capacity, load_capacity):
        """
        Инициализирует грузовик.

        :param speed: Скорость (км/ч).
        :param capacity: Вместимость (количество мест).
        :param load_capacity: Грузоподъёмность (т).
        :raises ValueError: Если параметры некорректны.
        """
        super().__init__(speed, capacity)
        self.__load_capacity = None
        self.load_capacity = load_capacity


    @property
    def load_capacity(self):
        """Возвращает грузоподъёмность."""
        return self.__load_capacity


    @load_capacity.setter
    def load_capacity(self, value):
        """
        Устанавливает грузоподъёмность.

        :param value: Грузоподъёмность в тоннах.
        :raises ValueError: Если значение некорректно.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Грузоподъёмность должна быть числом.")
        if value <= 0:
            raise ValueError("Грузоподъёмность должна быть положительным числом.")
        self.__load_capacity = value

    def calculate_delivery_cost(self, distance, price_for_km):
        """
        Рассчитывает стоимость перевозки.

        :param distance: Расстояние в км.
        :param price_for_km: Цена за км.
        :return: Стоимость перевозки.
        """
        return distance * price_for_km

    def __str__(self):
        """Возвращает строку с характеристиками грузовика."""
        return f"{super().__str__()},\n Грузоподъёмность: {self.__load_capacity} тонн"


class Taxi(Transport):
    """
    Такси - наследник Transort.
    Добавляет тариф и расчет стоимости поездки.
    """
    def __init__(self, speed, capacity, rate):
        """
        Инициализирует такси.

        :param speed: Скорость (км/ч).
        :param capacity: Вместимость (количество мест).
        :param rate: Тариф за километр.
        :raises ValueError: Если параметры некорректны.
        """
        super().__init__(speed, capacity)
        self.__rate = None
        self.rate = rate 


    @property
    def rate(self):
        """Возвращает тариф."""
        return self.__rate


    @rate.setter
    def rate(self, value):
        """
        Устанавливает тариф.

        :param value: Тариф за километр.
        :raises ValueError: Если значение некорректно.
        """
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValueError("Тариф должен быть числом.")
        if value <= 0:
            raise ValueError("Тариф должен быть положительным числом.")
        self.__rate = value

    def calculate_trip_cost(self, distance):
        """
        Рассчитывает стоимость поездки.

        :param distance: Расстояние в км
        :return: Стоимость поездки
        """
        return distance * self.rate


    def __str__(self):
        """
        Возвращает строку с характеристиками такси.
        """
        return f"{super().__str__()},\n Тариф: {self.__rate} рублей/км"


if __name__ == '__main__':
    print("Создание через конструктор:")
    bus = Bus(speed=65, capacity=52, route="Санкт-Петербург - Великий Новгород")
    truck = Truck(speed=45, capacity=1, load_capacity=11.50)
    taxi = Taxi(speed=75, capacity=4, rate = 20.15)

    print(bus)
    print(truck)
    print(taxi)


    print("Создание через классовый метод")
    data_bus = {"speed": 68, "capacity": 45, "route": "Санкт-Петербург - Великий Новгород"}
    bus_from_dict = Bus.from_dict(data_bus)
    print(f"Автобус из словаря: {bus_from_dict}")

    data_transport = {"speed": 100, "capacity": 4}
    transport_from_dict = Transport.from_dict(data_transport)
    print(f"Транспорт из словаря: {transport_from_dict}")


    print("\n Проверка валидации:")
    try:
        bad_transport_1 = Transport(speed=30, capacity=0)
    except ValueError as e:
        print(f"Ошибка вместимости: {e}")

    try:
        bad_transport_2 = Transport(speed=1000, capacity=25)
    except ValueError as e:
        print(f"Ошибка скорости: {e}")

    print("\n Полиморфизм:")
    many_transport = (bus, truck, taxi)
    for t in many_transport:
        print("--", t)

    print("\n Проверка превышения скорости (порог 60 км/ч):")
    for t in many_transport:
        exceeded = t.is_speed_exceeded(60)
        print(f" - {t.__class__.__name__}: {'превысил' if exceeded else 'не превысил'}")

    print("\n Расчет стоимости поездки на 150 км:")
    print(f" - Грузовик: {truck.calculate_delivery_cost(150, 18.04)} руб")
    print(f" - Такси: {taxi.calculate_trip_cost(150)} руб")

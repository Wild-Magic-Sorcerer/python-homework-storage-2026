HIGH_SPEED = 90
LOW_SPEED = 50
PRICE_INDEX = 2
PRICE_MINIMUM = 500

class Transport:
    """
    Класс для описания любого транспорта и его характеристик.
    """
    def __init__(self, speed, capacity):
        """
        Метод-конструктор класса Transport.
        :param speed: Скорость транспорта.
        :param capacity: Ёмкость траноспорта.
        :return: None
        """
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        """
        Метод, возвращающий скорость транспорта.
        :return: Скорость транспорта.
        """
        return self._speed

    @property
    def capacity(self):
        """
        Метод, возвращающий ёмкость транспорта.
        :return: Ёмкость транспорта.
        """
        return self._capacity

    @speed.setter
    def speed(self, value):
        """
        Метод, позволяющий установить новую скорость транспорта (с валидацией).
        :param value: Новая скорость транспорта.
        :return: None
        :raises: ValueError: Если скорость отрицательная.
        """
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        self._speed = value

    @capacity.setter
    def capacity(self, value):
        """
        Метод, позволяющий установить новую ёмкость транспорта (с валидацией).
        :param value: Новая ёмкость транспорта.
        :return: None
        :raises: ValueError: Если ёмкость отрицательная.
        """
        if value < 0:
            raise ValueError("Ёмкость не может быть отрицательной!")
        self._capacity = value

    def __str__(self):
        """
        Метод, возвращающий строку с кратким описанием основных характеристик класса.
        :return: Строка с характеристиками класса.
        """
        return f"Это транспорт с ёмкостью {self._capacity} человек и скоростью {self._speed} км/ч."

    def high_speed(self, high_speed):
        """
        Метод, вовзращающий True, если скорость транспорта выше заданного значения,
        и False, если нет.
        :param high_speed: Критическое значение скорости, с которым сравнивается текущая скорость.
        :return: True или False
        """
        return self._speed > high_speed

    @classmethod
    def reform_dict(cls, some_dict):
        """
        Классовый метод, создающий объект из словаря.
        :param some_dict: Словарь, описывающий объект, который должен быть создан.
        :return: Новый объект класса Transport.
        """
        speed = some_dict.get("speed", 0)
        capacity = some_dict.get("capacity", 0)
        return cls(speed, capacity)

    @staticmethod
    def tell_the_speed(self):
        """
        Статический метод, сравнивающий скорость транспорта с эталонными вариантами.
        :param self: Ссылка на объект класса Transport и его характеристики.
        :return: Строка с описанием текущей скорости.
        """
        if self > HIGH_SPEED:
            return "Хорошо бы сбавить скорость."
        elif self < LOW_SPEED:
            return "Хорошо бы ускориться!"
        else:
            return "Всё хорошо!"

class Bus(Transport):
    """
    Класс для автобуса. Наследует характеристики класса Transport.
    """
    def __init__(self, speed, capacity, route = ""):
        """
        Метод-конструктор класса Bus.
        :param speed: Скорость автобуса.
        :param capacity: Ёмкость автобуса.
        :param route: Маршрут автобуса.
        :return: None
        """
        super().__init__(speed, capacity)
        self._route = route

    @property
    def route(self):
        """
        Метод, возвращающий маршрут автобуса.
        :return: Маршрут автобуса.
        """
        return self._route

    @route.setter
    def route(self, value):
        """
        Метод, позволяющий установить новый маршрут автобуса.
        :param value: Новый маршрут автобуса.
        :return: None
        """
        self._route = value

class Truck(Transport):
    """
    Класс для грузовика. Наследует характеристики класса Transport.
    """
    def __init__(self, speed, capacity, payload):
        """
        Метод-конструктор класса Truck.
        :param speed: Скорость грузовика.
        :param capacity: Ёмкость грузовика.
        :param payload: Грузоподъёмность грузовика.
        :return: None
        """
        super().__init__(speed, capacity)
        self._payload = payload

    @property
    def payload(self):
        """
        Метод, возвращающий грузоподъёмность грузовика.
        :return: Грузоподъёмность грузовика.
        """
        return self._payload

    def transport_cost(self, distance, load):
        """
        Метод, позволяющий рассчитать стоимость перевозки.
        :param distance: Расстояние, на которое нужно перевести груз.
        :param load: Вес перевозимого груза.
        :return: Итоговая стоимость перевозки.
        :raises ValueError: Если груз больше, чем грузоподъёмность.
        """
        if load <= self._payload:
            return distance * self._speed * PRICE_INDEX
        else:
            raise ValueError("На этом транспорте нельзя везти такой тяжёлый груз!")

class Taxi(Transport):
    """
    Класс для такси. Наследует характеристики класса Transport.
    """
    def __init__(self, speed, capacity, price):
        """
        Метод-конструктор класса Taxi.
        :param speed: Скорость такси.
        :param capacity: Ёмкость такси.
        :param price: Тариф, по которому рассчитывается стоимость поездки.
        :return: None
        """
        super().__init__(speed, capacity)
        self._price = price

    @property
    def price(self):
        """
        Тариф, по которому рассчитывается стоимость поездки.
        :return: Текущий тариф.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Метод, позволяющий поменять тариф.
        :param value: Новое значение тарифа.
        :return: None
        :raises: ValueError: Если новое значение тарифа меньше или равно 0.
        """
        if value > 0:
            self._price = value
        else:
            raise ValueError("Значение тарифа должно быть положительным!")

    def final_cost(self):
        """
        Расчёт стоимости поездки.
        :return: Стоимость поездки.
        """
        final_cost = self._price * self._speed + PRICE_MINIMUM
        return final_cost

if __name__ == '__main__':
    car_1 = Transport(100, 8)
    print(f"Скорость машины {car_1.speed} км/ч.")
    print(f"Скорость высокая? {car_1.high_speed(80)}.")
    super_car = Transport.reform_dict({"speed": 130, "capacity": 5})
    print(super_car)
    print("Вызов метода без создания объекта:", Transport.tell_the_speed(45))
    bus_1 = Bus(70, 50)
    truck_1 = Truck(80, 10, 900)
    taxi_1 = Taxi(95, 5, 50)
    for transport in (bus_1, truck_1, taxi_1):
        print(transport.speed)
    try:
        car_1.capacity = -2
    except ValueError:
        print("Нормальную скорость и вместимость введите!")

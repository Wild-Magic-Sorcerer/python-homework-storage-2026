#!/usr/bin/env python3


DEFAULT_SPEED = 0.0
DEFAULT_CAPACITY = 1


class Transport:
    """
    Родительский класс, в котором находятся основные характеристики транспорта.
    """
    def __init__(self, speed, capacity):
        """
        Базовый конструктор класса Transport.

        :param speed: Скорость транспорта.

        :param capacity: Емкость транспорта.
        """
        self._speed = DEFAULT_SPEED
        self._capacity = DEFAULT_CAPACITY
        self.speed = speed
        self.capacity = capacity


    @staticmethod
    def check_int(value):
        """
        Метод для проверки целого числа.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) == int


    @staticmethod
    def check_float(value):
        """
        Метод для проверки вещественного числа.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        return type(value) == float


    @staticmethod
    def check_string(value):
        """
        Метод для проверки строкового значения.

        :param value: Значение для проверки.

        :return: True, если все тип-топ.
        """
        if type(value) != str:
            return False

        if value.strip():
            return True

        return False

    @property
    def speed(self):
        """
        Метод, который позволяет прочитать значение скорости транспорта.

        :return: Скорость транспорта.
        """
        return self._speed


    @speed.setter
    def speed(self, value):
        """
        Метод, который изменяет значение скорости после его проверки.

        :param value: Новое значение скорости.

        :raises ValueError: Если значение имеет неверный тип
        или меньше 0.
        """
        if self.check_float(value) and value >= 0:
            self._speed = value
        else:
            raise ValueError('Скорость не может быть отрицательным или нецелым числом..')


    @property
    def capacity(self):
        """
        Метод, который позволяет прочитать значение емкости транспорта.

        :return: Емкость транспорта.
        """
        return self._capacity


    @capacity.setter
    def capacity(self, value):
        """
        Метод, который изменяет значение емкости после его проверки.

        :param value: Новое значение емкости.

        :raises ValueError: Если значение имеет неверный тип
        или меньше либо равна 0.
        """
        if self.check_int(value) and value > 0:
            self._capacity = value
        else:
            raise ValueError('Емкость не может быть 0 или отрицательной')


    def __str__(self):
        """
        Метод, который возвращает основные характеристики транспорта.

        :return: Строка с основными характеристиками транспорта.
        """
        return f'Скорость: {self._speed}, 'f'емкость: {self._capacity}'


    def speedy(self, value):
        """
        Метод для проверки превышения скорости.

        :param value: Произвольная отметка для сравнения.

        :return: True, если скорость превысила произвольную отметку.
        """
        return self._speed > value


    @classmethod
    def from_dict(cls, dictionary):
        """
        Метод, который создает объект класса из словаря.

        :param dictionary: Словарь с характеристиками транспорта.

        :return: Новый объект класса.
        """
        speed = dictionary.get('speed')
        capacity = dictionary.get('capacity')

        if not cls.check_float(speed) or speed < 0:
            raise ValueError('Некорректное значение скорости')

        if not cls.check_int(capacity) or capacity <= 0:
            raise ValueError('Некорректное значение емкости')

        return cls(**dictionary)


class Bus(Transport):
    """
    Дочерний класс с характеристиками автобуса, который наследует класс Transport.
    """
    def __init__(self, speed, capacity, way):
        """
        Базовый конструктор класса Bus.

        :param speed: Скорость автобуса.

        :param capacity: Емкость автобуса.

        :param way: Маршрут автобуса.
        """
        super().__init__(speed=speed, capacity=capacity)
        if self.check_string(way):
            self._way = way
        else:
            raise ValueError('Маршрут должен быть в виде непустой строки..')


    @property
    def way(self):
        """
        Метод, который позволяет прочитать маршрут автобуса.

        :return: Маршрут автобуса.
        """
        return self._way


    def __str__(self):
        """
        Метод, который возвращает основные характеристики автобуса.

        :return: Строка с основными характеристиками автобуса.
        """
        return f'Я автобус и вот мои характеристики: {super().__str__()}, 'f'а еще и маршрут: {self._way}'


class Truck(Transport):
    """
    Дочерний класс с характеристиками грузовика, который наследует класс Transport.
    """
    def __init__(self, speed, capacity, carrying):
        """
        Базовый конструктор класса Truck.

        :param speed: Скорость грузовика.

        :param capacity: Емкость грузовика.

        :param carrying: Грузоподъемность грузовика.
        """
        super().__init__(speed=speed, capacity=capacity)
        if self.check_float(carrying) and carrying > 0:
            self._carrying = carrying
        else:
            raise ValueError('Грузоподъемность должна быть больше 0..')


    @property
    def carrying(self):
        """
        Метод, с помощью которого получаем грузоподъемность грузовика.

        :return: Грузоподъемность грузовика.
        """
        return self._carrying


    def how_much(self, distance):
        """
        Метод, который рассчитывает стоимость перевозки.

        :param distance: Расстояние перевозки.

        :return: Стоимость перевозки.
        """
        return self._carrying * distance


    def __str__(self):
        """
        Метод, который возвращает основные характеристики грузовика.

        :return: Строка с характеристиками грузовика.
        """
        return f'А теперь я грузовик: {super().__str__()}, 'f'и вот моя грузоподъемность: {self._carrying}'


class Taxi(Transport):
    """
    Дочерний класс с характеристиками такси, который наследует класс Transport.
    """
    def __init__(self, speed, capacity, tariff):
        """
        Базовый конструктор класса Taxi.

        :param speed: Скорость такси.

        :param capacity: Емкость такси.

        :param tariff: Тариф.
        """
        super().__init__(speed=speed,capacity=capacity)
        if self.check_float(tariff) and tariff > 0:
            self._tariff = tariff
        else:
            raise ValueError('Тариф должен быть больше 0..')


    @property
    def tariff(self):
        """
        Метод, с помощью которого получаем тариф такси.

        :return: Тариф такси.
        """
        return self._tariff


    def how_much(self, distance):
        """
        Метод, который рассчитывает стоимость поездки.

        :param distance: Расстояние поездки.

        :return: Стоимость поездки.
        """
        return self._tariff * distance


    def __str__(self):
        """
        Метод, который возвращает основные характеристики такси.

        :return: Строка с характеристиками такси.
        """
        return f'А вот я и такси: {super().__str__()}, 'f'со своим тарифом: {self._tariff}'


if __name__ == '__main__':
    bus_1 = Bus(speed=80.0, capacity=40, way='Уфа-Казань')  #создание объекта через конструктор
    result_1 = bus_1.speedy(90.0)
    print(result_1)

    transport_1 = Transport.from_dict({'speed': 60.0, 'capacity': 3})  #через классовый метод
    print(transport_1)

    try:
        transport_2 = Transport(speed=-10.0, capacity=5)  #попытка задать недопустимую скорость
    except ValueError as error:
        print(error)

    result_2 = Transport.check_float(10.0)  #вызов метода без создания объекта
    print(result_2)

    transports = (bus_1, Truck(speed=70.0, capacity=2, carrying=10.0),
                                   Taxi(speed=90.0, capacity=4, tariff=3.5))  #полиморфный вызов

    for transport in transports:
        print(transport)
        

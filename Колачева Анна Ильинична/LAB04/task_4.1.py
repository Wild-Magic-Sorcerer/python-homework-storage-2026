#!/usr/bin/env python3


class Transport:
    """
    Основной класс транспортных объектов
    """
    def __init__(self, speed, capacity):
        """
        Конструктор класса

        :param speed: int
        :param capacity: int 
        """
        self.speed = speed             #приватные атрибуты, извне к ним не получится обратиться ( исползуются сеттеры так что проверка сразу бует происходить)
        self.capacity = capacity

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        if value < 0:
           raise ValueError('В нашей вселенной отрицательной скорости е бывает!')
        self.__speed = value
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError('С призраками что ли едешь?')
        self.__capacity = value

    def info(self):
        """
        Возвращает строку с основными характеристиками
        """
        return f'Скорость: {self.speed} км/ч, вместимость: {self.capacity}'

    def high_speed(self, value):
        """
        метод возвращает True если есть превышение скорости
        :param value: значение скорости передаваемое методу 
        :return: bool 
        """
        return self.speed > value

    @classmethod
    def from_dict(cls, data):
        """
        Классовый метод создающий новый объект этого класса из словаря

        :param data: словарь с данными для нового объекта
        :return: cls object
        """
        obj_bus = cls(data['speed'], data['capacity'])
        return obj_bus


class Bus(Transport):
    """
    Класс автобуса наследуемый от Transport
    """
    def __init__(self, speed, capacity, marshr = None):
        """
        Базовый конструктор
        """
        super().__init__(speed, capacity)
        self._marshr = marshr
    
    def make_marshrut(self, *items):
        """
        Метод позволяющий создавать маршрут автобуса из списка
        """   
        if items:
            self._marshr = list(items)
        else:
            self._marshr = []

    @property
    def marshrut(self):
        return self._marshr
    @marshrut.setter
    def marshrut(self, value):
        """
        Устанавка нового маршрута
        """
        if isinstance(value, list):
            self._marshr = value
        else:
            raise TypeError("Маршрут должен быть списком")

    def transport_type(self):
        return "Автобус"    

class Truck(Transport):
    """
    Класс грузовика наследуемый от Transport
    """
    
    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self._load_capacity = load_capacity

    def calculate_cost(self, distance):
        """
        Расчет стоимости перевозки: расстояние * грузоподъемность * тариф
        """
        return distance * self._load_capacity * 17

    def transport_type(self):
        return "Грузовик"

class Taxi(Transport):
    """
    Класс такси наследуемый от Transport
    """
    
    def __init__(self, speed, capacity, tarif):
        super().__init__(speed, capacity)
        self._tarif = tarif

    @property
    def tarif(self):
        return self._tarif

    @tarif.setter
    def tarif(self, value):
        if value < 0:
            raise ValueError('Тариф не может быть отрицательным!')
        self._tarif = value


    def trip_cost(self, distance):
        """
        Расчет стоимости поездки: расстояние * тариф
        """
        if distance < 0:
            raise ValueError('Расстояние не может быть отрицательным!')
        return distance * self.tarif
    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект такси из словаря.

        :param data: Словарь с характеристиками такси
        :return: Новый объект такси
        """
        return cls(data['speed'], data['capacity'], data['tarif'])

    def transport_type(self):
        return "Такси"
    
if __name__ == "__main__":

    # 1. Создание через конструктор
    bus = Bus(60, 50, ["Центр", "Вокзал", "Порт"])
    truck = Truck(80, 2, 5)
    taxi = Taxi(90, 4, 25)

    # 2. Создание через классовый метод (из словаря)
    data = {"speed": 100, "capacity": 1, "tarif": 25}
    new_taxi = Taxi.from_dict(data)
    print(new_taxi.info()) 

    # 3. Попытка задать недопустимую скорость (ошибка!)
    try:
        bad_bus = Bus(-10, 50)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # 4. Вызов метода без создания объекта (классовый метод)
    obj = Transport.from_dict({"speed": 50, "capacity": 10})

    # 5. Полиморфный вызов 
    vehicles = [bus, truck, taxi]
    for v in vehicles:
        print(f'\nТип транспорта: {v.transport_type()}')
        print(v.info())

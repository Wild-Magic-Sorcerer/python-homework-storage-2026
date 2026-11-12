MAX_SPEED = 350.0
MAX_CAPACITY = 200


class Transport:
    """
    Базовый класс транспортного средства

    :param speed: скорость транспорта
    :param capacity: вместимость транспорта
    """

    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        """
        Возвращает текущую скорость транспорта
        """
        return self.__speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость с проверкой диапазона от 1 до MAX_SPEED

        :param value: новое значение скорости
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Скорость должна быть числом')
        if not (0 < value <= MAX_SPEED):
            raise ValueError(
                f'Скорость должна быть в диапазоне от 1 до {MAX_SPEED} км/ч'
            )
        self.__speed = float(value)

    @property
    def capacity(self):
        """
        Возвращает текущую вместимость транспорта
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает вместимость с проверкой диапазона от 1 до MAX_CAPACITY

        :param value: новое значение вместимости
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError('Вместимость должна быть целым числом')
        if not (0 < value <= MAX_CAPACITY):
            raise ValueError(f'Вместимость должна быть от 1 до {MAX_CAPACITY}')
        self.__capacity = value

    def get_info(self):
        """
        Возвращает строку с основными характеристиками транспорта

        :return: строка с описанием
        """
        return (
            f'{self.__class__.__name__}: \nСкорость: {self.speed} км/ч \nВместимость: {self.capacity} чел.')

    def over_speedlimit(self, limit):
        """
        Проверяет, превышает ли скорость заданную отметку

        :param limit: порог скорости
        :return: True, если скорость выше лимита
        """
        return self.speed > limit

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект из словаря

        :param d: словарь с ключами speed и capacity
        :return: новый объект Transport
        """
        return cls(d['speed'], d['capacity'])


class Bus(Transport):
    """
    Автобус — наследник Transport с поддержкой маршрута

    :param speed: скорость
    :param capacity: вместимость
    :param route: маршрут автобуса
     """

    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
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
        Устанавливает маршрут автобуса с проверкой на пустую строку

        :param value: название маршрута
        """
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Маршрут е должен быть пустой строкой')
        self.__route = value.strip()

    def get_info(self):
        """
        Возвращает строку с характеристиками автобуса

        :return: строка с описанием и маршрутом
        """
        base_info = super().get_info()
        return f'{base_info} \nМаршрут: {self.route}'

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект Bus из словаря

        :param d: словарь с ключами speed, capacity, route
        :return: новый объект Bus
        """
        return cls(d['speed'], d['capacity'], d['route'])


class Truck(Transport):
    """
    Еще один наследник Transport с расчётом стоимости перевозки

    :param speed: скорость
    :param capacity: вместимость
    :param load_capacity: грузоподъёмность
    """
    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self):
        """
        Возвращает грузоподъёмность грузовика
        """
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        """
        Устанавливает грузоподъёмность с проверкой корректности ввода

        :param value: новое значение грузоподъёмности
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Грузоподъемность должна быть числом')
        if value <= 0:
            raise ValueError('Грузоподъемность должна быть больше нуля')
        self.__load_capacity = float(value)

    def delivery_cost(self, distance):
        """
        Рассчитывает стоимость перевозки груза

        :param distance: расстояние перевозки (км)
        :return: стоимость перевозки
        """
        if distance <= 0:
            raise ValueError('Расстояние должно быть больше нуля')
        return self.load_capacity * distance

    def get_info(self):
        """
        Возвращает строку с характеристиками грузовика

        :return: строка с описанием и грузоподъёмностью
        """
        base_info = super().get_info()
        return f'{base_info}, грузоподъемность: {self.load_capacity}т'

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект Truck из словаря

        :param d: словарь с ключами speed, capacity, load_capacity
        :return: новый объект Truck
        """
        return cls(d['speed'], d['capacity'], d['load_capacity'])


class Taxi(Transport):
    """
        Новый наследник Transport с расчётом стоимости поездки по тарифу

        :param speed: скорость
        :param capacity: вместимость
        :param tariff: тариф за километр пути
        """
    def __init__(self, speed, capacity, tariff):
        super().__init__(speed, capacity)
        self.tariff = tariff

    @property
    def tariff(self):
        """
        Возвращает текущий тариф такси
         """
        return self.__tariff

    @tariff.setter
    def tariff(self, value):
        """
        Устанавливает тариф с проверкой на положительное число

        :param value: новое значение тарифа
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Тариф должен быть числом')
        if value <= 0:
            raise ValueError('Тариф должен быть больше нуля')
        self.__tariff = float(value)

    def trip_cost(self, distance):
        """
        Рассчитывает стоимость поездки на заданное расстояние

        :param distance: расстояние поездки
        :return: стоимость поездки
         """
        if distance <= 0:
            raise ValueError('Расстояние должно быть больше нуля')
        return self.tariff * distance

    def get_info(self):
        """
        Возвращает строку с характеристиками такси

        :return: строка с описанием и тарифом
        """
        base_info = super().get_info()
        return f'{base_info}, тариф: {self.tariff} руб/км'

    @classmethod
    def from_dict(cls, d):
        """
        Создаёт объект Taxi из словаря

        :param d: словарь с ключами speed, capacity, tariff
        :return: новый объект Taxi
        """
        return cls(d['speed'], d['capacity'], d['tariff'])


if __name__ == '__main__':
    print('Создание объектов')
    bus = Bus(65, 40, 'Москва - Лондон')
    truck = Truck(80, 2, 12.5)
    print(bus.get_info())
    print(truck.get_info())
    print(f'Стоимость перевозки: {truck.delivery_cost(100)} руб.\n')

    print('Создание объектов через классовый метод')
    taxi_data = {'speed': 95, 'capacity': 4, 'tariff': 25.0}
    taxi = Taxi.from_dict(taxi_data)
    generic_transport = Transport.from_dict({'speed': 50, 'capacity': 5})
    print(taxi.get_info())
    print(generic_transport.get_info())
    print(f'Стоимость поездки (12 км): {taxi.trip_cost(1200)} руб.\n')

    print('Попытка задать недопустимую скорость')
    try:
        transport_2 = Transport(speed=-10.0, capacity=5)
    except ValueError as error:
        print(error)

    print('Полиморфный вызов метода')
    fleet = [bus, truck, taxi, generic_transport]
    speed_limit = 70

    for vehicle in fleet:
        over_limit = 'Да' if vehicle.over_speedlimit(speed_limit) else 'Нет'
        print(f"{vehicle.get_info()} | Превышение {speed_limit} км/ч {over_limit}")


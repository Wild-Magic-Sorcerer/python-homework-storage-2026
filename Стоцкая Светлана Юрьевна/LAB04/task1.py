class Transport:
    '''
    Класс для описания любого транспорта и его характеристик.
    '''
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    @property
    def speed(self):
        '''
        Метод, возвращающий скорость транспорта.
        :return: self._speed
        '''
        return self._speed

    @property
    def capacity(self):
        '''
        Метод, возвращающий ёмкость транспорта.
        :return: self._capacity
        '''
        return self._capacity

    @speed.setter
    def speed(self, value):
        '''
        Метод, позволяющий установить новую скорость транспорта (с валидацией).
        :param value: Новая скорость транспорта.
        :return: None
        :raises: ValueError: Если скорость отрицательная.
        '''
        if value < 0:
            raise ValueError("Скорость не может быть отрицательной!")
        self._speed = value

    @capacity.setter
    def capacity(self, value):
        '''
        Метод, позволяющий установить новую ёмкость транспорта (с валидацией).
        :param value: Новая ёмкость транспорта.
        :return: None
        :raises: ValueError: Если ёмкость отрицательная.
        '''
        if value < 0:
            raise ValueError("Ёмкость не может быть отрицательной!")
        self._capacity = value

    def main_features(self):
        '''
        Метод, возвращающий строку с кратким описанием основных характеристик класса.
        :return: Строка с характеристиками класса.
        '''
        return f"Это транспорт с ёмкостью {self._capacity} человек и скоростью {self._speed} км/ч."

    def high_speed(self, high_speed):
        '''
        Метод, вовзращающий True, если скорость транспорта выше заданного значения,
        и False, если нет.
        :param high_speed: Критическое значение скорости, с которым сравнивается текущая скорость.
        :return: True или False
        '''
        if self._speed > high_speed:
            return True
        return False

    @classmethod
    def reform_dict(cls, some_dict):
        '''
        Классовый метод, создающий объект из словаря.
        :param some_dict: Словарь, описывающий объект, который должен быть создан.
        :return: Новый объект класса Transport.
        '''
        speed = some_dict.get("speed", 0)
        capacity = some_dict.get("capacity", 0)
        return cls(speed, capacity)

    @staticmethod
    def tell_the_speed(self):
        if self > 90:
            return "Хорошо бы сбавить скорость."
        elif self < 50:
            return "Хорошо бы ускориться!"
        else:
            return "Всё хорошо!"

class Bus(Transport):
    '''
    Класс для автобуса. Наследует характеристики класса Transport.
    '''
    def __init__(self, speed, capacity, route = ""):
        super().__init__(speed, capacity)
        self._route = route

    @property
    def route(self):
        '''
        Метод, возвращающий маршрут автобуса.
        :return: self._route
        '''
        return self._route

    @route.setter
    def route(self, value):
        '''
        Метод, позволяющий установить новый маршрут автобуса.
        :param value: Новый маршрут автобуса.
        :return: None
        '''
        self._route = value

class Truck(Transport):
    '''
    Класс для грузовика. Наследует характеристики класса Transport.
    '''
    def __init__(self, speed, capacity, payload):
        super().__init__(speed, capacity)
        self._payload = payload

    @property
    def payload(self):
        '''
        Метод, возвращающий грузоподъёмность грузовика.
        :return: self._payload
        '''
        return self._payload

    def transport_cost(self, distance, load):
        '''
        Метод, позволяющий рассчитать стоимость перевозки.
        :param distance: Расстояние, на которое нужно перевести груз.
        :param load: Вес перевозимого груза.
        :return: distance * self._speed * 2
        :raises ValueError: Если груз больше, чем грузоподъёмность.
        '''
        if load <= self._payload:
            return distance * self._speed * 2
        else:
            raise ValueError("На этом транспорте нельзя везти такой тяжёлый груз!")


class Taxi(Transport):
    '''
    Класс для такси. Наследует характеристики класса Transport.
    '''
    def __init__(self, speed, capacity, price):
        super().__init__(speed, capacity)
        self._price = price

    @property
    def price(self):
        '''
        Тариф, по которому рассчитывается стоимость поездки.
        :return: self._price
        '''
        return self._price

    @price.setter
    def price(self, value):
        '''
        Метод, позволяющий поменять тариф.
        :param value: Новое значение тарифа.
        :return: None
        :raises: ValueError: Если новое значение тарифа меньше или равно 0.
        '''
        if value > 0:
            self._price = value
        else:
            raise ValueError("Значение тарифа должно быть положительным!")

    def final_cost(self):
        '''
        Расчёт стоимости поездки.
        :return: final_cost
        '''
        final_cost = self._price * self._speed + 500
        return final_cost

if __name__ == '__main__':
    car_1 = Transport(100, 8)
    print(f"Скорость машины {car_1.speed} км/ч.")
    print(f"Скорость высокая? {car_1.high_speed(80)}.")
    super_car = Transport.reform_dict({"speed": 130, "capacity": 5})
    print(super_car.main_features())
    print("Вызов метода без создания объекта:", Transport.tell_the_speed(45))
    bus_1 = Bus(70, 50)
    truck_1 = Truck(80, 10, 900)
    taxi_1 = Taxi(95, 5, 50)
    for transport in [bus_1, truck_1, taxi_1]:
        print(transport.speed)
    try:
        car_1.capacity = -2
    except ValueError:
        print("Нормальную скорость и вместимость введите!")

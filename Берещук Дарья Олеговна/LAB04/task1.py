class Transport:
    """
    Базовый класс транспортного средства.
    Хранит скорость и ёмкость, проверяет их корректность при создании
    """
    def __init__(self, speed, capacity):
        """
        Создаёт транспорт с заданными скоростью и ёмкостью.

        :param speed: скорость транспорта
        :param capacity: ёмкость транспорта

        """
        if speed <= 0:
            raise ValueError("Скорость должна быть > 0")
        if capacity <= 0:
            raise ValueError("Ёмкость должна быть > 0")
        self.__speed = speed
        self.__capacity = capacity

    @property
    def speed(self):
        return self.__speed

    @property
    def capacity(self):
        return self.__capacity

    def info(self):
        return f"Скорость: {self.speed}, Ёмкость: {self.capacity}"

    def is_fast(self, limit=100):
        return self.speed > limit

    @classmethod
    def from_dict(cls, some_dict):
        #Создаёт объект из словаря с ключами speed и capacity
        return cls(some_dict["speed"], some_dict["capacity"])


class Bus(Transport):
    """Автобус: транспорт с маршрутом"""
    def __init__(self, speed, capacity, route):
        """
        Создаёт автобус с заданными скоростью, ёмкостью и маршрутом
        :param speed: скорость автобуса
        :param capacity: емкость автобуса
        :param route: маршрут автобуса
        """
        super().__init__(speed, capacity)
        self.__route = route

    @property
    def route(self):
        return self.__route

    @route.setter
    #Устанавливает маршрут с проверкой на непустую строку
    def route(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Надо написать маршрут текстом и маршрут не должен быть пустой строкой")
        self.__route = value

    def info(self):
        return {super().info()} + f", Маршрут: {self.route}"

    @classmethod
    def from_dict(cls, some_dict):
        return cls(some_dict["speed"],some_dict["capacity"],some_dict["route"])


class Truck(Transport):
    """Грузовик: транспорт с грузоподъемностью"""
    def __init__(self, speed, capacity, load_capacity):
        """
        Создаёт грузовик с заданными скоростью, ёмкостью и грузоподъёмностью
        :param speed: скорость
        :param capacity: емкость
        :param load_capacity: грузоподьемность
        """
        super().__init__(speed, capacity)
        self.__load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self.__load_capacity

    def delivery_cost(self, distance, price_per_km=10):
        return distance * price_per_km + self.load_capacity * 5

    def info(self):
        return super().info() + f", грузоподъёмность: {self.load_capacity}"

    @classmethod
    def from_dict(cls, some_dict):
        return cls(some_dict["speed"], some_dict["capacity"], some_dict["load_capacity"])


class Taxi(Transport):
    """Такси: транспорт с тарифом за километр"""
    def __init__(self, speed, capacity, tariff):
        """
        Создает такси с заданными скоростью, емкостью и тарифом
        :param speed: скорость
        :param capacity: емкость
        :param tariff: тариф за км
        """
        super().__init__(speed, capacity)
        self.__tariff = tariff

    @property
    def tariff(self):
        return self.__tariff

    def ride_cost(self, distance):
        return distance * self.tariff

    def info(self):
        return super().info() + f", Тариф: {self.tariff}"

    @classmethod
    def from_dict(cls, some_dict):
        return cls(some_dict["speed"], some_dict["capacity"], some_dict["tariff"])


#ДЕМОНСТРАЦИЯ
# 1. Создание объектов через конструктор
t = Transport(100, 30)
bus = Bus(60, 40, "маршрут 177")
truck = Truck(70, 2, 5000)
taxi = Taxi(80, 4, 25)

print("1. Создание через конструктор:")
print(bus.info())
print(truck.info())
print(taxi.info())

#из словаря
print("1.2. Создание из словаря")
t1 = Transport.from_dict({"speed": 50, "capacity": 30})
b1 = Bus.from_dict({"speed": 50, "capacity": 30, "route": "№20"})
tr1 = Truck.from_dict({"speed": 70, "capacity": 2, "load_capacity": 5000})
tx1 = Taxi.from_dict({"speed": 80, "capacity": 4, "tariff": 25})

print(t1.info())
print(b1.info())
print(tr1.info())
print(tx1.info())

#2. Попытка задать недопустимую скорость
print("2. Попытка задать недопустимую скорость:")
try:
    Transport(-10, 20)
except ValueError:
    print("Недопустимое значение для скорости или емкости")


#3. вызов метода без создания объекта
print("3. вызов метода без создания объекта")
print(Transport.from_dict({"speed": 55, "capacity": 25}).info())


#4. полиморфный вызов метода для списка разных транспортных средств.
print("4. Полиморфный вызов метода info")
vehicles = [bus, truck, taxi]
for v in vehicles:
    print(v.info())






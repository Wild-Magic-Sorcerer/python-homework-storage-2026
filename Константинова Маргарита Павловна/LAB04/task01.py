#!/usr/bin/env python3

from typing import Any, Self

MAKSIMALNAYA_SKOROST: float = 400.0
MAKSIMALNAYA_EMKOST: float = 500.0


class Transport:
    """Базовое транспортное средство с проверенными скоростью и емкостью."""

    def __init__(self, skorost: float, emkost: float) -> None:
        """Создает транспорт, проверяя допустимость скорости и емкости."""
        self._proverit_skorost(skorost)
        self._proverit_emkost(emkost)
        self.__skorost: float = skorost
        self.__emkost: float = emkost

    @staticmethod
    def _proverit_skorost(skorost: float) -> None:
        """Проверяет, что скорость положительна и не превышает предел."""
        if not (0 < skorost <= MAKSIMALNAYA_SKOROST):
            raise ValueError(f"недопустимая скорость: {skorost}")

    @staticmethod
    def _proverit_emkost(emkost: float) -> None:
        """Проверяет, что емкость положительна и не превышает предел."""
        if not (0 < emkost <= MAKSIMALNAYA_EMKOST):
            raise ValueError(f"недопустимая емкость: {emkost}")

    @property
    def skorost(self) -> float:
        """Возвращает скорость транспорта."""
        return self.__skorost

    @property
    def emkost(self) -> float:
        """Возвращает емкость транспорта."""
        return self.__emkost

    def harakteristiki(self) -> str:
        """Возвращает строку с основными характеристиками транспорта."""
        return f"{type(self).__name__}: скорость {self.__skorost} км/ч, емкость {self.__emkost}"

    def prevysila_otmetku(self, otmetka: float) -> bool:
        """Возвращает True, если скорость транспорта превысила заданную отметку."""
        return self.__skorost > otmetka

    @classmethod
    def iz_slovarya(cls, dannye: dict[str, Any]) -> Self:
        """Создает объект транспорта из словаря с его параметрами."""
        return cls(**dannye)


class Bus(Transport):
    """Автобус с маршрутом."""

    def __init__(self, skorost: float, emkost: float, marshrut: str = "") -> None:
        """Создает автобус с маршрутом поверх базовых характеристик транспорта."""
        super().__init__(skorost, emkost)
        self.__marshrut: str = marshrut

    @property
    def marshrut(self) -> str:
        """Возвращает текущий маршрут автобуса."""
        return self.__marshrut

    @marshrut.setter
    def marshrut(self, novyi_marshrut: str) -> None:
        """Задает новый маршрут автобуса."""
        self.__marshrut = novyi_marshrut

    def harakteristiki(self) -> str:
        """Возвращает строку с характеристиками автобуса, включая маршрут."""
        return f"{super().harakteristiki()}, маршрут {self.__marshrut!r}"


class Truck(Transport):
    """Грузовик с грузоподъемностью."""

    TARIF_ZA_TONNOKILOMETR: float = 15.0

    def __init__(self, skorost: float, emkost: float, gruzopodyemnost: float) -> None:
        """Создает грузовик поверх базовых характеристик транспорта."""
        super().__init__(skorost, emkost)
        self.__gruzopodyemnost: float = gruzopodyemnost

    @property
    def gruzopodyemnost(self) -> float:
        """Возвращает грузоподъемность грузовика."""
        return self.__gruzopodyemnost

    def stoimost_perevozki(self, rasstoyanie: float) -> float:
        """Возвращает стоимость перевозки груза на заданное расстояние."""
        return self.__gruzopodyemnost * rasstoyanie * self.TARIF_ZA_TONNOKILOMETR

    def harakteristiki(self) -> str:
        """Возвращает строку с характеристиками грузовика, включая грузоподъемность."""
        return f"{super().harakteristiki()}, грузоподъемность {self.__gruzopodyemnost} т"


class Taxi(Transport):
    """Такси с тарифом за километр."""

    def __init__(self, skorost: float, emkost: float, tarif: float) -> None:
        """Создает такси поверх базовых характеристик транспорта."""
        super().__init__(skorost, emkost)
        self.__tarif: float = tarif

    @property
    def tarif(self) -> float:
        """Возвращает тариф такси за километр."""
        return self.__tarif

    def stoimost_poezdki(self, rasstoyanie: float) -> float:
        """Возвращает стоимость поездки на заданное расстояние."""
        return self.__tarif * rasstoyanie

    def harakteristiki(self) -> str:
        """Возвращает строку с характеристиками такси, включая тариф."""
        return f"{super().harakteristiki()}, тариф {self.__tarif} руб/км"


if __name__ == "__main__":
    avtobus = Bus(60.0, 40.0, "Маршрут 10")
    gruzovik = Truck(90.0, 3.0, 5.0)
    taksi_iz_slovarya = Taxi.iz_slovarya({"skorost": 120.0, "emkost": 4.0, "tarif": 35.0})

    print("Такси создано методом из словаря без предварительного создания объекта:")
    print(taksi_iz_slovarya.harakteristiki())

    try:
        Taxi(-10.0, 4.0, 35.0)
    except ValueError as oshibka:
        print(f"Ошибка при создании транспорта: {oshibka}")

    try:
        Bus(60.0, -5.0, "Маршрут 1")
    except ValueError as oshibka:
        print(f"Ошибка при создании транспорта: {oshibka}")

    transportnye_sredstva: list[Transport] = [avtobus, gruzovik, taksi_iz_slovarya]
    for sredstvo in transportnye_sredstva:
        print(sredstvo.harakteristiki())
        print(sredstvo.prevysila_otmetku(80.0))

#!/usr/bin/env python3

import random
from abc import ABC, abstractmethod
from typing import Self

VOZRAST_SOVERSHENNOLETIYA: int = 18
DOPUSTIMYE_POLY: tuple[str, str] = ("м", "ж")
PENSIONNYI_VOZRAST_MUZHCHIN: int = 65
PENSIONNYI_VOZRAST_ZHENSHCHIN: int = 60
MESYATSEV_V_GODU: int = 12


class Person:
    """Человек с именем, полом и возрастом."""

    def __init__(self, imya: str, pol: str, vozrast: int) -> None:
        """Создает человека, проверяя пол и возраст."""
        if pol not in DOPUSTIMYE_POLY:
            raise ValueError(f"недопустимый пол: {pol}")
        if vozrast < 0:
            raise ValueError(f"недопустимый возраст: {vozrast}")
        self.__imya: str = imya
        self.__pol: str = pol
        self.__vozrast: int = vozrast

    @property
    def imya(self) -> str:
        """Возвращает имя человека."""
        return self.__imya

    @property
    def pol(self) -> str:
        """Возвращает пол человека."""
        return self.__pol

    @property
    def vozrast(self) -> int:
        """Возвращает возраст человека."""
        return self.__vozrast

    def predstavit(self) -> str:
        """Возвращает строку с представлением человека."""
        return f"{self.__imya}, пол {self.__pol}, возраст {self.__vozrast}"

    def eto_vzrosly(self) -> bool:
        """Возвращает True, если человек достиг совершеннолетия."""
        return self.__vozrast >= VOZRAST_SOVERSHENNOLETIYA

    @classmethod
    def iz_peremennyh(cls, imya: str, pol: str, vozrast: int) -> Self:
        """Создает человека из переданных переменных."""
        return cls(imya, pol, vozrast)


class Employee(Person, ABC):
    """Сотрудник с должностью, зарплатой и расходами, умирающий при их превышении."""

    def __init__(
        self,
        imya: str,
        pol: str,
        vozrast: int,
        dolzhnost: str,
        zarplata: float,
        srednie_raskhody: float,
    ) -> None:
        """Создает сотрудника, проверяя зарплату, расходы и их соотношение."""
        super().__init__(imya, pol, vozrast)
        if zarplata <= 0:
            raise ValueError(f"недопустимая зарплата: {zarplata}")
        if srednie_raskhody < 0:
            raise ValueError(f"недопустимые расходы: {srednie_raskhody}")
        if srednie_raskhody > zarplata:
            raise ValueError(f"{imya} умер: расходы {srednie_raskhody} превышают зарплату {zarplata}")
        self.__dolzhnost: str = dolzhnost
        self.__zarplata: float = zarplata
        self.__srednie_raskhody: float = srednie_raskhody

    @property
    def dolzhnost(self) -> str:
        """Возвращает должность сотрудника."""
        return self.__dolzhnost

    @property
    def zarplata(self) -> float:
        """Возвращает зарплату сотрудника."""
        return self.__zarplata

    @property
    def srednie_raskhody(self) -> float:
        """Возвращает средние расходы сотрудника в месяц."""
        return self.__srednie_raskhody

    def predstavit(self) -> str:
        """Возвращает строку с представлением сотрудника, дополняя представление человека."""
        return f"{super().predstavit()}, должность {self.__dolzhnost}, зарплата {self.__zarplata}"

    @abstractmethod
    def rabotat(self) -> str:
        """Описывает работу сотрудника, зависящую от его конкретной должности."""

    def otsenit_pritok_deneg(self, n_mesyatsev: int) -> float:
        """Возвращает чистый приток денег сотрудника за заданное количество месяцев."""
        return (self.__zarplata - self.__srednie_raskhody) * n_mesyatsev

    def rasschitat_nakopleniya_k_pensii(self) -> float:
        """Возвращает сумму, которую сотрудник накопит к пенсии при текущих доходах и расходах."""
        pensionnyi_vozrast = PENSIONNYI_VOZRAST_MUZHCHIN if self.pol == "м" else PENSIONNYI_VOZRAST_ZHENSHCHIN
        mesyatsev_do_pensii = max(0, (pensionnyi_vozrast - self.vozrast) * MESYATSEV_V_GODU)
        return self.otsenit_pritok_deneg(mesyatsev_do_pensii)


class Manager(Employee):
    """Менеджер со списком подчиненных."""

    def __init__(self, imya: str, pol: str, vozrast: int, zarplata: float, srednie_raskhody: float) -> None:
        """Создает менеджера с должностью 'менеджер' и пустым списком подчиненных."""
        super().__init__(imya, pol, vozrast, "менеджер", zarplata, srednie_raskhody)
        self.__podchinennye: list[str] = []

    @property
    def podchinennye(self) -> list[str]:
        """Возвращает копию списка подчиненных менеджера."""
        return list(self.__podchinennye)

    def dobavit_podchinennogo(self, imya_podchinennogo: str) -> None:
        """Добавляет подчиненного менеджеру."""
        self.__podchinennye.append(imya_podchinennogo)

    def udalit_podchinennogo(self, imya_podchinennogo: str) -> None:
        """Удаляет подчиненного у менеджера."""
        self.__podchinennye.remove(imya_podchinennogo)

    def provesti_miting(self) -> str:
        """Проводит совещание для текущих подчиненных менеджера."""
        return f"{self.imya} проводит совещание для {len(self.__podchinennye)} подчиненных"

    def rabotat(self) -> str:
        """Описывает работу менеджера как управление подчиненными."""
        return f"{self.imya} управляет командой из {len(self.__podchinennye)} человек"

    def predstavit(self) -> str:
        """Возвращает строку с представлением менеджера, дополняя представление сотрудника."""
        return f"{super().predstavit()}, подчиненных {len(self.__podchinennye)}"


class Developer(Employee):
    """Разработчик со списком языков программирования."""

    def __init__(
        self,
        imya: str,
        pol: str,
        vozrast: int,
        zarplata: float,
        srednie_raskhody: float,
        yazyki_programmirovaniya: list[str],
    ) -> None:
        """Создает разработчика с должностью 'разработчик' и списком языков программирования."""
        super().__init__(imya, pol, vozrast, "разработчик", zarplata, srednie_raskhody)
        self.__yazyki_programmirovaniya: list[str] = list(yazyki_programmirovaniya)

    @property
    def yazyki_programmirovaniya(self) -> list[str]:
        """Возвращает копию списка языков программирования разработчика."""
        return list(self.__yazyki_programmirovaniya)

    def pisat_na_sluchainom_yazyke(self) -> str:
        """Пишет программу на случайном языке из списка известных разработчику."""
        yazyk = random.choice(self.__yazyki_programmirovaniya)
        return f"{self.imya} пишет программу на {yazyk}"

    def rabotat(self) -> str:
        """Описывает работу разработчика как написание программы на случайном языке."""
        return self.pisat_na_sluchainom_yazyke()

    def predstavit(self) -> str:
        """Возвращает строку с представлением разработчика, дополняя представление сотрудника."""
        return f"{super().predstavit()}, языки {', '.join(self.__yazyki_programmirovaniya)}"


class Designer(Employee):
    """Дизайнер со списком инструментов."""

    def __init__(
        self,
        imya: str,
        pol: str,
        vozrast: int,
        zarplata: float,
        srednie_raskhody: float,
        instrumenty: list[str],
    ) -> None:
        """Создает дизайнера с должностью 'дизайнер' и списком инструментов."""
        super().__init__(imya, pol, vozrast, "дизайнер", zarplata, srednie_raskhody)
        self.__instrumenty: list[str] = list(instrumenty)

    @property
    def instrumenty(self) -> list[str]:
        """Возвращает копию списка инструментов дизайнера."""
        return list(self.__instrumenty)

    def sozdat_maket(self) -> str:
        """Создает макет с помощью первого инструмента из списка дизайнера."""
        instrument = self.__instrumenty[0]
        return f"{self.imya} создает макет с помощью {instrument}"

    def rabotat(self) -> str:
        """Описывает работу дизайнера как создание макета."""
        return self.sozdat_maket()

    def predstavit(self) -> str:
        """Возвращает строку с представлением дизайнера, дополняя представление сотрудника."""
        return f"{super().predstavit()}, инструменты {', '.join(self.__instrumenty)}"


if __name__ == "__main__":
    menedzher = Manager("Олег Смирнов", "м", 40, 150000.0, 80000.0)
    razrabotchik = Developer("Светлана Кузнецова", "ж", 28, 200000.0, 90000.0, ["Python", "Go", "Rust"])
    dizainer = Designer("Артем Волков", "м", 25, 120000.0, 70000.0, ["Figma", "Photoshop"])

    menedzher.dobavit_podchinennogo(razrabotchik.imya)
    menedzher.dobavit_podchinennogo(dizainer.imya)
    print(menedzher.provesti_miting())

    try:
        Manager("Иван Иванов", "м", 30, 50000.0, 60000.0)
    except ValueError as oshibka:
        print(f"Ошибка при создании сотрудника: {oshibka}")

    sotrudniki: list[Employee] = [menedzher, razrabotchik, dizainer]
    for sotrudnik in sotrudniki:
        print(sotrudnik.predstavit())
        print(sotrudnik.rabotat())
        print(sotrudnik.rasschitat_nakopleniya_k_pensii())

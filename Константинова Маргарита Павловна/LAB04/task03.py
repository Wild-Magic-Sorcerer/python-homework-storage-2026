#!/usr/bin/env python3

import random
from abc import ABC, abstractmethod
from typing import Self

VOZRAST_SOVERSHENNOLETIYA: int = 18
DOPUSTIMYE_POLY: tuple[str, str] = ("м", "ж")
PENSIONNYI_VOZRAST_MUZHCHIN: int = 65
PENSIONNYI_VOZRAST_ZHENSHCHIN: int = 60
MESYATSEV_V_GODU: int = 12
DOLZHNOST_MENEDZHERA: str = "менеджер"
DOLZHNOST_RAZRABOTCHIKA: str = "разработчик"
DOLZHNOST_DIZAINERA: str = "дизайнер"


class SotrudnikUmer(Exception):
    """Исключение, означающее смерть сотрудника от нехватки денег на жизнь."""


class Person:
    """Человек с именем, полом и возрастом."""

    def __init__(self, imya: str, pol: str, vozrast: int) -> None:
        """Создает человека, проверяя пол и возраст."""
        if pol not in DOPUSTIMYE_POLY:
            raise ValueError(f"недопустимый пол: {pol}")
        if vozrast < 0:
            raise ValueError(f"недопустимый возраст: {vozrast}")
        self._imya: str = imya
        self._pol: str = pol
        self._vozrast: int = vozrast

    @property
    def imya(self) -> str:
        """Возвращает имя человека."""
        return self._imya

    @property
    def pol(self) -> str:
        """Возвращает пол человека."""
        return self._pol

    @property
    def vozrast(self) -> int:
        """Возвращает возраст человека."""
        return self._vozrast

    def predstavit(self) -> str:
        """Возвращает строку с представлением человека."""
        return f"{self._imya}, пол {self._pol}, возраст {self._vozrast}"

    def eto_vzrosly(self) -> bool:
        """Возвращает True, если человек достиг совершеннолетия."""
        return self._vozrast >= VOZRAST_SOVERSHENNOLETIYA

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
            raise SotrudnikUmer(f"{imya} умер: расходы {srednie_raskhody} превышают зарплату {zarplata}")
        self._dolzhnost: str = dolzhnost
        self._zarplata: float = zarplata
        self._srednie_raskhody: float = srednie_raskhody

    @property
    def dolzhnost(self) -> str:
        """Возвращает должность сотрудника."""
        return self._dolzhnost

    @property
    def zarplata(self) -> float:
        """Возвращает зарплату сотрудника."""
        return self._zarplata

    @property
    def srednie_raskhody(self) -> float:
        """Возвращает средние расходы сотрудника в месяц."""
        return self._srednie_raskhody

    def predstavit(self) -> str:
        """Возвращает строку с представлением сотрудника, дополняя представление человека."""
        return f"{super().predstavit()}, должность {self._dolzhnost}, зарплата {self._zarplata}"

    @abstractmethod
    def rabotat(self) -> str:
        """Описывает работу сотрудника, зависящую от его конкретной должности."""

    def otsenit_pritok_deneg(self, n_mesyatsev: int) -> float:
        """Возвращает чистый приток денег сотрудника за заданное количество месяцев."""
        return (self._zarplata - self._srednie_raskhody) * n_mesyatsev

    def rasschitat_nakopleniya_k_pensii(self) -> float:
        """Возвращает сумму, которую сотрудник накопит к пенсии при текущих доходах и расходах."""
        pensionnyi_vozrast = PENSIONNYI_VOZRAST_MUZHCHIN if self.pol == "м" else PENSIONNYI_VOZRAST_ZHENSHCHIN
        mesyatsev_do_pensii = max(0, (pensionnyi_vozrast - self.vozrast) * MESYATSEV_V_GODU)
        return self.otsenit_pritok_deneg(mesyatsev_do_pensii)


class Manager(Employee):
    """Менеджер со списком подчиненных."""

    def __init__(self, imya: str, pol: str, vozrast: int, zarplata: float, srednie_raskhody: float) -> None:
        """Создает менеджера с должностью менеджера и пустым списком подчиненных."""
        super().__init__(imya, pol, vozrast, DOLZHNOST_MENEDZHERA, zarplata, srednie_raskhody)
        self._podchinennye: list[str] = []

    @property
    def podchinennye(self) -> list[str]:
        """Возвращает копию списка подчиненных менеджера."""
        return list(self._podchinennye)

    def dobavit_podchinennogo(self, imya_podchinennogo: str) -> None:
        """Добавляет подчиненного менеджеру."""
        self._podchinennye.append(imya_podchinennogo)

    def udalit_podchinennogo(self, imya_podchinennogo: str) -> None:
        """Удаляет подчиненного у менеджера."""
        self._podchinennye.remove(imya_podchinennogo)

    def provesti_miting(self) -> str:
        """Проводит совещание для текущих подчиненных менеджера."""
        return f"{self.imya} проводит совещание для {len(self._podchinennye)} подчиненных"

    def rabotat(self) -> str:
        """Описывает работу менеджера как управление подчиненными."""
        return f"{self.imya} управляет командой из {len(self._podchinennye)} человек"

    def predstavit(self) -> str:
        """Возвращает строку с представлением менеджера, дополняя представление сотрудника."""
        return f"{super().predstavit()}, подчиненных {len(self._podchinennye)}"


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
        """Создает разработчика с должностью разработчика и списком языков программирования."""
        super().__init__(imya, pol, vozrast, DOLZHNOST_RAZRABOTCHIKA, zarplata, srednie_raskhody)
        self._yazyki_programmirovaniya: list[str] = yazyki_programmirovaniya

    @property
    def yazyki_programmirovaniya(self) -> list[str]:
        """Возвращает копию списка языков программирования разработчика."""
        return list(self._yazyki_programmirovaniya)

    def pisat_na_sluchainom_yazyke(self) -> str:
        """Пишет программу на случайном языке из списка известных разработчику."""
        yazyk = random.choice(self._yazyki_programmirovaniya)
        return f"{self.imya} пишет программу на {yazyk}"

    def rabotat(self) -> str:
        """Описывает работу разработчика как написание программы на случайном языке."""
        return self.pisat_na_sluchainom_yazyke()

    def predstavit(self) -> str:
        """Возвращает строку с представлением разработчика, дополняя представление сотрудника."""
        return f"{super().predstavit()}, языки {', '.join(self._yazyki_programmirovaniya)}"


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
        """Создает дизайнера с должностью дизайнера и списком инструментов."""
        super().__init__(imya, pol, vozrast, DOLZHNOST_DIZAINERA, zarplata, srednie_raskhody)
        self._instrumenty: list[str] = instrumenty

    @property
    def instrumenty(self) -> list[str]:
        """Возвращает копию списка инструментов дизайнера."""
        return list(self._instrumenty)

    def sozdat_maket(self) -> str:
        """Создает макет с помощью первого инструмента из списка дизайнера."""
        if not self._instrumenty:
            raise ValueError("у дизайнера нет доступных инструментов")
        instrument = self._instrumenty[0]
        return f"{self.imya} создает макет с помощью {instrument}"

    def rabotat(self) -> str:
        """Описывает работу дизайнера как создание макета."""
        return self.sozdat_maket()

    def predstavit(self) -> str:
        """Возвращает строку с представлением дизайнера, дополняя представление сотрудника."""
        return f"{super().predstavit()}, инструменты {', '.join(self._instrumenty)}"


if __name__ == "__main__":
    menedzher = Manager("Олег Смирнов", "м", 40, 150000.0, 80000.0)
    razrabotchik = Developer("Светлана Кузнецова", "ж", 28, 200000.0, 90000.0, ["Python", "Go", "Rust"])
    dizainer = Designer("Артем Волков", "м", 25, 120000.0, 70000.0, ["Figma", "Photoshop"])

    menedzher.dobavit_podchinennogo(razrabotchik.imya)
    menedzher.dobavit_podchinennogo(dizainer.imya)
    print(menedzher.provesti_miting())

    try:
        Manager("Иван Иванов", "м", 30, 50000.0, 60000.0)
    except SotrudnikUmer as oshibka:
        print(f"Ошибка при создании сотрудника: {oshibka}")

    for sotrudnik in (menedzher, razrabotchik, dizainer):
        print(sotrudnik.predstavit())
        print(sotrudnik.rabotat())
        print(sotrudnik.rasschitat_nakopleniya_k_pensii())

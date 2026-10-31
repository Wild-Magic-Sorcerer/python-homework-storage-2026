#!/usr/bin/env python3

from typing import Self


class BankAccount:
    """Банковский счет с балансом, владельцем и историей операций."""

    def __init__(self, vladelets: str, nachalny_balans: float = 0.0) -> None:
        """Создает счет с начальным балансом, проверяя его корректность."""
        if nachalny_balans < 0:
            raise ValueError(f"недопустимый начальный баланс: {nachalny_balans}")
        self.__vladelets: str = vladelets
        self.__balans: float = nachalny_balans
        self.__istoriya: list[str] = []

    @property
    def vladelets(self) -> str:
        """Возвращает владельца счета."""
        return self.__vladelets

    @property
    def balans(self) -> float:
        """Возвращает текущий баланс счета."""
        return self.__balans

    @property
    def istoriya(self) -> list[str]:
        """Возвращает копию истории операций по счету."""
        return list(self.__istoriya)

    def popolnit(self, summa: float) -> None:
        """Пополняет счет на заданную сумму."""
        if summa <= 0:
            raise ValueError(f"недопустимая сумма пополнения: {summa}")
        self.__balans += summa
        self.__istoriya.append(f"пополнение на {summa}")

    def snyat(self, summa: float) -> None:
        """Снимает со счета заданную сумму."""
        if summa <= 0:
            raise ValueError(f"недопустимая сумма снятия: {summa}")
        if summa > self.__balans:
            raise ValueError(f"сумма снятия превышает баланс: {summa} > {self.__balans}")
        self.__balans -= summa
        self.__istoriya.append(f"снятие на {summa}")

    @classmethod
    def sozdat_schet(cls, vladelets: str, nachalny_balans: float = 0.0) -> Self:
        """Создает новый банковский счет с заданным владельцем и начальным балансом."""
        return cls(vladelets, nachalny_balans)


class SavingsAccount(BankAccount):
    """Сберегательный счет с процентной ставкой."""

    MAKSIMALNAYA_DOLYA_SNYATIYA: float = 0.5

    def __init__(self, vladelets: str, nachalny_balans: float, protsentnaya_stavka: float) -> None:
        """Создает сберегательный счет, проверяя процентную ставку."""
        super().__init__(vladelets, nachalny_balans)
        if protsentnaya_stavka < 0:
            raise ValueError(f"недопустимая процентная ставка: {protsentnaya_stavka}")
        self.__protsentnaya_stavka: float = protsentnaya_stavka

    @property
    def protsentnaya_stavka(self) -> float:
        """Возвращает процентную ставку сберегательного счета."""
        return self.__protsentnaya_stavka

    def nachislit_protsenty(self) -> None:
        """Начисляет проценты на текущий баланс счета."""
        self.popolnit(self.balans * self.__protsentnaya_stavka)

    def snyat(self, summa: float) -> None:
        """Снимает со счета сумму, не превышающую половину баланса за одну операцию."""
        if summa > self.balans * self.MAKSIMALNAYA_DOLYA_SNYATIYA:
            raise ValueError(f"нельзя снять более {self.MAKSIMALNAYA_DOLYA_SNYATIYA:.0%} баланса за одну операцию")
        super().snyat(summa)


if __name__ == "__main__":
    schet = BankAccount.sozdat_schet("Иван Иванов", 1000.0)
    sberschet = SavingsAccount("Анна Петрова", 2000.0, 0.05)

    schet.popolnit(500.0)
    schet.snyat(200.0)

    try:
        schet.popolnit(-100.0)
    except ValueError as oshibka:
        print(f"Ошибка операции: {oshibka}")

    try:
        schet.snyat(10000.0)
    except ValueError as oshibka:
        print(f"Ошибка операции: {oshibka}")

    try:
        schet.balans = 999999.0  # type: ignore[attr-defined]
    except AttributeError as oshibka:
        print(f"Нельзя изменить баланс напрямую: {oshibka}")

    sberschet.nachislit_protsenty()
    print(schet.istoriya)
    print(sberschet.istoriya)

    scheta: list[BankAccount] = [schet, sberschet]
    for odin_schet in scheta:
        try:
            odin_schet.snyat(odin_schet.balans * 0.6)
        except ValueError as oshibka:
            print(f"Полиморфное снятие для {type(odin_schet).__name__} вызвало ошибку: {oshibka}")
        else:
            print(f"Полиморфное снятие для {type(odin_schet).__name__} прошло успешно, новый баланс {odin_schet.balans}")

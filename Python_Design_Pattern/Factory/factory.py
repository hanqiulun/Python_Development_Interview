# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: factory.py
Description : 
Project: Factory
Last Modified: Monday, 25th March 2019 9:56:45 pm
-------------------------------------------------------------
'''

from dataclasses import dataclass
from typing import (
    NoReturn,
    ClassVar
)

# Burger Class
@dataclass
class Burger:
    name: str = ""
    price: float = 0.0
    type: str = "BURGER"

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, price) -> NoReturn:
        self.price = price

    def getName(self) -> str:
        return self.name


@dataclass
class cheeseBurger(Burger):
    name: str = "cheese burger"
    price: float = 10.0


@dataclass
class spicyChickenBurger(Burger):
    name: str = "spicy chicken burger"
    price: float = 15.0

# Snack Class
@dataclass
class Snack:
    name: str = ""
    price: float = 0.0
    type: str = "SNACK"

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, price) -> NoReturn:
        self.price = price

    def getName(self) -> str:
        return self.name


@dataclass
class chips(Snack):
    name: str = "chips"
    price: float = 6.0


@dataclass
class chickenWings(Snack):
    name: str = "chicken wings"
    price: float = 12.0


# Beverage Class
@dataclass
class Beverage:
    name: str = ""
    price: float = 0.0
    type: str = "BEVERAGE"

    def getPrice(self) -> float:
        return self.price

    def setPrice(self, price) -> NoReturn:
        self.price = price

    def getName(self) -> str:
        return self.name


@dataclass
class coke(Beverage):
    name: str = "coke"
    price: float = 4.0


@dataclass
class milk(Beverage):
    name: str = "milk"
    price: float = 5.0

# Factory
@dataclass
class foodFactory:
    type: str = ""

    def createFood(self, foodClass) -> ClassVar:
        print(self.type, " factory produce a instance.")
        foodIns = foodClass()
        return foodIns


@dataclass
class burgerFactory(foodFactory):
    type: str = "BURGER"


@dataclass
class snackFactory(foodFactory):
    type: str = "SNACK"


@dataclass
class beverageFactory(foodFactory):
    type: str = "BEVERAGE"


if __name__ == "__main__":
    burger_factory = burgerFactory()
    snack_factorry = snackFactory()
    beverage_factory = beverageFactory()
    cheese_burger = burger_factory.createFood(cheeseBurger)
    print(cheese_burger.getName(), cheese_burger.getPrice())
    chicken_wings = snack_factorry.createFood(chickenWings)
    print(chicken_wings.getName(), chicken_wings.getPrice())
    coke_drink = beverage_factory.createFood(coke)
    print(coke_drink.getName(), coke_drink.getPrice())

#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = None
        self.size = size

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if isinstance(value, str):
            self._brand = value
        else:
            print("Brand must be a string")

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
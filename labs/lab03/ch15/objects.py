# Starting file for Lab 3 - objects.py
# Name: Temitope S. Olugbemi
# Date: 10-27-2026
# Class: Dev 128

from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

# Intermediateclass inheriting from Product
class Media(Product):
    def __init__(self, name:str = "", price:float = 0.0, discountPercent:int = 0, format:str = ""):
        super().__init__(name, price, discountPercent)
        self.format = format

@dataclass
class Book(Media):

    def __init__(self, name:str = "", price:float = 0.0, discountPercent:int = 0, author:str = "", format:str = ""):
        super().__init__(name, price, discountPercent, format)
        self.author = author

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author}"

@dataclass        
class Movie(Media):
    def __init__(self, name:str = "", price:float = 0.0, discountPercent:int = 0, year:int = 0, format:str = ""):
        super().__init__(name, price, discountPercent, format)
        self.year = year
    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year})"

@dataclass
class Album(Media):
    def __init__(self, name:str = "", price:float = 0.0, discountPercent:int = 0, artist:str = "", format:str = ""):
        super().__init__(name, price, discountPercent, format)
        self.artist = artist

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.artist}"

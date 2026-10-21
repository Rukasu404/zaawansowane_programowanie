class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Dom o powierzchni {self.area} z {self.rooms} pokojami. Cena: {self.price} Adres: {self.address} Działka: {self.plot}'

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Mieszkanie o powierzchni {self.area} z {self.rooms} pokojami. Cena: {self.price} Adres: {self.address} Piętro: {self.floor}'

prop_01 = Property(10,5,999999, 'Aszynbecher 3')
house_01 = House(60,5,999992929,'Aszynbecher 2', 99)
flat_01 = Flat(99,2,67,'Aszynbecher 1', 2)

print(house_01)
print(flat_01)
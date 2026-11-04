from magazine import Property

class Flat(Property.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f'Mieszkanie o powierzchni {self.area} '
                f'z {self.rooms} pokojami. '
                f'Cena: {self.price} Adres: {self.address} '
                f'Piętro: {self.floor}')
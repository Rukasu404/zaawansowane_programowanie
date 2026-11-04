from magazine import Property

class House(Property.Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f'Dom o powierzchni {self.area} '
                f'z {self.rooms} pokojami. '
                f'Cena: {self.price} Adres: {self.address} '
                f'Działka: {self.plot}')
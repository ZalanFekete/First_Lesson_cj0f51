import random as rnd

class TicketFZ:
    def __init__(self, name, destination, date):
        self.name = name
        self.destination = destination
        self.date = date
        self.price = rnd.randint(1000, 10000)
        self.delay = rnd.randint(5, 50)

        if self.delay < 25:
            self.delay_type = "Enyhe késés!"
        elif self.delay < 35:
            self.delay_type = "Sokat késik!"
        else:
            self.delay_type = "Rengeteget késik!"

    def __str__(self):
        return (
            f"Utas: {self.name} → Cél: {self.destination}\n"
            f"Dátum: {self.date} | Ár: {self.price} Ft"
            f"\nKésés: {self.delay} perc — {self.delay_type}"
        )






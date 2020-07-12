class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, add_dollars, add_cents):
        if self.cents + add_cents >= 100:
            self.dollars += (self.cents + add_cents) // 100
            self.cents = (self.cents + add_cents) % 100
        else:
            self.cents += add_cents
        self.dollars += add_dollars

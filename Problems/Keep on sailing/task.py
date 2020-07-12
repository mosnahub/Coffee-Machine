# our class Ship
class Ship:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return f"The {self.name} has sailed for {self.country}!"

country = input()
black_pearl = Ship("Black Pearl", country)
print(black_pearl.sail())

# put your python code here
class Trip:
    def __init__(self, days, foodc_day, oneway_flight, hotel_cost):
        self.days = days
        self.foodc_day = foodc_day
        self.oneway_flight = oneway_flight
        self.hotel_cost = hotel_cost

    def sum_money(self):
        return (self.foodc_day * self.days) + (self.oneway_flight * 2) + (self.hotel_cost * (self.days - 1))


days = int(input())
foodc_day = int(input())
oneway_flight = int(input())
hotel_cost = int(input())

trip = Trip(days, foodc_day, oneway_flight, hotel_cost)
print(trip.sum_money())

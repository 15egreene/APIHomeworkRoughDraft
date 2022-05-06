# OOP - Create your own object. Make at least two additional methods for it.

'''

Amazon Car Sales

let user see cars and prices and small description
option inside show to show larger description of car
let user buy car based on credit
let user buy car based on down payment
checkout
warranty plan
schedule test drive








This project is strictly fictional
'''



class CarSales():
    def __init__(self, year, name, model, price, small_description, large_description):
        self.year = year
        self.name = name
        self.model = model
        self.model = model
        self.price = price
        self.small_description = small_description
        self.large_description = large_description

    def View(self):
        print(f"Welcome to Amazon Car Sales!{self.small_description}")

    pass
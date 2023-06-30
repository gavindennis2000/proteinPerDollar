class foodItem:
    def __init__(self, name, totalPrice, numberOfServings, proteinPerServing):
        # creates foodItem object with name, price, number of servings, and protein per serving
        self.name = name # the name (e.g. chicken breast)
        self.totalPrice = totalPrice # price in dollar and cents (e.g. 5.99)
        self.numberOfServings = numberOfServings # number of servings listed on the nutrition facts (e.g. 10)
        self.proteinPerServing = proteinPerServing # protein in grams listed per serving (e.g. 40)

    def proteinPerDollar(self):
        # this method does the actual math to find out protein per dollar
        return round((self.proteinPerServing * self.numberOfServings) / self.totalPrice, 1) # round to 1 decimal place

def findProteinPerDollar(obj):
    print("The amount of protein per dollar for", obj.name, "is", obj.proteinPerDollar(), "grams")

kodiacCakes = foodItem("Kodiac Cakes", 5.99, 11, 13)
findProteinPerDollar(kodiacCakes)
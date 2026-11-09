# Abdyrakhman Raiapov
# Nov 8, 2026
# Problem 6 - The car class with two new attributes, type and manufacturer,
# their methods, and an updated fullspecs().
#
# Attribute vs. method:
# - An ATTRIBUTE is data stored inside an object, for example self.color.
#   Each car object has its own values for its attributes.
# - A METHOD is a function defined inside the class that works with the
#   object, for example get_color(). It is called with dot notation and
#   parentheses: car1.get_color().


class car:

    def __init__(self, model, year, color, type, manufacturer):
        # attributes (the data each car stores)
        self.model = model
        self.year = year
        self.color = color
        self.type = type                    # NEW attribute, e.g. "Coupe"
        self.manufacturer = manufacturer    # NEW attribute, e.g. "BMW"

    # methods (functions that return the car's data)
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):                     # NEW method
        return self.type

    def get_manufacturer(self):             # NEW method
        return self.manufacturer

    def fullspecs(self):                    # UPDATED to include the new attributes
        return (self.manufacturer + ' ' + self.model + ' ' + str(self.year) + ' '
                + self.color + ' ' + self.type)


car1 = car("Sports", 2012, "Blue", "Coupe", "BMW")
car2 = car("Sedan", 2020, "Black", "Four-door", "Toyota")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.get_type())
print(car2.get_manufacturer())
print(car1.fullspecs())
print(car2.fullspecs())

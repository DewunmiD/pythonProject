class Person:
    def __init__(self, fname, lname, price):
        self.firstname = fname
        self.lastname = lname
        self.fuelprice = price

    def printname(self):
        print(self.firstname, self.lastname)

    def fuelprice(self):
        price = 800
        return price


class Student(Person):
    def __init__(self, fname, lname, price, year, newprice):
        super().__init__(fname, lname, price)
        self.graduationyear = year
        self.newfuelprice = newprice

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    # def fuelpercentage(self):
    #     percentage = round(4000 / self.fuelprice() * 100)
    #     return percentage

#
# class Petrol(Student):
#     def __init__(self, fname, lname, price, year, newprice, litreprice):
#         super().__init__(fname, lname, price, year, newprice)
#         self.newlitreprice = litreprice
#
#     def litre(self, parent):
#         if parent == True:
#             print(self.newlitreprice * self.newfuelprice)
#             return self.newlitreprice * self.newfuelprice
#
#         elif parent == False:
#             print(self.newfuelprice)
#             return self.newfuelprice
#
# x = Petrol("Mike", "Olsen", 80, 2024, 40, 10)
#
# print(x.fuelprice)
# print(x.newfuelprice)
# print(x.newlitreprice)
#
# print(x.litre)

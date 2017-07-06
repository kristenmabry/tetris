# name: Kristen Mabry
# collaborators: no one
# moving.py
# I have to guess the output

"""
I think it will print:
10
PEW
100
united

"""

class Vehicles:
 
    def __init__(self, heavy, people):
        self.weight = heavy
        self.occupancy = people
 
    def getWeight(self):
        return int(self.weight)
 
    def getOccupancy(self):
        return self.occupancy
 
class Plane(Vehicles):
 
    def __init__(self, heavy, people, airline):
        Vehicles.__init__(self, heavy, people)
        self.airline=airline
 
    def fly(self):
        return "PEW"
 
 
x = Vehicles(10, 1)
y = Plane(1000, 100, "united")
 
print(x.getWeight())
print(y.fly())
print(y.getOccupancy() )
print(y.airline)

# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid:

    def __init__ (self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def getSurface(self):
        surface = (self.sideC * self.sideB) * 2 + (self.sideC * self.sideA) * 2 + (self.sideA * self.sideB) * 2
        return surface

    def getVolume(self):
        volume = self.sideA * self.sideB * self.sideC
        return volume

cuboid1 = Cuboid(2, 4, 3)

cuboid1.getSurface()
cuboid1.getVolume()

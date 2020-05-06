'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result

V=4/3pir^3 - vol Sphere
4pir^2- SA
'''

from math import pi
class cylinder:
    def __init__(self, radius,height):
        self.r = radius
        self.h = height
    def __vol__(self):
        return ((4/3)*pi*((self.r)**2))
    def __sur__(self):
        return 4*pi*(self.r**2)
x = cylinder(3.14,5)
print(f'The volume of the cylinder is {x.__vol__()} and the surface area is {x.__sur__()}.')

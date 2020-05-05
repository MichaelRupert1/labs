'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''

class rectangle:
    def __init__(self, width, heigth):
        self.w = width
        self.h = heigth
    def __area__(self):
        return (self.w*self.h)
    def __perimeter__(self):
        return (self.w+self.h)*2
x = rectangle(2.4,6.4)
print(f'For this rectangle the area is {x.__area__()} and the perimeter is {x.__perimeter__()}.')

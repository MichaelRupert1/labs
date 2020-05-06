'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
class temp:
    def __init__(self, fah):
        self.f = fah
    def __cel__(self):
        return (self.f-32)*(5/9)

x = temp(81.32)
print(f'{x.f} degress fahrenheit = {x.__cel__()} degrees celsius')
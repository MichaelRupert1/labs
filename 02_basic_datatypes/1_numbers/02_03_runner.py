'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

class runner:
    def __init__(self, distance, time):
        self.d = distance
        self.t = time
    def __mitokm__(self):
        return self.d*1.6
    def __hour__(self):
        return (self.t/60)
    def __avgspeed__(self):
        return (self.__mitokm__())/(self.__hour__())
x = runner(10,30.5)
print(f'The runner is moving at a avg speed of {x.__avgspeed__()} Km per hour.')
#INIT usage
class Vehicle:
    def __init__ (self,max_speed,mileage):
        self.maxspeed = max_speed
        self.mileage = mileage
        
merc = Vehicle(300,650)
bmw = Vehicle(285,700)

print('The top speed of the Mercedes is',merc.maxspeed)
print('The mileage of the BMW is',bmw.mileage)
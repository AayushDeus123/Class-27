#Parrot species
class Parrot:
    species = 'Bird'
    def __init__ (self,name,age):
        self.name = name
        self.age = age

p1 = Parrot('Birdy',8)
p2 = Parrot('Woody',3)    

print('The species of this parrot is',p1.species)
print('The name of parrot 1 is',p1.name)
print('The name of parrot 2 is',p2.name)
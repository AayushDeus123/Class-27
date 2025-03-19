class Dog:
    animal = "Dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    def display(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed: {self.breed}")
        print(f"Colour: {self.colour}")
        print("-" * 20)

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("Beagle", "Tricolor")

dog1.display()
dog2.display()
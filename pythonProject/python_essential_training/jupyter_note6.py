
# Classes and Objects
class dog:
    def __init__(self,name):
        self.name = name
        self.lags = 4

    def speak (self):
        print(self.name + ' says: bark!')

my_dog = dog('Rover')
another_dog = dog('Fluffy')
my_dog.speak()
another_dog.speak()


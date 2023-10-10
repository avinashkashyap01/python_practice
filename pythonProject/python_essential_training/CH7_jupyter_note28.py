
# Instance Attributes

class dog:
    def __init__(self,name):
        self.name = name
        self.lags = 4

    def speak (self):
        print(self.name + ' says: bark!')

my_dog = dog('Rover')
print(my_dog.name)
print(my_dog.lags)


# Static Attributes

class dog:
    lags = 4
    def __init__(self,name):
        self.name = name

    def speak (self):
        print(self.name + ' says: bark!')

my_dog = dog('Rover')
print(my_dog.name)
print(my_dog.lags)

dog.lags = 3
my_dog = dog('Rover')
print(my_dog.name)
print(my_dog.lags)


class dog:
    _legs = 4
    def __init__(self,name):
        self.name = name
        self.lags = 4

    def getlegs(self):
        return self._legs

    def speak (self):
        print(self.name + ' says: bark!')

my_dog = dog('Rover')
print(my_dog.name)
print(my_dog.getlegs())

mydog = dog('Rover')
mydog._lags = 3
print(mydog._lags)
print(mydog.getlegs())
print(dog._lags)

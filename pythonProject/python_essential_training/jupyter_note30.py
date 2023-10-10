
# Class Inheritence

class dog:
    _legs = 4
    def __init__(self,name):
        self.name = name

    def bark(self):
        print(self.name + ' says: bark!')

    def getlegs(self):
        return self._legs


class chihuahua(dog):
    def speak(self):
        return f'{self.name} says: yap yap yap!'

    def wagtail(self):
        print('Vigorous wagging')

dog = chihuahua('Roxy')
print(dog.speak())
print(dog.bark())



# Extending build-in classes

# mylist = list()
#
# class uniquelist(list):
#     def append(self,item):
#         if item in self:
#             return
#         super().append(item)
#
# uniquelist = uniquelist()
# uniquelist.append(1)
# uniquelist.append(1)
# uniquelist.append(2)
#
# print(uniquelist)

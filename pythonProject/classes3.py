
class pet:
    def __init__(self,name,a,h,p):
        self.name = name
        self.age = a
        self.hunger = h
        self.playful = p
    #setter
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def gethunger(self):
        return self.hunger
    def getplayful(self):
        return self.playful

    #getter
    def setname(self,xname):
        self.name = xname
    def setage(self,age):
        self.age = age
    def sethunger(self,hunger):
        self.hunger = hunger
    def setplayful(self,play):
        self.playful = play

pet1 = pet("jim",3,False,True)

print(pet1.getname())
print(pet1.getplayful())
pet1.setname("snowball")
print(pet1.getname())
print(pet1.name)
pet1.name = "jim"
print(pet1.name)

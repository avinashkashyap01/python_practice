
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
    def __str__(self):
        return (self.name + " is " + str(self.age) + " years old")

class dog (pet):
    def __init__(self,name,age,hunger,playful,breed,favoritetoy):
        pet. __init__(self,name,age,hunger,playful)
        self.breed = breed
        self.favoritetoy = favoritetoy

    def wantstoplay(self):
         if self.playful == True :
            return ("dog wants to play with " + self.favoritetoy)
         else:
             return ("dog does't want to play")

class cat (pet):
    def __init__(self,name,age,hunger,playful,place):
        pet. __init__(self,name,age,hunger,playful)
        self.favoriteplacetosit = place

    def wantstosit(self):
        if self.playful == False:
            print("the cat wants to sit in",self.favoriteplacetosit)
        else:
            print("the cat wants to play")

    def __str__(self):
        return (self.name + " likes to sit in " + self.favoriteplacetosit)

class human :
    def __init__(self,name,pets):
        self.name = name
        self.pets = pets
    def haspets(self):
        if len(self.pets) != 0:
            return "yes"
        else:
            return "no"


huskydog = dog ("snowball",5,False,True,"husky","stick")
play = huskydog.wantstoplay()
print(play)
huskydog.playful = False
play = huskydog.wantstoplay()
print(play)
taypicalcat = cat("fluffy",3,False,False," the sun ray")
taypicalcat.wantstosit()
print(taypicalcat)
print(huskydog)

youraveragehuman = human ("alice",[huskydog,taypicalcat])
haspet = youraveragehuman.haspets()
print(haspet)
print(youraveragehuman.pets[0])
print(youraveragehuman.pets[1])
print(youraveragehuman.pets[1].name)
print(youraveragehuman.pets[0].name)

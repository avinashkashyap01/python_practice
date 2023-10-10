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
hunkydog = dog ("snowball",5,False,True,"husky","stick")

play = hunkydog.wantstoplay()
print(play)
hunkydog.playful = False
play = hunkydog.wantstoplay()
print(play)


#first
 # class classname :
 #
 #    def __init__(self):
 #        self.attribute = 0
 #
 #        def anotherfunction(self):
 #            action(s)


# class team:
#     def __init__(self,name = "name",origin = "origin"):
#         self.teamname = name
#         self.teamorigin = origin
#
#     def defineteamname (self,name):
#         self.teamname = name
#
#     def defineteamorigin (self,origin):
#         self.teamorigin = origin
#
#
# # class inheritenceclassname(ParentClass):
# #      def __init__(self,input1,input2):
# #          ParentClass.__init__(self)
# #          self.attribute1=input1
# #          self.attribute2=input2
# #          self.attribute3=0
# #      def anotherfunction(self):
# #               action(s)
#
# class player(team):
#     def __init__(self):
#         team.__init__(self)
#         self.playername = "none"
#         self.playerpoints = 0
#     def scoredpoint(self):
#         self.playerpoints += 1
#     def setname(self,name):
#         self.playername = name
#
# player1 = player()
#
# print(player1.playername)
# print(player1.playerpoints)
# print(player1.teamname)
# print(player1.teamorigin)




#second

class team:
    def __init__(self,name = "name",origin = "origin"):
        self.teamname = name
        self.teamorigin = origin

    def defineteamname (self,name):
        self.teamname = name

    def defineteamorigin (self,origin):
        self.teamorigin = origin


class player(team):
    def __init__(self,playername,playerpoints,teamname,teamorigin):
        team.__init__(self,teamname,teamorigin)
        self.playername = playername
        self.playerpoints = playerpoints
    def scoredpoint(self):
        self.playerpoints += 1
    def setname(self,name):
        self.playername = name

player1 = player("sid",0,"sharks","chicago")

print(player1.playername)
print(player1.playerpoints)
# player1.defineteamname("sharks")
print(player1.teamname)
print(player1.teamorigin)

player1.scoredpoint()
print(player1.playerpoints)

player1.setname("lee")

print(player1.teamname)



#third
class team:
    def __init__(self,name = "name",origin = "origin"):
        self.teamname = name
        self.teamorigin = origin

    def defineteamname (self,name):
        self.teamname = name

    def defineteamorigin (self,origin):
        self.teamorigin = origin


class player(team):
    def __init__(self,playername,playerpoints,teamname,teamorigin):
        team.__init__(self,teamname,teamorigin)
        self.playername = playername
        self.playerpoints = playerpoints
    def scoredpoint(self):
        self.playerpoints += 1
    def setname(self,name):
        self.playername = name
    def __str__(self):
        return self.playername + " has scored :" + str(self.playerpoints) + " points"

player1 = player("sid",0,"sharks","chicago")

print(player1.playername)
print(player1.playerpoints)
# player1.defineteamname("sharks")
print(player1.teamname)
print(player1.teamorigin)

player1.scoredpoint()
print(player1.playerpoints)

player1.setname("lee")

print(player1.teamname)
print(player1)

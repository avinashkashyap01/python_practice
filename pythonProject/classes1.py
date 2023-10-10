
# class classname :
#
#     def __init__(self):
#         self.attribute =0
#
#         def anotherfunction(self):
#             action(s)

class team:
    def __init__(self):
        self.teamname = "name"
        self.teamorigin = "origin"

    def defineteamname (self,name):
        self.teamname = name

    def defineteamorigin (self,origin):
        self.teamorigin = origin

team1 = team( )
print(team1.teamname)
team1.defineteamname("tigers")
print(team1.teamname)
print(team1.teamorigin)
team1.defineteamorigin("chicago")
print(team1.teamorigin)



# class team:
#     def __init__(self,name,origin):
#         self.teamname = name
#         self.teamorigin = origin
#
#     def defineteamname (self,name):
#         self.teamname = name
#
#     def defineteamorigin (self,origin):
#         self.teamorigin = origin
#
# team1 = team("tigers","chicago")
# team2 = team("hawks","new york")
#
# print(team1.teamname)
# team1.defineteamname("dolphin")
# print(team1.teamname)
# print(team1.teamorigin)
# team1.defineteamorigin("chicago")
# print(team2.teamname)
# print(team2.teamorigin)


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
# team1 = team("tigers","chicago")
# team2 = team("hawks","new york")
# team3 = team()
#
# print(team1.teamname)
# team1.defineteamname("dolphin")
# print(team1.teamname)
# print(team1.teamorigin)
# team1.defineteamorigin("chicago")
# print(team2.teamname)
# print(team2.teamorigin)
# print(team3.teamname)
# print(team3.teamorigin)

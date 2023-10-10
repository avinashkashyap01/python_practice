
import random as r

simplelist = [1,3,5,7,11]
pickelement = r.choice(simplelist)
print(pickelement)
r.shuffle(simplelist)
print(simplelist)

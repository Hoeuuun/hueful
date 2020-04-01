from Group import Group
from Light import Light

g = Group()
# print(g.getAllGroups())
# # ['1', '2', '3', '4', '5', '6', '8']
#
# print(g.getGroup('1'))
#
# print(g.getGroupByRoom("Living room"))
#
# print(g.getGroupByRoom("Dining room"))
# # Cannot find Dining room lights!
# # None
#
# l = Light()
# print(l.getAllLights())
# # ['2', '4', '5', '6', '7', '8']
#
# print("Turning lights")
# g.turnLights('1', True)
# #g.turnLights('1', False)


# print(g.getLights())
print("----")
print(g.getState(1))
g.setBri(1,200)
g.setHue(1,25500)
g.setSat(1, 100)
g.setXY(1, [0.555, 0.92])
g.setCT(1, 500)

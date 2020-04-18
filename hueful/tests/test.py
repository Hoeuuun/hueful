from hueful.Connection import Connection
from hueful.Group import Group
from hueful.Light import Light


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

import pytest

# print(g.getLights())
class TestHuey:
    def test_brightness(self):
        g = Group(id='1', connection=Connection(verify=False))
        print("----")
        print(g.getState(1))
        g.setBri(200)
        g.setHue(25500)
        g.setSat(100)
        g.setXY([0.555, 0.92])
        g.setCT(500)

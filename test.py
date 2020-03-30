from Group import Group
from Light import Light

g = Group()
print(g.getAllGroups())
# ['1', '2', '3', '4', '5', '6', '8']

print(g.getAGroup('1'))
# {
# 	"name": "Living room",
# 	"lights": [
# 		"8",
# 		"2"
# 	],
# 	"sensors": [],
# 	"type": "Room",
# 	"state": {
# 		"all_on": false,
# 		"any_on": false
# 	},
# 	"recycle": false,
# 	"class": "Living room",
# 	"action": {
# 		"on": false,
# 		"bri": 144,
# 		"hue": 7676,
# 		"sat": 199,
# 		"effect": "none",
# 		"xy": [
# 			0.5016,
# 			0.4151
# 		],
# 		"ct": 443,
# 		"alert": "select",
# 		"colormode": "xy"
# 	}
# }


print(g.getAGroupRoom("Living room"))
# {'name': 'Living room', 'lights': ['8', '2'], 'sensors': [], 'type': 'Room', 'state': {'all_on': False, 'any_on': False}, 'recycle': False, 'class': 'Living room', 'action': {'on': False, 'bri': 144, 'hue': 7676, 'sat': 199, 'effect': 'none', 'xy': [0.5016, 0.4151], 'ct': 443, 'alert': 'select', 'colormode': 'xy'}}
# {'name': 'Living room', 'lights': ['8', '2'], 'sensors': [], 'type': 'Room', 'state': {'all_on': False, 'any_on': False}, 'recycle': False, 'class': 'Living room', 'action': {'on': False, 'bri': 144, 'hue': 7676, 'sat': 199, 'effect': 'none', 'xy': [0.5016, 0.4151], 'ct': 443, 'alert': 'select', 'colormode': 'xy'}}


print(g.getAGroupRoom("Dining room"))
# Cannot find Dining room lights!
# None

l = Light()
print(l.getAllLights())
# ['2', '4', '5', '6', '7', '8']



# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check
#
# # get all lights
# URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n"
#
# r = requests.get(URL, verify=False)
#
# data = r.json()
#
# lights = data['lights']
#
# for light in lights:
#     print(light)
#
# # 2 living room
# # 4 bathroom
# # 5 bathroom
# # 6 kitchen
# # 7 closet
# # 8 living room
#
# # get living room lights, 2 and 8
# living_room = ["4", "5"]
#
# # turn lights on and off
# for light in living_room:
#     # print(light)
#     # print('------')
#     URL = f"https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/lights/{light}/state"
#     if lights[light]['state']['on'] == True:
#         resp = requests.put(URL, data='{"on": false}', verify=False)
#     else:
#         resp = requests.put(URL, data='{"on": true}', verify=False)
#     print(resp)
#     print(resp.content)
#
# # <Response [200]>
# # b'[{"success":{"/lights/2/state/on":false}}]'
# # <Response [200]>
# # b'[{"success":{"/lights/8/state/on":false}}]'

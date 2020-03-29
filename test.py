import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check

# get all lights
URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n"

r = requests.get(URL, verify=False)

data = r.json()

lights = data['lights']

for light in lights:
    print(light)

# 2
# 4
# 5
# 6
# 7
# 8

# get living room lights, 2 and 8
living_room = ["2", "8"]

# turn lights on and off
for light in living_room:
    # print(light)
    # print('------')
    URL = f"https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/lights/{light}/state"
    if lights[light]['state']['on'] == True:
        resp = requests.put(URL, data='{"on": false}', verify=False)
        print(resp)
        print(resp.content)
    else:
        resp = requests.put(URL, data='{"on": true}', verify=False)
        print(resp)
        print(resp.content)

# <Response [200]>
# b'[{"success":{"/lights/2/state/on":false}}]'
# <Response [200]>
# b'[{"success":{"/lights/8/state/on":false}}]'

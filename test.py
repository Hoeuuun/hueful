import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check

# get all lights
URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/lights"

r = requests.get(URL, verify=False)

data = r.json()

# print(data)

# get living room lights, 2 and 8
light_a = data['2']
light_b = data['8']

# print(light_a)
# print('-------')
# print(light_b)

# update status 
URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/lights/2/state / put"
resp = requests.put(URL, data={'key': 'value'}, verify=False)

print(resp)
print(resp.content)

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Light():
    def __init__(self, id=None):
        self.id = id
        self.URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n"
        self.r = requests.get(self.URL, verify=False)
        self.data = self.r.json()
        self.lights = self.data['lights']

    def getAllLights(self):
        return [light for light in self.lights]

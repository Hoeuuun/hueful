import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check

class Group():
    def __init__(self, id=None):
        self.id = id

        self.URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/groups"

        self.r = requests.get(self.URL, verify=False)

        self.data = self.r.json()

    def getAllGroups(self):
        '''
        Returns a list of all groups in the system.
        '''

        return [id for id in self.data]

    def getAGroup(self, id):
        '''
        Returns a dictionary of data for a particular group id.
        '''
        if id in self.getAllGroups():
            return self.data[id]
        else:
            return "Not a valid id!"

    def getAGroupRoom(self, room):
        '''
        Returns a dictonary of data for a particular group name.
        '''
        ids = self.getAllGroups()

        for id in ids:
            if self.data[id]['name'] == room:
                return self.data[id]

        print("Cannot find", room, "lights!")
        return None

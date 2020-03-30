import requests
import logging
import json
from typing import Iterable, Dict, Optional
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

class Group():
    def __init__(self, id=None):
        self.id = id
        self.URL = "https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/groups"
        self._refresh_state()

    def _refresh_state(self) -> Dict:
        '''
        Refreshes and returns the state directly from the HUE server
        '''
        try:
            response = requests.get(self.URL, verify=False)
            _logger.info(response.json())
            self.data = response.json()
            self.ids = [id for id in self.data]
            return self.data
        except requests.RequestException as e:
            _logger.error("can't get state from HUE bridge.")
            raise e


    def getAllGroups(self) -> Iterable[str]:
        '''
        Returns a list of all groups in the system
        '''
        return self._refresh_state().keys()

    def getGroup(self, id):
        '''
        Returns a dictionary of data for a particular group id
        '''
        return self._refresh_state()[id]

    def getGroupByRoom(self, room:str) -> Optional[Dict]:
        '''
        Returns a dictonary of data for a particular group name
        '''
        data = self._refresh_state()
        for id in data.keys():
            if data[id]['name'] == room:
                return data[id]

        _logger.info(f"Cannot find {room} lights!")
        return None

    def turnLights(self, id:str, on:bool):
        '''
        Turns the group's lights on and off
        '''
        URL = f"https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n/groups/{id}/action"
        try:
            body = {"on": on}
            resp = requests.put(URL, data=json.dumps(body), verify=False)
            _logger.info(resp.json())
            #  _logger.info(resp.content)
        except requests.RequestException as e:
            _logger.error(f"Couldn't communicate with the server. ({e})")

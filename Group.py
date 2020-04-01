import requests
import logging
import json
from typing import Iterable, Dict, Optional, List
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
        self.state_URL = self.URL + f"/{id}/action"

    def _refresh_state(self) -> Dict:
        '''
        Refreshes and returns the state directly from the HUE server
        '''
        try:
            response = requests.get(self.URL, verify=False)
            # _logger.info(response.json())
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

    def getLights(self):
        '''
        Returns a list of all light IDs in the system.
        All lights in the system are part of the immutable group 0.
        '''
        URL = self.URL + "/lights"
        try:
            resp = requests.get(URL, verify=False)
            _logger.info(resp.json())
            data = resp.json()
            lights = data['lights']
            return lights
        except requests.RequestException as e:
            _logger.error("can't get lights from HUE bridge.")
            raise e

    def getState(self, id:str):
        '''
        Returns a dictionary of the group's current state
        '''
        URL = self.URL + f"/{id}"
        try:
            resp = requests.get(URL, verify=False)
            # _logger.info(resp.json())
            data = resp.json()
            state = data['action']
            return state
        except requests.RequestException as e:
            _logger.error("can't get state from HUE bridge.")
            raise e


    '''
    Methods to modify the group's state:
    '''
    def turnLights(self, id:str, on:bool):
        '''
        Turns the lights on/off
        '''
        try:
            body = {"on": on}
            resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
            _logger.info(resp.json())
            #  _logger.info(resp.content)
        except requests.RequestException as e:
            _logger.error(f"Couldn't communicate with the server. ({e})")

    def setBri(self, id:str, bri:int):
        '''
        Sets the brightness, 0 - 254
        :throws: AssertionError if brightness not within 0-254 in_range
                 RquestException if calling HUE Server did not succeed.
        '''
        assert bri >= 0 and bri <= 254
        body = {"bri": bri}
        resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
        _logger.info(resp.json())

    def setHue(self, id:str, hue:int):
        '''
        Sets the hue, 0 - 65535
        Red = 0, 65535
        Green = 25500
        Blue = 46920
        '''
        assert hue >= 0 and hue <= 65535
        body = {"hue": hue}
        resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
        _logger.info(resp.json())

    def setSat(self, id:str, sat:int):
        '''
        Sets the staturation, 0 - 254
        '''
        assert sat >= 0 and sat <= 254
        body = {"sat": sat}
        resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
        _logger.info(resp.json())

    def setXY(self, id:str, xy:List[float]):
        '''
        Sets the X and Y coordinates of a color in the CIE color space, 0.0 - 1.0
        '''
        assert xy[0] >= 0 and xy[1] <= 1 and xy[1] >= 0 and xy[1] <= 1
        body = {"xy": [xy[0], xy[1]]}
        resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
        _logger.info(resp.json())

    def setCT(self, id:str, ct:int):
        '''
        Sets the Mired Color temperature, 153 (6500K) - 500 (2000K)
        '''
        assert ct >= 153 and ct <= 500
        body = {"ct": ct}
        resp = requests.put(self.state_URL, data=json.dumps(body), verify=False)
        _logger.info(resp.json())

    # TODO: alert, effect, transitiontime, increments for each, scene

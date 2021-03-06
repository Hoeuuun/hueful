import requests
from typing import Iterable, Dict, Optional, List
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from hueful.AbstractLight import AbstractLight

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check


class Group(AbstractLight):
    def __init__(self, id=None, connection: 'Connection' = None):
        super().__init__(id, connection)
        self._url_infix = 'groups'
        self._state = 'action'

    def _refresh_state(self) -> Dict:
        return super()._refresh_state()

    def get_state(self) -> Dict:
        """
        Returns a dictionary of the group's current state
        """
        return self._refresh_state()["action"]

    def _send_state(self, state: Dict):
        super()._send_state(state)

    '''
    Methods to modify the group's state:
    '''

    def turn_on(self, on: bool):
        super().turn_on(on)

    def set_bri(self, bri: int):
        super().set_bri(bri)

    def set_hue(self, hue: int):
        super().set_hue(hue)

    def set_sat(self, sat: int):
        super().set_sat(sat)

    def set_xy(self, xy: List[float]):
        super().set_sat(xy)

    def set_ct(self, ct: int):
        super().set_ct(ct)

    def set_effect(self, effect: bool):
        super().set_effect(effect)

    # TODO: alert, effect, transitiontime, increments for each, scene

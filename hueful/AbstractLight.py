import json
from typing import List, Dict
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  # needed to disable SSL check

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)


# Superclass from which Groups and Lights will inherit
class AbstractLight:
    def __init__(self, id=None, connection: 'Connection' = None):
        self.id = id
        self.connection = connection

    def _send_state(self, state: Dict):
        """
        Sends given state to the HUE hub
        """
        resp = self.connection.put(
            url_suffix=f'/{self._url_infix}/{self.id}/action',
            data=json.dumps(state)
        )
        _logger.info(f'Send state: {state}')

    def _refresh_state(self) -> Dict:
        """
        Refreshes and returns the state directly from the HUE server
        """
        return self.connection.get(f'/{self._url_infix}/{self.id}/')

    def turn_on(self, on: bool):
        """
        Toggles the light(s) on and off
        on = True,
        off = False
        """
        body = {"on": on}
        self._send_state(body)

    def set_bri(self, bri: int):
        """
        Sets the brightness, 0 - 254
        :throws: AssertionError if brightness not within 0-254 in_range
                 RquestException if calling HUE Server did not succeed.
        """
        assert 0 <= bri <= 254
        body = {"bri": bri}
        self._send_state(body)

    def set_hue(self, hue: int):
        """
        Sets the hue, 0 - 65535
        Red = 0, 65535
        Green = 25500
        Blue = 46920
        """
        assert 0 <= hue <= 65535
        body = {"hue": hue}
        self._send_state(body)

    def set_sat(self, sat: int):
        """
        Sets the saturation, 0 - 254
        """
        assert 0 <= sat <= 254
        body = {"sat": sat}
        self._send_state(body)

    def set_xy(self, xy: List[float]):
        """
        Sets the X and Y coordinates of a color in the CIE color space
        Both x and y must be between 0.0 and 1.0
        """
        assert xy[0] >= 0 and 1 >= xy[1] >= 0 and xy[1] <= 1
        body = {"xy": [xy[0], xy[1]]}
        self._send_state(body)

    def set_ct(self, ct: int):
        """
        Sets the Mired Color temperature, 153 (6500K) - 500 (2000K)
        """
        assert 153 <= ct <= 500
        body = {"ct": ct}
        self._send_state(body)

    def set_effect(self, effect: bool):
        """
        Set the "colorloop" effect, which cycles through all hues using
        the current brightness and saturation
        colorloop = True,
        none = False
        """
        if effect:
            body = {"effect": "colorloop"}
        else:
            body = {"effect": "none"}
        self._send_state(body)


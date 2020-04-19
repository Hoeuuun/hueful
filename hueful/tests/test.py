import json
from typing import Dict

from hueful.Connection import Connection
from hueful.Group import Group

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

FAKE_HUB_BASE_ADDRESS = 'http://localhost/api'


class FakeConnection(Connection):
    def __init__(self, *args, **kwargs):
        super().__init__(server_address=FAKE_HUB_BASE_ADDRESS)
        self.get_requests = []
        self.put_requests = []

    def get(self, url_suffix, data=None) -> Dict:
        self.get_requests.append((url_suffix, data))

    def put(self, url_suffix, data=None):
        self.put_requests.append((url_suffix, data))


@pytest.fixture
def hue_connection():
    return FakeConnection()


class TestHuey:
    def test_brightness(self, hue_connection):
        # Given: A connection and a single group
        g = Group(id='1', connection=hue_connection)
        # When: We set brightness on the group
        g.set_bri(200)
        # Then: We should have made single put request
        assert len(hue_connection.put_requests) == 1
        url, data = hue_connection.put_requests[0]
        assert url == f'/groups/1/action'
        assert data == json.dumps({'bri': 200})

    def test_turn_lights(self, hue_connection):
        # Given: A connection and a single group
        g = Group(id='1', connection=hue_connection)
        # When: We turn_lights on the group
        g.turn_lights(True)
        # Then: We should've made a single put request
        assert len(hue_connection.put_requests) == 1
        url, data = hue_connection.put_requests[0]
        assert url == f'/groups/1/action'
        assert data == json.dumps({'on': True})

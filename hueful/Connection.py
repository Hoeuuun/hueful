from typing import Dict, Iterable

import requests

from hueful.Group import Group


class Connection:
    def __init__(
            self,
            server_address='https://192.168.1.51/api/is83Oh2YZuNuD4Nqoks0nLmfQw32UaGdvn5hQX9n',
            verify=True,
    ):
        self.server_address = server_address
        self.verify = verify

    def _make_url(self, url_suffix: str) -> str:
        return f'{self.server_address}{url_suffix}'

    def get(self, url_suffix: str, data: str = None) -> Dict:
        full_url = self._make_url(url_suffix)
        response = requests.get(full_url, data=data, verify=self.verify)
        json_data = response.json()
        return json_data

    def put(self, url_suffix: str, data: str = None):
        full_url = self._make_url(url_suffix)
        response = requests.post(full_url, data=data, verify=self.verify)
        return response.json()

    def get_all_groups(self) -> Dict[str, Group]:
        """
        Returns a list of all groups in the system
        """
        group_json = self.get('/groups')
        return {
            x: Group(id=x, connection=self)
            for x in group_json.keys()}


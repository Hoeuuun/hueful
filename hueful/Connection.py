from typing import Dict

import requests


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
        return response.json()

    def put(self, url_suffix: str, data: str = None):
        full_url = self._make_url(url_suffix)
        response = requests.post(full_url, data=data, verify=self.verify)
        return response.json()

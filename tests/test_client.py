# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from georapid.client import GeoRapidClient
from georapid.factory import EnvironmentClientFactory
from geourban.services import simulations
import unittest

# Import errors during debug session: https://github.com/microsoft/vscode-python/issues/21648#issuecomment-1638365589
# Add the following in your user or workspace settings
"""
"python.experiments.optOutFrom": [
        "pythonTestAdapter"
    ]
"""



class TestConnect(unittest.TestCase):

    def setUp(self) -> None:
        self._latitudes = [51.83864, 50.73438]
        self._longitudes = [12.24555, 7.09549]

    def test_create(self):
        host = 'geourban.p.rapidapi.com'
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        self.assertIsNotNone(client, "Client must be initialized!")

    def test_list_simulations(self):
        host = 'geourban.p.rapidapi.com'
        client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)
        urban_simulations = simulations(client)
        self.assertIsNotNone(urban_simulations, "List of urban simulations must be initialized!")
        self.assertGreater(len(urban_simulations), 0, "List of urban simulations must not be emtpy!")
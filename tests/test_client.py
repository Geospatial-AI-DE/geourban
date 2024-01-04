# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from georapid.client import GeoRapidClient
from georapid.factory import EnvironmentClientFactory
import unittest



class TestConnect(unittest.TestCase):

    def setUp(self) -> None:
        self._latitudes = [51.83864, 50.73438]
        self._longitudes = [12.24555, 7.09549]

    def test_create(self):
        client: GeoRapidClient = EnvironmentClientFactory.create_client()
        self.assertIsNotNone(client, "Client must be initialized!")
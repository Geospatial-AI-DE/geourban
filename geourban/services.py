# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from georapid.client import GeoRapidClient
import requests



def simulations(client: GeoRapidClient):
    """
    Returns all the available simulations using the urban region and the simulation date.
    The client instance must refer to a valid geourban services host like 'geourban.p.rapidapi.com'.
    """
    endpoint = '{0}/simulations'.format(client.url)
    params = {
        'format': str(format)
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()
# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from datetime import date, datetime
from georapid.client import GeoRapidClient
from geourban.formats import OutFormat
from geourban.types import GridType, VehicleType
import requests



def aggregate(client: GeoRapidClient, region_code: str, simulation_datetime: datetime, vehicle_type: VehicleType, grid_type: GridType, out_format: OutFormat=OutFormat.GEOJSON):
    """
    Returns a spatially enabled traffic grid representing aggregated simulated movements of pedestrians, bikes and cars.
    """
    endpoint = '{0}/aggregate'.format(client.url)
    params = {
        'region': region_code,
        'time': simulation_datetime.isoformat(),
        'vehicle': str(vehicle_type),
        'grid': str(grid_type),
        'format': str(out_format)
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()

def simulations(client: GeoRapidClient):
    """
    Returns all the available simulations using the urban region and the simulation date.
    The client instance must refer to a valid geourban services host like 'geourban.p.rapidapi.com'.
    """
    endpoint = '{0}/simulations'.format(client.url)
    response = requests.request('GET', endpoint, headers=client.auth_headers)
    response.raise_for_status()

    return response.json()

def top(client: GeoRapidClient, region_code: str, simulation_date: date, vehicle_type: VehicleType, grid_type: GridType, limit: int=10, out_format: OutFormat=OutFormat.GEOJSON):
    """
    Returns the top most accumulated traffic grid cells for an urban region.
    """
    endpoint = '{0}/top'.format(client.url)
    params = {
        'region': region_code,
        'date': simulation_date.strftime('%Y-%m-%d'),
        'vehicle': str(vehicle_type),
        'grid': str(grid_type),
        'limit': limit,
        'format': str(out_format)
    }
    response = requests.request('GET', endpoint, headers=client.auth_headers, params=params)
    response.raise_for_status()

    return response.json()
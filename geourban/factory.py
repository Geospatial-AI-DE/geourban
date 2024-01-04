# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

import os
from . client import GeoRapidClient



class EnvironmentClientFactory(object):
    """
    Represents a factory creating client instances using the system environment.
    The environment must offer various variables for authenticating against the web service endpoints.
    """

    @staticmethod
    def create_client():
        """
        Creates a new client using 'x_rapidapi_url', 'x_rapidapi_host' and 'x_rapidapi_key' environment variables.
        Raises a ValueError when these variables are not defined!
        """
        if not 'x_rapidapi_url' in os.environ:
            raise ValueError("'x_rapidapi_url' is not defined in the current environment!")
        if not 'x_rapidapi_host' in os.environ:
            raise ValueError("'x_rapidapi_host' is not defined in the current environment!")
        if not 'x_rapidapi_key' in os.environ:
            raise ValueError("'x_rapidapi_key' is not defined in the current environment!")

        url = os.environ['x_rapidapi_url']
        host = os.environ['x_rapidapi_host']
        key = os.environ['x_rapidapi_key']
        auth_headers = {
            'x-rapidapi-host': host,
            'x-rapidapi-key': key
        }

        return GeoRapidClient(url, auth_headers)

    @staticmethod
    def create_client_with_host(host):
        """
        Creates a new client using 'x_rapidapi_key' enironment variable.
        Raises a ValueError when this variable is not defined!
        """
        if not 'x_rapidapi_key' in os.environ:
            raise ValueError("'x_rapidapi_key' is not defined in the current environment!")

        key = os.environ['x_rapidapi_key']
        auth_headers = {
            'x-rapidapi-host': host,
            'x-rapidapi-key': key
        }

        url = "https://%s" % host
        return GeoRapidClient(url, auth_headers)
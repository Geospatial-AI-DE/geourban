# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

class GeoRapidClient(object):
    """
    Represents a client accessing the geospatial knowledge API services being hosted at Rapid API.
    """

    def __init__(self, url, auth_headers) -> None:
        """
        Initializes this instance using an url and an authorization header dictionary.
        The dictionary must contain 'x-rapidapi-host' and 'x-rapidapi-host' as keys.
        """
        self._url = url
        if not 'x-rapidapi-host' in auth_headers:
            raise ValueError("'x-rapidapi-host' must be specified in the authorization header!")
        if not 'x-rapidapi-key' in auth_headers:
            raise ValueError("'x-rapidapi-key' must be specified in the authorization header!")

        self._auth_headers = auth_headers

    @property
    def auth_headers(self):
        """Returns the authorization header dictionary."""
        return self._auth_headers

    @property
    def url(self):
        """Returns the endpoint url."""
        return self._url

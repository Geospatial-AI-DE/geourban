Usage
=====

.. _installation:

Installation
------------

To use geourban, first install it using pip:

.. code-block:: console

   (.venv) $ pip install geourban

Creating clients
----------------
To authorize against the endpoints being hosted on Rapid API you need to use your own Rapid API key.
This geourban module uses client instances from the georapid module.

The ``host`` parameter must target the specific host like ``"geourban.p.rapidapi.com"``.
Furthermore, the factory directly access ``os.environ['x_rapidapi_key']`` and uses the specified API key as a header parameter.
Otherwise, :py:func:`georapid.factory.EnvironmentClientFactory.create_client_with_host` will raise a :exc:`ValueError`.

For example:

>>> from georapid.client import GeoRapidClient
>>> from georapid.factory import EnvironmentClientFactory
>>> host = 'geourban.p.rapidapi.com'
>>> client: GeoRapidClient = EnvironmentClientFactory.create_client_with_host(host)

For more details take a closer look at `Creating clients <https://georapid.readthedocs.io/en/latest/usage.html#creating-clients>`__.

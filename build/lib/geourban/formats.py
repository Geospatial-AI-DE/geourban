# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from enum import Enum, unique



@unique
class OutFormat(Enum):
    """Represents the supported output formats."""
    ESRI=0
    GEOJSON=1
    JSON=2

    def __str__(self) -> str:
        if 0 == self.value:
            return 'esri'
        elif 1 == self.value:
            return 'geojson'
        elif 2 == self.value:
            return 'json'
        
        return self.name
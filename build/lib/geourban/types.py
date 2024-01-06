# author: Jan Tschada
# SPDX-License-Identifer: Apache-2.0

from enum import Enum, unique



@unique
class GridType(Enum):
    """
    Represents the supported grid types.
    agent: The number of unique agents is calculated.
    speed: The speed average of every agent is calculated.
    emissions: The sum of carbon dioxide emissions of every agent is calculated. This makes only sense for vehicle being cars!
    """
    AGENT=0
    SPEED=1
    EMISSIONS=2

    def __str__(self) -> str:
        if 0 == self.value:
            return 'agent'
        elif 1 == self.value:
            return 'speed'
        elif 2 == self.value:
            return 'emissions'
        
        return self.name
    
@unique
class VehicleType(Enum):
    """
    Represents the supported vehicle types.
    Car, Bike and Pedestrian are possible vehicle types.
    """
    CAR=0
    BIKE=1
    PEDESTRIAN=2

    def __str__(self) -> str:
        if 0 == self.value:
            return 'Car'
        elif 1 == self.value:
            return 'Bike'
        elif 2 == self.value:
            return 'Pedestrian'
        
        return self.name
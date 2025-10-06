from .test_equipment_template import TestEquipmentTemplate

from .Agilent34405A import DMM34405A
from .AgilentDSO5054A import DSO5054A
from .AgilentE3648A import E3648A
from .KoradKA3005P import KA005P
from .KuaiquKDL8410 import KDL8410
from .UniTUTG962E import UTG962E


from .equipment_manager import EquipmentManager  # We'll create this

__all__ = [
    'TestEquipmentTemplate',
    'Agilent34405A',
    'AgilentDSO5054A',
    'AgilentE3648A',
    'KoradKA3005P',
    'KuaiquKDL8410',
    'UniTUTG962E'
]

__version__ = '1.0.0'
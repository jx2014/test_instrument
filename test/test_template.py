import sys
from logger import get_logger

class TestTemplate:
     def __init__(self, **kwargs):
         self.eq = kwargs.get("equipment_manager", None)
         if self.eq is None:
             sys.exit("No equipment found, exit program.")
         if not hasattr(self, 'required_equipment'):
            self.required_equipment = []
         if not hasattr(self, 'test_name'):
            self.test_name = "UnknownTestName"
         self._connected_equipment = []
         self.logger = get_logger(f"test.{self.test_name}")
         self.setup()

     def setup(self):
         """Connect to required equipment"""
         print(f"Setting up {self.__class__.__name__}...")

         # Check if required equipment exists
         for eq_name in self.required_equipment:
             if eq_name not in self.eq.equipment:
                 raise ValueError(f"Required equipment '{eq_name}' not available")

         # Connect to required equipment
         for eq_name in self.required_equipment:
             if self.eq.equipment[eq_name].connect():
                 self._connected_equipment.append(eq_name)
                 print(f" * Connected to {eq_name}")
             else:
                 raise ConnectionError(f"Failed to connect to {eq_name}")
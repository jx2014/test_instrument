import pyvisa
import json
import os
from abc import ABC, abstractmethod


class TestEquipmentTemplate(ABC):
    def __init__(self, equipment_config):
        self.config = equipment_config
        self.equipment_name = equipment_config.get('equipment_name', 'unknown')
        self.equipment_type = equipment_config.get('equipment_type', 'unknown')
        self.equipment_model = equipment_config.get('equipment_model', 'unknown')
        self.address = equipment_config.get('equipment_address', '')
        self.connection_type = equipment_config.get('connection_type', 'unknown')
        self.resource_manager = None
        self.instrument = None
        self.is_connected = False

    def connect(self):
        """Establish connection to the instrument"""
        try:
            self.resource_manager = pyvisa.ResourceManager()
            self.instrument = self.resource_manager.open_resource(self.address)

            # Set timeout to 5 seconds
            self.instrument.timeout = 5000

            # Test connection
            idn = self.get_idn()
            print(f"Connected to {self.equipment_name}: {idn}")
            self.is_connected = True
            return True

        except Exception as e:
            print(f"Failed to connect to {self.equipment_name} at {self.address}: {e}")
            self.is_connected = False
            return False

    def disconnect(self):
        """Close connection to the instrument"""
        if self.instrument:
            self.instrument.close()
            self.is_connected = False
            print(f"Disconnected from {self.equipment_name}")

    def write(self, command):
        """Send command to instrument"""
        if self.is_connected and self.instrument:
            self.instrument.write(command)
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    def read(self):
        """Read data from instrument"""
        if self.is_connected and self.instrument:
            return self.instrument.read()
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    def query(self, command):
        """Send command and read response"""
        if self.is_connected and self.instrument:
            return self.instrument.query(command)
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    @abstractmethod
    def get_idn(self):
        """Get instrument identification - to be implemented by child classes"""
        pass

    def reset(self):
        """Reset instrument to default settings"""
        self.write("*RST")
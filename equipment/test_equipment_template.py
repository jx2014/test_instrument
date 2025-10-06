import pyvisa
import json
import os

class TestEquipmentTemplate():
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
        try:
            self.resource_manager = pyvisa.ResourceManager()
            self.instrument = self.resource_manager.open_resource(self.address)
            self.instrument.timeout = 5000
            idn = self.get_idn()
            print(f"Connected to {self.equipment_name}: {idn}")
            self.is_connected = True
            return True

        except Exception as e:
            print(f"Failed to connect to {self.equipment_name} at {self.address}: {e}")
            self.is_connected = False
            return False

    def disconnect(self):
        if self.instrument:
            self.instrument.close()
            self.is_connected = False
            print(f"Disconnected from {self.equipment_name}")

    def write(self, command):
        if self.is_connected and self.instrument:
            self.instrument.write(command)
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    def read(self):
        if self.is_connected and self.instrument:
            return self.instrument.read()
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    def query(self, command):
        if self.is_connected and self.instrument:
            return self.instrument.query(command)
        else:
            raise ConnectionError(f"Not connected to {self.equipment_name}")

    def get_idn(self):
        pass

    def reset(self):
        self.write("*RST")
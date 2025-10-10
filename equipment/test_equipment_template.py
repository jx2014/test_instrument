import pyvisa
import time
import json
import os
from logger import get_logger
from pyvisa.constants import VI_WRITE_BUF_DISCARD, VI_READ_BUF_DISCARD

class TestEquipmentTemplate():
    def __init__(self, equipment_config, **kwargs):
        self.config = equipment_config
        self.special_config = kwargs.get("special_config", {})
        self.equipment_name = equipment_config.get('equipment_name', 'unknown')
        self.equipment_type = equipment_config.get('equipment_type', 'unknown')
        self.equipment_model = equipment_config.get('equipment_model', 'unknown')
        self.address = equipment_config.get('equipment_address', '')
        self.connection_type = equipment_config.get('connection_type', 'unknown')
        self.optional = equipment_config.get('optional', False)
        self.resource_manager = None
        self.instrument = None
        self.is_connected = False
        self.logger = get_logger(f"equipmenbt.{self.equipment_name}")
        self.logger.debug(f"Initialized {self.equipment_model}")

    def connect(self):
        try:
            self.logger.info(f"Connecting to {self.address} via {self.connection_type}")
            self.resource_manager = pyvisa.ResourceManager()
            self.instrument = self.resource_manager.open_resource(self.address)
            self.instrument.timeout = self.special_config.get("timeout", 5000)
            self.instrument.baud_rate = self.special_config.get("baud_rate", 9600)
            self.instrument.write_termination = self.special_config.get("write_termination", "\r\n")
            self.instrument.read_termination = self.special_config.get("read_termination", None)
            idn = self.get_idn()
            print(f"Connected to {self.equipment_name}: {idn}")
            self.is_connected = True
            self.logger.info("Connection successful")
            return True

        except Exception as e:
            self.logger.error(f"Failed to connect to {self.equipment_name} at {self.address}: {e}")
            self.is_connected = False
            return False

    def disconnect(self):
        if self.instrument:
            self.instrument.close()
            self.is_connected = False
            self.logger.info(f"Disconnected from {self.equipment_name}")

    def write(self, command):
        if self.is_connected and self.instrument:
            if 'serialinstrument' in repr(self.instrument).lower() and self.instrument.bytes_in_buffer != 0:
                self.instrument.flush(VI_READ_BUF_DISCARD | VI_WRITE_BUF_DISCARD)
            self.instrument.write(command)
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. Write command \"{command}\" ignored.")

    def read(self):
        if self.is_connected and self.instrument:
            return self.instrument.read()
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. read command ignored.")

    def query(self, command):
        if self.is_connected and self.instrument:
            if 'serialinstrument' in repr(self.instrument).lower() and self.instrument.bytes_in_buffer != 0:
                self.instrument.flush(VI_READ_BUF_DISCARD | VI_WRITE_BUF_DISCARD)
            return self.instrument.query(command)
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. query command ignored.")

    def query_raw(self, command):
        if self.is_connected and self.instrument:
            self.write_raw(command)
            return self.read_raw()
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. query_raw command ignored.")

    def write_raw(self, command):
        if self.is_connected and self.instrument:
            if 'serialinstrument' in repr(self.instrument).lower() and self.instrument.bytes_in_buffer != 0:
                self.instrument.flush(VI_READ_BUF_DISCARD | VI_WRITE_BUF_DISCARD)
            self.instrument.write_raw(command.encode())
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. Write command \"{command}\" ignored.")

    def read_raw(self):
        if self.is_connected and self.instrument:
            bytes_to_read = -1
            retries = 100
            while bytes_to_read != self.instrument.bytes_in_buffer and retries > 0:
                retries -= 1
                bytes_to_read = self.instrument.bytes_in_buffer
                time.sleep(0.05)
            return self.instrument.read_bytes(bytes_to_read).decode()
        elif not self.optional:
            raise ConnectionError(f"Not connected to {self.equipment_name}")
        else:
            self.logger.warn(f"Equipment is not connected. read_raw command ignored.")

    def get_idn(self):
        return self.instrument.query("*idn?")

    def reset(self):
        self.write("*RST")
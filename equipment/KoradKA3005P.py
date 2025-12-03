import time
from .dc_power_supply_template import DCPowerSupplyTemplate


class KA3005P(DCPowerSupplyTemplate):
    def __init__(self, general_equipment_config):
        equipment_specific_config = {"baud_rate": 9600,
                                     "write_termination": "",
                                     "read_termination": "",
                                     "timeout": 1000
                                     }
        super().__init__(general_equipment_config, special_config=equipment_specific_config)
        self.name = "Korad KA3005P"

    def get_idn(self):
        self.instrument.write_raw(b"*IDN?")
        response = self.instrument.read_bytes(self.instrument.bytes_in_buffer)
        return response.rstrip(b'\x00').decode()

    def read(self):
        response = self.read_raw()
        return response.rstrip('\x00')

    def write(self, cmd):
        self.write_raw(cmd)
        time.sleep(1)

    def query(self, command):
        response = self.query_raw(command)
        return response.rstrip('\x00')

    def get_voltage_limit(self, channel=None):
        return float(self.query(f"VSET1?"))

    def get_current_limit(self, channel=None):
        return float(self.query(f"ISET1?"))

    def get_voltage(self):
        # Korad specific command
        return float(self.query("VOUT1?"))

    def get_current(self):
        # Korad specific command
        return float(self.query("IOUT1?"))

    def set_voltage(self, voltage):
        self.write(f"VSET1:{voltage}")

    def set_current(self, current):
        self.write(f"ISET1:{current}")

    def turn_on(self):
        self.write("OUT1")

    def turn_off(self):
        self.write("OUT0")

    def set_output(self, voltage, current):
        self.set_voltage(voltage)
        self.set_current(current)

    def tear_down(self):
        self.turn_off()

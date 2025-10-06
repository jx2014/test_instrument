from .dc_power_supply_template import DCPowerSupplyTemplate


class E3648A(DCPowerSupplyTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Agilent E3648A"

    def get_voltage(self):
        return float(self.query(f"MEAS:VOLT? CH{self.channel}"))

    def get_current(self):
        return float(self.query(f"MEAS:CURR? CH{self.channel}"))

    def set_voltage(self, voltage):
        self.write(f"VOLT {voltage}, (@{self.channel})")

    def set_current(self, current):
        self.write(f"CURR {current}, (@{self.channel})")

    def turn_on(self):
        self.write(f"OUTP ON, (@{self.channel})")

    def turn_off(self):
        self.write(f"OUTP OFF, (@{self.channel})")
from .dc_power_supply_template import DCPowerSupplyTemplate


class KA3005P(DCPowerSupplyTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Korad KA3005P"

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
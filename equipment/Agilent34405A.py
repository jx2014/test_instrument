from .multimeter_template import MultiMeterTemplate


class DMM34405A(MultiMeterTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Agilent 34405A"

    def get_voltage(self):
        return float(self.query(f"MEAS:VOLT? CH{self.channel}"))

    def tear_down(self):
        pass
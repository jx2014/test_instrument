from .oscilloscope_template import OscilloscopeTemplate

class DSO5054A(OscilloscopeTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Agilent DSO5054A"
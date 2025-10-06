from test_equipment_template import TestEquipmentTemplate


class SignalGeneratorTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)

    def get_frequency(self, ch):
        raise NotImplementedError("get_frequency must be implemented in child class")

    def set_frequency(self, ch, value):
        raise NotImplementedError("set_frequency must be implemented in child class")

    def get_amplitude(self, ch):
        raise NotImplementedError("get_amplitude must be implemented in child class")

    def set_amplitude(self, ch, amplitude):
        raise NotImplementedError("set_amplitude must be implemented in child class")

    def get_offset(self, ch):
        raise NotImplementedError("get_offset must be implemented in child class")

    def set_offset(self, ch, offset):
        raise NotImplementedError("set_offset must be implemented in child class")

    def get_phase(self, ch):
        raise NotImplementedError("get_phase must be implemented in child class")

    def set_phase(self, ch, phase):
        raise NotImplementedError("set_phase must be implemented in child class")

    def get_load(self, ch):
        raise NotImplementedError("get_load must be implemented in child class")

    def set_load_high_z(self, ch):
        raise NotImplementedError("set_load_high_z must be implemented in child class")

    def set_load_50ohm(self, ch):
        raise NotImplementedError("set_load_50ohm must be implemented in child class")

    def set_load_75ohm(self, ch):
        raise NotImplementedError("set_load_75ohm must be implemented in child class")

    def get_waveform_type(self, ch):
        raise NotImplementedError("get_waveform_type must be implemented in child class")

    def set_waveform_sine(self, ch):
        raise NotImplementedError("set_waveform_sine must be implemented in child class")

    def set_waveform_square(self, ch):
        raise NotImplementedError("set_waveform_square must be implemented in child class")

    def set_waveform_ramp(self, ch):
        raise NotImplementedError("set_waveform_ramp must be implemented in child class")

    def set_cw(self, ch):
        raise NotImplementedError("set_cw must be implemented in child class")


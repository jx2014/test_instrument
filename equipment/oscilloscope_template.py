from test_equipment_template import TestEquipmentTemplate


class OscilloscopeTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)

    def get_vertical_scale(self, ch):
        raise NotImplementedError("get_vertical_scale must be implemented in child class")

    def set_vertical_scale(self, ch):
        raise NotImplementedError("set_vertical_scale must be implemented in child class")

    def get_horizontal_scale(self):
        raise NotImplementedError("get_horizontal_scale must be implemented in child class")

    def set_horizontal_scale(self):
        raise NotImplementedError("set_horizontal_scale must be implemented in child class")

    def get_trigger_channel(self):
        raise NotImplementedError("get_trigger_channel must be implemented in child class")

    def set_trigger_channel(self, ch):
        raise NotImplementedError("set_trigger_channel must be implemented in child class")

    def get_trigger_level(self):
        raise NotImplementedError("get_trigger_level must be implemented in child class")

    def set_trigger_level(self, level):
        raise NotImplementedError("set_trigger_level must be implemented in child class")

    def get_acquire_mode(self):
        raise NotImplementedError("get_acquire_mode must be implemented in child class")

    def set_acquire_mode(self, mode):
        raise NotImplementedError("set_acquire_mode must be implemented in child class")

    def set_channel_bandwidth(self, bw):
        raise NotImplementedError("set_channel_bandwidth must be implemented in child class")

    def get_frequency(self, ch):
        raise NotImplementedError("get_frequency must be implemented in child class")

    def get_vpp(self, ch):
        raise NotImplementedError("get_vpp must be implemented in child class")

    def get_vrms(self, ch):
        raise NotImplementedError("get_vrms must be implemented in child class")

    def get_screenshot(self):
        raise NotImplementedError("get_screenshot must be implemented in child class")


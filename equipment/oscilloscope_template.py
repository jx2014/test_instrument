from .test_equipment_template import TestEquipmentTemplate


class OscilloscopeTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)

    def get_probe_offset(self, ch):
        raise NotImplementedError("get_probe_offset must be implemented in child class")

    def set_probe_offset(self, ch, offset):
        raise NotImplementedError("set_probe_offset must be implemented in child class")

    def get_probe_attenuation(self, ch):
        raise NotImplementedError("get_probe_attenuation must be implemented in child class")

    def set_probe_attenuation(self, ch, atten):
        raise NotImplementedError("set_probe_attenuation must be implemented in child class")

    def get_vertical_scale(self, ch):
        raise NotImplementedError("get_vertical_scale must be implemented in child class")

    def set_vertical_scale(self, ch):
        raise NotImplementedError("set_vertical_scale must be implemented in child class")

    def get_vertical_range(self, ch):
        raise NotImplementedError("get_vertical_range must be implemented in child class")

    def set_vertical_range(self, ch):
        raise NotImplementedError("set_vertical_range must be implemented in child class")

    def get_horizontal_scale(self):
        raise NotImplementedError("get_horizontal_scale must be implemented in child class")

    def set_horizontal_scale(self):
        raise NotImplementedError("set_horizontal_scale must be implemented in child class")

    def get_horizontal_range(self):
        raise NotImplementedError("get_horizontal_range must be implemented in child class")

    def set_horizontal_range(self, time_range):
        raise NotImplementedError("set_horizontal_range must be implemented in child class")

    def get_trigger_source(self):
        raise NotImplementedError("get_trigger_source must be implemented in child class")

    def set_trigger_source(self, ch):
        raise NotImplementedError("set_trigger_source must be implemented in child class")

    def get_trigger_slope(self):
        raise NotImplementedError("get_trigger_slope must be implemented in child class")

    def set_trigger_slope(self, slope):
        raise NotImplementedError("set_trigger_slope must be implemented in child class")

    def get_trigger_coupling(self):
        raise NotImplementedError("get_trigger_coupling must be implemented in child class")

    def set_trigger_coupling(self, coupling):
        raise NotImplementedError("set_trigger_coupling must be implemented in child class")

    def get_trigger_level(self):
        raise NotImplementedError("get_trigger_level must be implemented in child class")

    def set_trigger_level(self, level):
        raise NotImplementedError("set_trigger_level must be implemented in child class")

    def get_acquire_mode(self):
        raise NotImplementedError("get_acquire_mode must be implemented in child class")

    def set_acquire_mode(self, mode):
        raise NotImplementedError("set_acquire_mode must be implemented in child class")

    def turn_channel_on(self, ch):
        raise NotImplementedError("turn_channel_on must be implemented in child class")

    def turn_channel_off(self, ch):
        raise NotImplementedError("turn_channel_off must be implemented in child class")

    def get_channel_impedance(self, ch):
        raise NotImplementedError("get_channel_impedance must be implemented in child class")

    def set_channel_impedance(self, ch, z):
        raise NotImplementedError("set_channel_impedance must be implemented in child class")

    def set_channel_bandwidth(self, bw):
        raise NotImplementedError("set_channel_bandwidth must be implemented in child class")

    def get_frequency(self, ch):
        raise NotImplementedError("get_frequency must be implemented in child class")

    def get_vpp(self, ch):
        raise NotImplementedError("get_vpp must be implemented in child class")

    def get_vrms(self, ch):
        raise NotImplementedError("get_vrms must be implemented in child class")

    def get_vaverage(self, ch):
        raise NotImplementedError("get_vaverage must be implemented in child class")

    def get_screenshot(self):
        raise NotImplementedError("get_screenshot must be implemented in child class")

    def get_time_base_mode(self):
        raise NotImplementedError("get_time_base_mode must be implemented in child class")

    def set_time_base_normal_mode(self):
        raise NotImplementedError("set_time_base_normal_mode must be implemented in child class")

    def set_time_base_window_mode(self):
        raise NotImplementedError("set_time_base_window_mode must be implemented in child class")

    def set_time_base_roll_mode(self):
        raise NotImplementedError("set_time_base_roll_mode must be implemented in child class")

    def set_time_base_xy_mode(self):
        raise NotImplementedError("set_time_base_xy_mode must be implemented in child class")

    def get_time_base_position(self):
        raise NotImplementedError("get_time_base_position must be implemented in child class")

    def set_time_base_position(self, pos=0):
        raise NotImplementedError("set_time_base_position must be implemented in child class")

    def get_time_base_reference(self):
        raise NotImplementedError("get_time_base_reference must be implemented in child class")

    def set_time_base_reference_left(self):
        raise NotImplementedError("set_time_base_reference_left must be implemented in child class")

    def set_time_base_reference_center(self):
        raise NotImplementedError("set_time_base_reference_center must be implemented in child class")

    def set_time_base_reference_right(self):
        raise NotImplementedError("set_time_base_reference_right must be implemented in child class")


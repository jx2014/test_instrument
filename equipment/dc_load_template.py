from .test_equipment_template import TestEquipmentTemplate


class DCLoadTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)

    def get_mode(self):
        raise NotImplementedError("get_mode must be implemented in child class")

    def get_slew_rate(self):
        raise NotImplementedError("get_slew_rate must be implemented in child class")

    def get_voltage(self):
        raise NotImplementedError("get_voltage must be implemented in child class")

    def get_current(self):
        raise NotImplementedError("get_current must be implemented in child class")

    def set_mode_cc(self):
        raise NotImplementedError("set_mode_cc must be implemented in child class")

    def set_mode_cr(self):
        raise NotImplementedError("set_mode_cr must be implemented in child class")

    def set_mode_cw(self):
        raise NotImplementedError("set_mode_cw must be implemented in child class")

    def set_mode_cv(self):
        raise NotImplementedError("set_mode_cv must be implemented in child class")

    def set_slew_rate(self):
        raise NotImplementedError("set_slew_rate must be implemented in child class")

    def set_voltage(self, voltage):
        raise NotImplementedError("set_voltage must be implemented in child class")

    def set_current(self, current):
        raise NotImplementedError("set_current must be implemented in child class")

    def turn_on(self):
        raise NotImplementedError("turn_on must be implemented in child class")

    def turn_off(self):
        raise NotImplementedError("turn_off must be implemented in child class")

    def get_output_status(self):
        """Get output status (on/off)"""
        try:
            return self.query("OUTP?")
        except:
            return "Unknown"
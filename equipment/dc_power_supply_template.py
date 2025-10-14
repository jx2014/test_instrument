from .test_equipment_template import TestEquipmentTemplate


class DCPowerSupplyTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config, **kwargs):
        super().__init__(equipment_config, **kwargs)
        self.default_channel = equipment_config.get('channel', 1)

    def get_voltage_limit(self):
        raise NotImplementedError("get_voltage_limit must be implemented in child class")

    def get_current_limit(self):
        raise NotImplementedError("get_current_limit must be implemented in child class")

    def get_voltage(self):
        """Get output voltage - override in specific models"""
        raise NotImplementedError("get_voltage must be implemented in child class")

    def get_current(self):
        """Get output current - override in specific models"""
        raise NotImplementedError("get_current must be implemented in child class")

    def set_voltage_limit(self):
        raise NotImplementedError("set_voltage_limit must be implemented in child class")

    def set_current_limit(self):
        raise NotImplementedError("set_current_limit must be implemented in child class")

    def set_voltage(self, voltage):
        """Set output voltage - override in specific models"""
        raise NotImplementedError("set_voltage must be implemented in child class")

    def set_current(self, current):
        """Set output current - override in specific models"""
        raise NotImplementedError("set_current must be implemented in child class")

    def turn_on(self):
        """Turn output on - override in specific models"""
        raise NotImplementedError("turn_on must be implemented in child class")

    def turn_off(self):
        """Turn output off - override in specific models"""
        raise NotImplementedError("turn_off must be implemented in child class")

    def set_output(self, voltage, current):
        raise NotImplementedError("set_output must be implemented in child class")

    def get_system_error(self):
        raise NotImplementedError("get_system_error must be implemented in child class")
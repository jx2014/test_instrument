from .test_equipment_template import TestEquipmentTemplate


class MultiMeterTemplate(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)

    def get_voltage(self):
        raise NotImplementedError("get_voltage must be implemented in child class")

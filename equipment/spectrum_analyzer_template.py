from test_equipment_template import TestEquipmentTemplate


class SpectrumAnalyer(TestEquipmentTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.channel = equipment_config.get('channel', 1)
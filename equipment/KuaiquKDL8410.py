from .dc_load_template import DCLoadTemplate


class KDL8410(DCLoadTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Kuaiqu KDL8410"


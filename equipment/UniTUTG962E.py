from .signal_generator_template import SignalGeneratorTemplate


class UTG962E(SignalGeneratorTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Uni-T UTG962E"
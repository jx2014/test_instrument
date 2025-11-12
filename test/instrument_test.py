"""
    This script is used to test instrument drivers.
"""
from .test_template import TestTemplate

class InstrumentTest(TestTemplate):
    def __init__(self, **kwargs):
        self.test_name = "Instrument Test"
        super().__init__(**kwargs)
        self.eq.connect_all()
        self.eq.list_equipment()

    def run_test(self):
        pass

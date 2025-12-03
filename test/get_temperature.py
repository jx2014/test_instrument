"""
    Use Fluke 289's optical port to read temperature of a device.
"""
import time
from .test_template import TestTemplate
import numpy as np

class GetTemperature(TestTemplate):
    def __init__(self, **kwargs):
        self.required_equipment = ['dc_supply2',
                                   'dmm2']
        self.test_name = "Get_Temperature"
        super().__init__(**kwargs)
        self.dc_supply = self.eq.equipment['dc_supply2']
        self.dmm = self.eq.equipment['dmm2']


    def initialization(self):
        pass

    def run_test(self):
        # run for 2 minutes
        t0 = time.time()
        print("Time,", "Temperature,", "Voltage,", "Current")
        for s in np.arange(-10, 121, 0.5):
            t = time.time() - t0
            temperature = self.dmm.get_reading()
            voltage = self.dc_supply.get_voltage()
            current = self.dc_supply.get_current()
            time.sleep(0.5 - t if 0.5 > t else 0)
            if s >= 0 < 0.5:
                self.dc_supply.turn_on()
            print("%0.1f, %0.1f, %.2f, %.3f" % (s, temperature, voltage, current))






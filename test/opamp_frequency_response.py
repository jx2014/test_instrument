"""
    A test script to frequency sweep an op-amp to produce a Bode plot.
    This test requires two power supply to provide both positive and negative supply voltage, a frequency generator,
    an oscilloscope with two channels to read the input signal frequency and level and output frequency and level.
    The data is recorded as frequency, input signal level, input signal frequency, output signal level,
    output phase shift, gain (linear), gain (dB).
"""

from .test_template import TestTemplate
import sys

class OpampFrequencyResponse(TestTemplate):
    def __init__(self, **kwargs):
        self.required_equipment = ['dc_supply',
                                   'dc_supply2',
                                   'scope',
                                   'sig_gen']
        super().__init__(**kwargs)
        self.dc_supply = self.eq.equipment['dc_supply']
        self.dc_supply2 = self.eq.equipment['dc_supply2']
        self.scope = self.eq.equipment['scope']
        self.sig_gen = self.eq.equipment['sig_gen']

        self.dc_supply.set_voltage(3.1, 2)
        self.dc_supply2.query("*IDN?")

        print('asdf')

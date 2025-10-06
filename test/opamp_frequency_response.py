"""
    A test script to frequency sweep an op-amp to produce a Bode plot.
    This test requires two power supply to provide both positive and negative supply voltage, a frequency generator,
    an oscilloscope with two channels to read the input signal frequency and level and output frequency and level.
    The data is recorded as frequency, input signal level, input signal frequency, output signal level,
    output phase shift, gain (linear), gain (dB).
"""

import sys

class OpampFrequencyResponse:
    def __init__(self, **kwargs):
        equipment_manager = kwargs.get("equipment_manager", None)
        if equipment_manager is None:
            sys.exit("No equipment found, exit program.")
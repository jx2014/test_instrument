"""
    A test script to frequency sweep an op-amp to produce a Bode plot.
    This test requires two power supply to provide both positive and negative supply voltage, a frequency generator,
    an oscilloscope with two channels to read the input signal frequency and level and output frequency and level.
    The data is recorded as frequency, input signal level, input signal frequency, output signal level,
    output phase shift, gain (linear), gain (dB).
"""
import time
from .test_template import TestTemplate
import math

class OpampFrequencyResponse(TestTemplate):
    def __init__(self, **kwargs):
        self.required_equipment = ['dc_supply',
                                   'dc_supply2',
                                   'scope',
                                   'sig_gen']
        self.test_name = "OpampFrequencyResponseTest"
        super().__init__(**kwargs)
        self.dc_supply = self.eq.equipment['dc_supply']
        self.dc_supply2 = self.eq.equipment['dc_supply2']
        self.scope = self.eq.equipment['scope']
        self.sig_gen = self.eq.equipment['sig_gen']
        #self.sweep_frequencies = [7, 14, 22, 36, 43, 51, 58, 65, 72, 80, 87, 145, 217, 362, 506, 651, 723, 1447, 2170,
        #                          3617]
        self.sweep_frequencies = range(1, 3601, 1)
        # Assume dc power supplies have been set properly.
        self.initialization()

    def initialization(self):
        self.sig_gen.channel = 1
        self.sig_gen.set_waveform_sine()
        self.sig_gen.set_waveform_unit_vpp(ch=1)
        self.sig_gen.set_modulation(mode="cont")
        self.sig_gen.set_frequency(freq=1000)
        self.sig_gen.set_amplitude(amplitude=1)  # 1 Vpp
        self.sig_gen.turn_on()

        self.scope.set_trigger_source(1)
        self.scope.set_trigger_level(0)
        self.scope.set_trigger_slope("POS")
        self.scope.set_trigger_coupling("AC")
        self.scope.set_horizontal_range(0.01)

        self.scope.turn_channel_on(ch=1)
        self.scope.turn_channel_on(ch=2)

        self.scope.set_probe_offset(ch=1, offset=-1)
        self.scope.set_vertical_scale(ch=1, value=0.5, unit="V")

        self.scope.set_probe_offset(ch=2, offset=1)
        self.scope.set_vertical_scale(ch=2, value=0.5, unit="V")

        self.dc_supply.set_output(voltage=10, current=.05)
        self.dc_supply2.set_output(voltage=10, current=.05)
        self.dc_supply.turn_on()
        self.dc_supply2.turn_on()

    def get_proper_scope_range(self, scope_range, waveform_period):
        """
            set the o-scope horizontal range so that the waveform falls within 5 to 100 periods of scope window
        """
        while True:
            if scope_range / waveform_period >= 100:
                scope_range = scope_range / 10
            elif scope_range / waveform_period < 10:
                scope_range = scope_range * 10
            else:
                break
        return scope_range

    def run_test(self):
        hor_range = 0.01
        for f in self.sweep_frequencies:
            self.sig_gen.set_frequency(freq=f)
            time.sleep(0.1)
            period = 1 / f
            hor_range = self.get_proper_scope_range(hor_range, period)
            self.scope.set_horizontal_range(hor_range)
            self.logger.debug(f"Set horizontal range: {hor_range}")
            time.sleep(0.1)
            vin = self.scope.get_vpp(ch=1)
            vout = self.scope.get_vpp(ch=2)
            gain = vout / vin
            gain_db = 20 * math.log10(gain)
            print("%d, %0.4f, %0.4f, %0.4f, %.2f" % (f, vin, vout, gain, gain_db))






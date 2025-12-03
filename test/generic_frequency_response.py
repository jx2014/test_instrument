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
import pandas as pd
import matplotlib.pyplot as plt

class GenericFrequencyResponse(TestTemplate):
    def __init__(self, **kwargs):
        self.required_equipment = ['dc_supply',
                                   'scope',
                                   'sig_gen']
        self.test_name = "GenericFrequencyResponseTest"
        super().__init__(**kwargs)
        self.dc_supply = self.eq.equipment['dc_supply']
        freq_sweep_range = range(1, 1001, 1)
        self.vin_level = 100e-6
        self.scope = self.eq.equipment['scope']
        self.sig_gen = self.eq.equipment['sig_gen']
        self.sweep_frequencies = kwargs.get("frequencies", [x/10 for x in freq_sweep_range])
        # Assume dc power supplies have been set properly.
        self.df = pd.DataFrame(columns=['frequency', 'vout', 'gain', 'gain(dB)'])
        self.scope.instrument.timeout = 120000
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
        self.scope.set_horizontal_range(0.1)

        self.scope.turn_channel_on(ch=1)

        self.scope.set_probe_offset(ch=1, offset=0)
        self.scope.set_vertical_scale(ch=1, value=.5, unit="V")
        self.dc_supply.turn_on()

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
                if scope_range >= 10:
                    scope_range = 10
                break
        return scope_range

    def plot_result(self, **kwargs):
        min_gain_idx = self.df['gain(dB)'].idxmin()
        min_freq = self.df.loc[min_gain_idx, 'frequency']
        min_gain_db = self.df.loc[min_gain_idx, 'gain(dB)']
        plt.figure(figsize=(12, 8))
        plot_comment = kwargs.get("comments", "")
        #plt.semilogx(self.df['frequency'], self.df['gain(dB)'], 'b-', linewidth=2, label='Gain (dB)')
        plt.plot(self.df['frequency'], self.df['gain(dB)'], 'b-', linewidth=2, label=f'Gain: {min_gain_db:.2f} dB')
        plt.plot(min_freq, min_gain_db, 'ro', markersize=10, label=f'Notch: {min_freq:.2f} Hz')
        # plt.annotate(f'Notch: {min_freq:.2f} Hz\nGain: {min_gain_db:.2f} dB',
        #              xy=(min_freq, min_gain_db),
        #              xytext=(min_freq * 1.5, min_gain_db + 5),
        #              arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
        #              fontsize=12,
        #              bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
        plt.axvline(x=min_freq, color='r', linestyle='--')
        plt.axhline(y=min_gain_db, color='r', linestyle='--')
        plt.xlabel('Frequency (Hz)', fontsize=14)
        plt.ylabel('Gain (dB)', fontsize=14)
        plt.title(f'Frequency Response - Notch Filter\n[{plot_comment}]', fontsize=16)
        plt.grid(True, which='both', alpha=0.3)
        plt.legend(fontsize=12)
        plt.tight_layout()
        plt.show()

    def run_test(self):
        hor_range = 0.01
        for f in self.sweep_frequencies:
            self.sig_gen.set_frequency(freq=f)
            while self.sig_gen.get_frequency() != f:
                time.sleep(0.1)
            period = 1 / f
            hor_range = self.get_proper_scope_range(hor_range, period)
            self.scope.set_horizontal_range(hor_range)
            self.logger.debug(f"Set horizontal range: {hor_range}")
            time.sleep(0.1)
            vout = self.scope.get_vpp(ch=1)
            gain = vout / self.vin_level
            gain_db = 20 * math.log10(gain)
            print("%0.1f, %0.4f, %0.4f, %.2f" % (f, vout, gain, gain_db))
            new_row = pd.DataFrame({
                'frequency': [f],
                'vout': [vout],
                'gain': [gain],
                'gain(dB)': [gain_db]
            })
            self.df = pd.concat([self.df, new_row], ignore_index=True)

        self.df.to_csv('frequency_response.csv', index=False)
        self.plot_result(comments="Full circuit, 12.5°C")






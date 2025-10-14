from .signal_generator_template import SignalGeneratorTemplate


class UTG962E(SignalGeneratorTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Uni-T UTG962E"

    def turn_on(self, ch=1):
        self.write(f":CHANnel{ch}:OUTPut ON")

    def turn_off(self, ch=1):
        self.write(f":CHANnel{ch}:OUTPut OFF")

    def get_frequency(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:FREQuency?"))

    def set_frequency(self, ch=1, freq=1000):
        self.write(f":CHANnel{ch}:BASE:FREQuency {freq}")

    def get_period(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:PERiod?"))

    def set_period(self, ch=1, period=0.001):
        self.write(f":CHANnel{ch}:BASE:PERiod {period}")

    def get_duty_cycle(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:DUTY?"))

    def set_duty_cycle(self, ch=1, duty=0.5):
        self.write(f":CHANnel{ch}:BASE:DUTY {duty}")

    def get_amplitude(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:AMPLitude?"))

    def set_amplitude(self, ch=1, amplitude=1):
        self.write(f":CHANnel{ch}:BASE:AMPLitude {amplitude}")

    def get_offset(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:OFFSet?"))

    def set_offset(self, ch=1, offset=0):
        self.write(f":CHANnel{ch}:BASE:OFFSet {offset}")

    def get_phase(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:PHASe?"))

    def set_phase(self, ch=1, phase=0):
        return self.write(f":CHANnel{ch}:BASE:PHASe {phase}")

    def get_output_impedance(self, ch=1):
        return float(self.query(f":CHANnel{ch}:LOAD?"))

    def set_output_impedance_high_z(self, ch=1):
        self.write(f":CHANnel{ch}:LOAD 10000")

    def set_output_impedance_50ohm(self, ch=1):
        self.write(f":CHANnel{ch}:LOAD 50")

    def set_output_impedance_75ohm(self, ch=1):
        self.write(f":CHANnel{ch}:LOAD 75")

    def get_waveform_type(self, ch=1):
        self.query(f":CHANnel{ch}:BASE:WAVe?")

    def set_waveform_sine(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe SINe")

    def set_waveform_square(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe SQUare")

    def set_waveform_pulse(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe PULSe")

    def set_waveform_ramp(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe RAMP")

    def set_waveform_arb(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe ARB")

    def set_waveform_noise(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe NOISe")

    def set_waveform_dc(self, ch=1):
        self.write(f":CHANnel{ch}:BASE:WAVe DC")

    def set_value_high(self, ch=1, value=0.5):
        self.write(f":CHANnel{ch}:BASE:HIGH {value}")

    def set_value_low(self, ch=1, value=-0.5):
        self.write(f":CHANnel{ch}:BASE:LOW {value}")

    def get_value_high(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:HIGH?"))

    def get_value_low(self, ch=1):
        return float(self.query(f":CHANnel{ch}:BASE:LOW?"))

    def set_cw(self, ch=1):
        raise NotImplementedError("set_cw must be implemented in child class")

    def set_remote(self):
        self.write(":SYSTem:LOCK ON")

    def set_local(self):
        self.write(":SYSTem:LOCK OFF")

    # equipment dependent functions
    def get_phase_mode(self):
        return self.query(":SYSTem:PHASE:MODE?")

    def set_phase_mode(self, mode="SYNC"):
        """
            Control the phase mode between channels. The starting phases of two channels are synchronized if it
            is synchronous, otherwise independent.
            available modes: INDependent or SYNChronization
        """
        if mode.lower() in "INDependent".lower():
            self.write(f":SYSTem:PHASe:MODe INDependent")
        elif mode.lower() in "SYNChronization".lower():
            self.write(f":SYSTem:PHASe:MODe SYNChronization")

    def set_beep(self, beep=0):
        self.write(f":SYSTem:BEEP {beep}")

    def set_number_format(self, form="COMMa"):
        """
            Control the separator of system number format.
            available modes: COMMa SPACe NONe
        """
        if form.lower() in "comma".lower():
            self.write(f":SYSTem:NUMBer:FORMat COMMa")
        elif form.lower() in "space".lower():
            self.write(f":SYSTem:NUMBer:FORMat SPACe")
        elif form.lower() in "none".lower():
            self.write(f":SYSTem:NUMBer:FORMat NONe")

    def get_waveform_unit(self, ch=1):
        return self.query(f":CHANnel{ch}:AMPLitude:UNIT?")

    def set_waveform_unit_vpp(self, ch=1):
        self.write(f":CHANnel{ch}:AMPLitude:UNIT VPP")

    def set_waveform_unit_vrms(self, ch=1):
        self.write(f":CHANnel{ch}:AMPLitude:UNIT VRMS")

    def set_waveform_unit_dbm(self, ch=1):
        self.write(f":CHANnel{ch}:AMPLitude:UNIT DBM")

    def get_modulation(self, ch=1):
        return self.query(f":CHANnel{ch}:MODe?")

    def set_modulation(self, ch=1, mode="CONTINUE"):
        if mode.lower() in "continue":
            self.write(f":CHANnel{ch}:MODe CONTINUE")
        elif mode.lower() in "am":
            self.write(f":CHANnel{ch}:MODe AM")
        elif mode.lower() in "pm":
            self.write(f":CHANnel{ch}:MODe PM")
        elif mode.lower() in "fm":
            self.write(f":CHANnel{ch}:MODe FM")
        elif mode.lower() in "fsk":
            self.write(f":CHANnel{ch}:MODe FSK")
        elif mode.lower() in "line":
            self.write(f":CHANnel{ch}:MODe Line")
        elif mode.lower() in "log":
            self.write(f":CHANnel{ch}:MODe Log")

    def get_modulate_signal_type(self, ch=1):
        return self.query(f":CHANnel{ch}:MODulate:WAVe?")

    def set_modulate_signal_type(self, ch=1, wave="SINe"):
        if wave.lower() in "sine":
            self.write(f":CHANnel{ch}:MODulate:WAVe SINe")
        elif wave.lower() in "square":
            self.write(f":CHANnel{ch}:MODulate:WAVe SQUare")
        elif wave.lower() in "upramp":
            self.write(f":CHANnel{ch}:MODulate:WAVe UPRamp")
        elif wave.lower() in "dnramp":
            self.write(f":CHANnel{ch}:MODulate:WAVe DNRamp")
        elif wave.lower() in "arb":
            self.write(f":CHANnel{ch}:MODulate:WAVe ARB")
        elif wave.lower() in "noise":
            self.write(f":CHANnel{ch}:MODulate:WAVe NOISe")

    def get_modulate_signal_frequency(self, ch=1):
        return float(self.query(f":CHANnel{ch}:MODulate:FREQuency?"))

    def set_modulate_signal_frequency(self, ch=1, freq=100):
        self.write(f":CHANnel{ch}:MODulate:FREQuency {freq}")

    def tear_down(self):
        self.turn_off(1)
        self.turn_off(2)

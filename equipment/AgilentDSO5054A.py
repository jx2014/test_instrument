from .oscilloscope_template import OscilloscopeTemplate

class DSO5054A(OscilloscopeTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Agilent DSO5054A"

    def get_probe_offset(self, ch=1):
        return float(self.query(f":CHANnel{ch}:OFFSet?"))

    def set_probe_offset(self, ch=1, offset=0):
        self.write(f":CHANnel{ch}:OFFSet {offset}")

    def get_probe_attenuation(self, ch=1):
        return float(self.query(f":CHANnel{ch}:PROBe?"))

    def set_probe_attenuation(self, ch=1, atten=10):
        self.write(f":CHANnel{ch}:OFFSet {atten}")

    def get_vertical_scale(self, ch=1):
        return float(self.query(f":CHANnel{ch}:SCAle?"))

    def set_vertical_scale(self, ch=1, value=1, unit="mV"):
        self.write(f":CHANnel{ch}:SCALe {value} {unit}")

    def get_vertical_range(self, ch=1):
        return float(self.query(f":CHANnel{ch}:RANGe?"))

    def set_vertical_range(self, ch=1, value=1, unit="mV"):
        self.write(f":CHANnel{ch}:RANGe {value} {unit}")

    def get_horizontal_scale(self):
        return float(self.query(":TIMebase:SCALe?"))

    def set_horizontal_scale(self, time_scale=0.01):
        self.write(f":TIMebase:SCALe {time_scale}")

    def get_horizontal_range(self):
        return float(self.query(":TIMebase:RANGe?"))

    def set_horizontal_range(self, time_range=0.001):
        self.write(f":TIMebase:RANGe {time_range}")

    def get_trigger_source(self):
        chan = self.query(":TRIGger:SOURce?")
        if "CHAN" in chan:
            return int(chan.rstrip().split("CHAN")[1])
        return None

    def set_trigger_source(self, ch=1):
        self.write(f":TRIGger:SOURce CHANnel{ch}")

    def get_trigger_slope(self):
        return self.query(":TRIGger:SLOPe?")

    def set_trigger_slope(self, slope="POS"):
        if slope.lower() in "positive":
            self.write(f":TRIGger:SLOPe POSitive")
        elif slope.lower() in "negative":
            self.write(f":TRIGger:SLOPe NEGative")
        elif slope.lower() in "alternate":
            self.write(f":TRIGger:SLOPe ALTernate")

    def get_trigger_coupling(self):
        return self.query(":TRIGger:COUPling?")

    def set_trigger_coupling(self, coupling="DC"):
        if coupling.lower() in "dc":
            self.write(":TRIGger:COUPling DC")
        elif coupling.lower() in "ac":
            self.write(":TRIGger:COUPling AC")
        elif coupling.lower() in "dc":
            self.write(":TRIGger:COUPling LFReject")

    def get_trigger_level(self):
        return float(self.query(":TRIGger:LEVel?"))

    def set_trigger_level(self, level=0):
        self.write(f":TRIGger:LEVel {level}")

    def get_acquire_mode(self):
        """
            return one of three modes: RTIMe realtime, ETIMe equivalent time mode, SEGM, segmented memory mode
        :return: str
        """
        return self.query(":ACQuire:MODE?")

    def set_acquire_mode(self, mode="RTIMe"):
        if mode.lower() in "rtime":
            self.write(":ACQuire:MODE RTIMe")
        elif mode.lower() in "etime":
            self.write(":ACQuire:MODE ETIMe")
        elif mode.lower() in "segmented":
            self.write(":ACQuire:MODE SEGMented")

    def turn_channel_on(self, ch=1):
        self.write(f":CHANnel{ch}:DISPlay ON")

    def turn_channel_off(self, ch=1):
        self.write(f":CHANnel{ch}:DISPlay OFF")

    def get_channel_impedance(self, ch=1):
        return self.query(f":CHANnel{ch}:IMPedance?")

    def set_channel_impedance(self, ch=1, z=1000000):
        if z == 1000000:
            self.write(f":CHANnel{ch}:IMPedance ONEM")
        elif z == 50:
            self.write(f":CHANnel{ch}:IMPedance FIFT")

    def set_channel_bandwidth(self, bw):
        raise NotImplementedError("set_channel_bandwidth must be implemented in child class")

    def get_frequency(self, ch):
        return float(self.query(f":MEASure:FREQuency? CHANnel{ch}"))

    def get_vpp(self, ch):
        return float(self.query(f":MEASure:VPP? CHANnel{ch}"))

    def get_vpps(self, channels=None):
        if channels is None:
            channels = [1]
        cmd_string = ""
        for ch in channels:
            cmd_string += f":MEASure:VPP? CHANnel{ch};"
        values = self.query(cmd_string)
        return [float(v) for v in values.split(";")]


    def get_vrms(self, ch):
        return float(self.query(f":MEASure:VRMS? CHANnel{ch}"))

    def get_vaverage(self, ch):
        return float(self.query(f":MEASure:VAVerage? CHANnel{ch}"))

    def get_screenshot(self):
        raise NotImplementedError("get_screenshot must be implemented in child class")

    def get_time_base_mode(self):
        return self.query(":TIMebase:MODE?")

    def set_time_base_normal_mode(self):
        self.write(":TIMebase:MODE MAIN")

    def set_time_base_window_mode(self):
        self.write(":TIMebase:MODE MAIN")

    def set_time_base_roll_mode(self):
        self.write(":TIMebase:MODE ROLL")

    def set_time_base_xy_mode(self):
        self.write(":TIMebase:MODE ROLL")

    def get_time_base_position(self):
        return float(self.query(":TIMebase:POSition?"))

    def set_time_base_position(self, pos=0):
        self.write(":TIMebase:POSition {pos}")

    def get_time_base_reference(self):
        return self.query(":TIMebae:REFerence?")

    def set_time_base_reference_left(self):
        self.write(":TIMebae:REFerence LEFT")

    def set_time_base_reference_center(self):
        self.write(":TIMebae:REFerence CENT")

    def set_time_base_reference_right(self):
        self.write(":TIMebae:REFerence RIGHT")

#### vendor specific commands ####
    def get_acquire_type(self):
        return self.query(":ACQuire:TYPE?")

    def set_acquire_type(self, acquire_type="normal"):
        if acquire_type.lower() in "normal:":
            self.write(":ACQuire:TYPE NORMAL")
        elif acquire_type.lower() in "average:":
            self.write(":ACQuire:TYPE AVERage")
        elif acquire_type.lower() in "hresolution:":
            self.write(":ACQuire:TYPE HRESolution")
        elif acquire_type.lower() in "peak:":
            self.write(":ACQuire:TYPE PEAK")

    def get_acquire_points(self):
        return float(self.query(":ACQuire:POINts?"))

    def set_acquire_points(self, points=1000000):
        self.write(f":ACQuire:POINts {points}")

    def tear_down(self):
        pass
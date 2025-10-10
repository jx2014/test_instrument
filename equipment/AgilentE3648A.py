from .dc_power_supply_template import DCPowerSupplyTemplate
import time

def channel_selector(func):
    def wrapper(self, *args, **kwargs):
        channel = kwargs.pop('channel', None)
        if channel is None:
            channel = self.default_channel
        if f"OUTPUT{channel}" == self.which_output():
            pass
        elif channel == 1:
            self.select_output1()
        else:
            self.select_output2()
        return func(self, *args, **kwargs)

    return wrapper

class E3648A(DCPowerSupplyTemplate):
    def __init__(self, equipment_config):
        super().__init__(equipment_config)
        self.name = "Agilent E3648A"

    def select_output1(self):
        while True:
            self.write("INST:SELECT OUT1")
            time.sleep(0.1)
            if self.which_output() == 'OUTP1':
                break

    def select_output2(self):
        while True:
            self.write("INST:SELECT OUT2")
            time.sleep(0.1)
            if self.which_output() == 'OUTP2':
                break

    def which_output(self):
        return self.query("INST?").strip()

    @channel_selector
    def get_voltage(self, channel=None):
        return float(self.query(f"MEAS:VOLT?"))

    @channel_selector
    def get_current(self,  channel=None):
        return float(self.query(f"MEAS:CURR?"))

    @channel_selector
    def set_voltage(self, voltage, channel=None):
        self.write(f"VOLT {voltage}")

    @channel_selector
    def set_current(self, current, channel=None):
        self.write(f"CURR {current}")

    def turn_on(self):
        self.write(f"OUTP ON")

    def turn_off(self):
        self.write(f"OUTP OFF")

    @channel_selector
    def set_output(self, voltage, current, channel=None):
        self.set_voltage(voltage, channel)
        self.set_current(current, channel)

    def get_system_error(self):
        while True:
            error_msg = self.query("SYSTem:ERRor?")
            print(error_msg)
            if '+0,"No error"' in error_msg:
                break
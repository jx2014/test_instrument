import time
from .multimeter_template import MultiMeterTemplate


class Fluke289(MultiMeterTemplate):
    def __init__(self, general_equipment_config):
        equipment_specific_config = {"baud_rate": 115200,
                                     "write_termination": "\r",
                                     "read_termination": "\r",
                                     "timeout": 1000
                                     }
        super().__init__(general_equipment_config, special_config=equipment_specific_config)
        self.name = "Fluke 289"

    def get_idn(self):
        self.instrument.write_raw(b"ID\r")
        t0 = time.time()
        while self.instrument.bytes_in_buffer != 27:
            time.sleep(0.001)
            if time.time() - t0 > 10:
                break
        response = self.instrument.read_bytes(self.instrument.bytes_in_buffer)
        response = response.decode()
        responses = response.split("\r")
        if responses[0] == '0':
            return responses[1]
        return "Unable to identify device"

    def get_all_reading(self):
        result = self.query_raw('QDDA\r')
        result = result.split("\r")
        if result[0] == "0":
            return result
        return "Unable to get all readings"

    def get_reading(self):
        result = self.query_raw('QM\r')
        result = result.split("\r")
        try:
            if result[0] == "0":
                return float(result[1].split(",")[0])
        except ValueError:
            pass
        return "Unable to get all readings"


    def tear_down(self):
        pass
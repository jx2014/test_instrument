import types
import pyvisa as py
import time
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.animation import FuncAnimation

def get_waveform_preamble(self):
    preamble_result = self.query(":waveform:pre?")
    preamble_result = preamble_result.strip().split(',')
    byte_order = self.query(":waveform:byteorder?").strip()
    print("Format:          ", {0: "BYTE", 1: "WORD", 4: "ASCII"}.get(int(preamble_result[0])))
    print("Type:            ", {2: "Average", 0: "NORMal", 1: "PEAK", 3: "HIRes"}.get(int(preamble_result[1])))
    print("Data points:     ", int(preamble_result[2]))
    print("Acquire Count:   ", int(preamble_result[3]))
    print("xincrement:      ", float(preamble_result[4]))
    print("xorigin:         ", float(preamble_result[5]))
    print("xreference:      ", float(preamble_result[6]))
    print("yincrement:      ", float(preamble_result[7]))
    print("yorigin:         ", float(preamble_result[8]))
    print("yreference:      ", float(preamble_result[9]))
    print("byte order:      ", byte_order)
    print("unsigned:        ", self.query(":waveform:unsigned?").strip())
    return {"Format": {0: "BYTE", 1: "WORD", 4: "ASCII"}.get(int(preamble_result[0])),
            "Type": int(preamble_result[1]),
            "Data points": int(preamble_result[2]),
            "Acquire count": int(preamble_result[3]),
            "xincrement": float(preamble_result[4]),
            "xorigin": float(preamble_result[5]),
            "xreference": float(preamble_result[6]),
            "yincrement": float(preamble_result[7]),
            "yorigin": float(preamble_result[8]),
            "yreference": float(preamble_result[9]),
            "byte order": byte_order,
            }


def query2(self, cmd):
    self.write(cmd)
    if cmd[-1:] == "?":
        result = self.read_raw()
        try:
            return result.decode('ascii')
        except UnicodeDecodeError:
            return result

def get_waveform_data(self):
    waveform_info = self.get_waveform_preamble()
    xref = waveform_info["xreference"]
    xinc = waveform_info["xincrement"]
    xo = waveform_info["xorigin"]
    yref = waveform_info["yreference"]
    yinc = waveform_info["yincrement"]
    yo = waveform_info["yorigin"]

    if waveform_info["Format"] == "WORD":
        expected_data_points = 2 * waveform_info["Data points"]
    else:
        expected_data_points = waveform_info["Data points"]

    waveform_data = self.query2(":waveform:data?")
    waveform_data = waveform_data[10:-1]

    if waveform_info["Format"] == "ASCII":
        waveform_data = waveform_data.split(",")

    if expected_data_points != len(waveform_data):
        print(f"expected_data_points {expected_data_points} do not match "
              f"actual number of data points: {len(waveform_data)}")
        print(waveform_data)
        return None

    if waveform_info["Format"] == "ASCII":
        for i, data_point in enumerate(waveform_data):
            # time of each data point = [(data point indx - xreference) * xincrement] + xorigin
            yield float((i - xref) * xinc + xo), float(data_point)

    if waveform_info["Format"] == "BYTE":
        for i, data_point in enumerate(waveform_data):
            yield float((i - xref) * xinc + xo), float((data_point - yref) * yinc + yo)

    if waveform_info["Format"] == "WORD":
        high_byte = 0
        for i, data_point in enumerate(waveform_data):
            if i % 2 == 0:
                high_byte = waveform_data[i] * 256
                continue
            # convert word data to voltage
            data_point = high_byte + waveform_data[i]
            yield float((i/2 - xref) * xinc + xo), float((data_point - yref) * yinc + yo)

rm = py.ResourceManager()

scope = rm.open_resource("GPIB0::12::INSTR")

scope.query("*IDN?")

scope.query2 = types.MethodType(query2, scope)
scope.get_waveform_preamble = types.MethodType(get_waveform_preamble, scope)
scope.get_waveform_data = types.MethodType(get_waveform_data, scope)

#scope.write(":waveform:points max")
scope.query(":waveform:points?")

scope.query(":waveform:pre?")
scope.query(":waveform:data?")

scope.query(":waveform:byteorder?")
scope.query(":waveform:pre?")
scope.query(":waveform:unsigned?")

scope.write(":waveform:format word")
scope.query(":waveform:pre?")
scope.write(":waveform:data?")
data_raw_word = scope.read_raw()

scope.write(":waveform:format byte")
scope.query(":waveform:pre?")
scope.write(":waveform:data?")
data_raw_byte = scope.read_raw()

scope.write(":waveform:format ascii")
data_ascii = scope.query(":waveform:data?")
# time of each data point = [(data point indx - xreference) * xincrement] + xorigin
# voltage of each data point = [(data_value - yrefrence) * yincrement] + yorigin

data_ascii = data_ascii[10:]
data_ascii = data_ascii.strip()
data_ascii = data_ascii.split(',')
data_ascii = [float(x) for x in data_ascii]


# Initialize containers for time (x) and voltage (y)
x = []
y = []

# Load data directly from your generator
for t, v in scope.get_waveform_data():  # Uses your actual generator
    x.append(t)  # Time values on x-axis
    y.append(v)  # Voltage values on y-axis

x = np.array(x)
y = np.array(y)
n_points = len(x)

# Calculate 10 equal divisions based on data point count
division_indices = np.linspace(0, n_points-1, num=11, dtype=int)
division_x = x[division_indices]  # Time values at division boundaries

# Create plot with oscilloscope-style formatting
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b-', linewidth=1, label='Voltage')

# Configure x-axis for 10 equal data point divisions
plt.xticks(division_x)
plt.xlabel("Time (s)")
plt.xlim(x[0], x[-1])  # Explicit time range

# Configure y-axis (auto-scaled voltage)
plt.ylabel("Voltage (V)")
plt.autoscale(axis='y')  # Auto-scale to voltage range

# Add oscilloscope-style grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)
plt.title(f"Voltage vs. Time: {n_points} points, 10 divisions")
plt.legend()
plt.tight_layout()
plt.show()
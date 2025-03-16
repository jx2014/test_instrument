import pyvisa as py

def get_waveform_preamble(scope):
    preamble_result = scope.query(":waveform:pre?")
    preamble_result = preamble_result.strip().split(',')
    print("Format:          ", {0: "Byte", 1: "WORD", 4: "ASCII"}.get(int(preamble_result[0])))
    print("Type:            ", {2: "Average", 0: "NORMal", 1: "PEAK", 3: "HIRes"}.get(int(preamble_result[1])))
    print("Data points:     ", int(preamble_result[2]))
    print("Acquire Count:   ", preamble_result[3])
    print("xincrement:      ", float(preamble_result[4]))
    print("xorigin:         ", float(preamble_result[5]))
    print("xreference:      ", float(preamble_result[6]))
    print("yincrement:      ", float(preamble_result[7]))
    print("yorigin:         ", float(preamble_result[8]))
    print("yreference:      ", float(preamble_result[9]))
    print("byte order:      ", scope.query(":waveform:byteorder?").strip())
    print("unsigned:        ", scope.query(":waveform:unsigned?").strip())




rm = py.ResourceManager()

scope = rm.open_resource("GPIB0::12::INSTR")

scope.query("*IDN?")

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


import matplotlib.pyplot as plt

# Create x-axis (indices 0 to 99)
x = list(range(len(a)))

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(x, a, 'b.-', linewidth=1, markersize=8, label='Data Points')  # Blue line with dots
plt.grid(True)
plt.title('Plot of 100 Data Points')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()
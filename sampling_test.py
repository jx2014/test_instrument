import numpy as np
import matplotlib.pyplot as plt

# total plotting points for high speed sampling waveform.
# plot_points = 1000

f = 8
cycles = 24
total_time_interval = cycles / f

# Ts_hi is high speed sampling period
# Ts_hi = total_time_interval /  (plot_points - 1)
# Fs_hi = 1 / Ts_hi
Fs_hi = 100
Ts_hi = 1 / Fs_hi
plot_points = int(Fs_hi / f * cycles)
print(f"High sampling period: {Ts_hi*1000000}us, sampling frequency {Fs_hi/1000} KHz, plot points: {plot_points} points")
t = np.linspace(0, total_time_interval, plot_points)
# x = [t * ts for t in range(plot_points)]
# y = 3* np.sin(2 * np.pi * f/3 * t) + np.sin(2 * np.pi * 100 * t) + np.sin(2 * np.pi * 250 * t)
# y = np.sinc(2 * np.pi * f * (t-0.005))
# y = [0] * int(plot_points / 4) + [1] * int(plot_points / 2) + [0] * int(plot_points - np.ceil(plot_points * 3 / 4))
y = np.sin(2 * np.pi * f * t)
if len(y) < len(t):
    y.append(0)

y[int(len(y)/2):] = 0



fs = 0.1
Ts_lo = 1 / fs
ns =  int(total_time_interval / Ts_lo) + 1
ts = np.linspace(0, total_time_interval, ns)
ys = np.sin(2 * np.pi * f * ts)

# DFT for high speed sampling waveform
N = len(t)
X = [0] * N
P = [0] * N
for k in range(N):
    real = 0
    imagine = 0
    for n in range(N):
        angle = 2 * np.pi * k * n / N
        real = real + y[n] * np.cos(angle)
        imagine = imagine - y[n] * np.sin(angle)
    X[k] = np.sqrt(real**2 + imagine**2)
    P[k] = np.arctan2(imagine, real)

freq_indices = range(N)
freq = [k * Fs_hi / N for k in freq_indices]
X_axis = freq_indices
# Create figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=False)

# 1. Time-domain plot (your original)
ax1.plot(t, y, color="blue", label=f"sin(2πft), f = {f} Hz")
ax1.plot(ts, ys, "ro", label=f"Sampled, fs = {fs} Hz")
ax1.set_title(f"Continuous Sine Wave and Sampled Points")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Amplitude")
ax1.grid(True)
ax1.legend(loc='lower left')

# 2. Magnitude plot
ax2.plot(X_axis, X, "g-", label="Magnitude")
ax2.set_title("Magnitude Spectrum")
ax2.set_xlabel("Frequency (Hz))")
ax2.set_ylabel("Magnitude")
ax2.grid(True)
ax2.legend(loc='upper right')

# 3. Phase plot
ax3.plot(X_axis, P, "m-", label="Phase")
ax3.set_title("Phase Spectrum")
ax3.set_xlabel("Frequency (Hz)")
ax3.set_ylabel("Phase (radians)")
ax3.grid(True)
ax3.legend(loc='upper right')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()


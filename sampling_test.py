import numpy as np
import matplotlib.pyplot as plt

# total plotting points for high speed sampling waveform.
# plot_points = 1000

f = 600
cycles = 10
total_time_interval = cycles / f

# Ts_hi is high speed sampling period
# Ts_hi = total_time_interval /  (plot_points - 1)
# Fs_hi = 1 / Ts_hi
Fs_hi = 1000
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

# y[0] = 1
# y[1:] = 0
# y[10] = 1
# #y[20] = 1

# pulse train
f_pulse = 1000
a = np.round(Fs_hi / f_pulse)
y_pulse = [0] * len(t)
for i, n in enumerate(t):
    if i % a == 0:
        y_pulse[i] = 1

# sampled by pulse train
Ys = [0] * len(t)
for i in range(0, len(t)):
    Ys[i] = y_pulse[i] * y[i]



# DFT for sampled waveform
N = len(t)
X = [0] * N
P = [0] * N
Xp = [0] * N
Pp = [0] * N
for k in range(N):
    real = 0
    imagine = 0
    real_pulse = 0
    imagine_pulse = 0
    for n in range(N):
        angle = 2 * np.pi * k * n / N
        real = real + y[n] * np.cos(angle)
        imagine = imagine - y[n] * np.sin(angle)
        real_pulse = real_pulse + Ys[n] * np.cos(angle)
        imagine_pulse = imagine_pulse - Ys[n] * np.sin(angle)
    X[k] = np.sqrt(real**2 + imagine**2)
    P[k] = np.arctan2(imagine, real)
    Xp[k] = np.sqrt(real_pulse**2 + imagine_pulse**2)
    Pp[k] = np.arctan2(imagine_pulse, real_pulse)

freq_indices = range(N)
freq = [k * Fs_hi / N for k in freq_indices]
freq_pulse = [k * f_pulse / N for k in freq_indices]
X_axis = freq
X_axis_pulse = freq_pulse

# Create figure with 3 subplots
fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10, 12), sharex=False)

# 1. Time-domain plot (your original)
ax1.stem(t, y, "blue", label=f"f = {f} Hz")
# ax1.stem(ts, ys, "ro", label=f"Sampled, fs = {fs} Hz")
ax1.set_title(f"Continuous Sine Wave and Sampled Points")
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Amplitude")
ax1.grid(True)
ax1.legend(loc='lower left')

# 2. Magnitude plot
ax2.stem(X_axis, X, "go")
ax2.set_title("Magnitude Spectrum")
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Magnitude")
ax2.grid(True)
# ax2.legend(loc='upper right')

# 3. Phase plot
ax3.stem(X_axis, P, "mo")
ax3.set_title("Phase Spectrum")
ax3.set_xlabel("Frequency")
ax3.set_ylabel("Phase (radians)")
ax3.grid(True)
# ax3.legend(loc='upper right')

# # 4. pulse train
ax4.stem(t, y_pulse, "bo", )
ax4.set_title("Pulse Train")
ax4.set_xlabel("Time")
ax4.set_ylabel("Amplitude")
ax4.grid(True)
# ax4.legend(loc='upper right')

# 5. sampled by pulse train
ax5.stem(t, Ys, "ro", )
ax5.set_title("Sampled by Pulse Train")
ax5.set_xlabel("Time")
ax5.set_ylabel("Amplitude")
ax5.grid(True)

# 6. sampled by pulse train freq domain
ax6.stem(X_axis_pulse, Xp, )
ax6.set_title("Freq domain")
ax6.set_xlabel("Freq")
ax6.set_ylabel("Magnitude")
ax6.grid(True)


# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

plot_points = 1000

f = 4000
cycles = 4
total_time_interval = cycles / f

ts = total_time_interval /  (plot_points - 1)
t = np.linspace(0, total_time_interval, plot_points)
#x = [t * ts for t in range(plot_points)]
y = np.sin(2 * np.pi * f * t)


fs = 6000
ts = 1 / fs
ns =  int(total_time_interval / ts) + 1
t_s = np.linspace(0, total_time_interval, ns)
ys = np.sin(2 * np.pi * f * t_s)


plt.figure(figsize=(10, 6))  # Optional: larger figure for clarity
plt.plot(t, y, color="blue", label=f"sin(2πft), f = {f} Hz")  # Continuous signal
plt.plot(t_s, ys, "ro", label=f"Sampled, fs = {fs} Hz")  # Red dots for samples
plt.title(f"Continuous Sine Wave and Sampled Points")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()


# Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration

# Generate two sine waves
f1 = 5   # Frequency of first sine wave (Hz)
f2 = 10  # Frequency of second sine wave (Hz)

signal1 = np.sin(2 * np.pi * f1 * t)  # 5 Hz sine wave
signal2 = np.sin(2 * np.pi * f2 * t)  # 10 Hz sine wave

# Combine the signals
combined_signal = signal1 + signal2

# Compute FFT of combined signal
N = len(combined_signal)
freqs = np.fft.fftfreq(N, 1/fs)
fft_values = np.fft.fft(combined_signal)
magnitude = np.abs(fft_values) / N

# Plot time-domain signals
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(t, signal1)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, signal2)
plt.title('10 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, combined_signal)
plt.title('Combined Signal (5 Hz + 10 Hz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Plot frequency-domain representation
plt.figure(figsize=(10, 5))
plt.plot(freqs[:N//2], magnitude[:N//2])  # Plot only positive frequencies
plt.title('Frequency Spectrum of Combined Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 500  # Sampling frequency (Hz)
t = np.linspace(0, 2, 2 * fs, endpoint=False)  # 2 seconds duration

# Generate sine and cosine waves
f1 = 5   # Frequency of sine wave (Hz)
f2 = 10  # Frequency of cosine wave (Hz)

sine_wave = np.sin(2 * np.pi * f1 * t)   # 5 Hz sine wave
cosine_wave = np.cos(2 * np.pi * f2 * t) # 10 Hz cosine wave

# Multiply the two signals element-wise
multiplied_signal = sine_wave * cosine_wave

# Compute FFT of the multiplied signal
N = len(multiplied_signal)
freqs = np.fft.fftfreq(N, 1/fs)
fft_values = np.fft.fft(multiplied_signal)
magnitude = np.abs(fft_values) / N

# Plot the time-domain signals
plt.figure(figsize=(12, 10))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave)
plt.title('5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, cosine_wave)
plt.title('10 Hz Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, multiplied_signal)
plt.title('Product of 5 Hz Sine Wave and 10 Hz Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Plot frequency-domain (FFT)
plt.figure(figsize=(10, 5))
plt.plot(freqs[:N//2], magnitude[:N//2])
plt.title('Frequency Spectrum of the Multiplied Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds. Plot the original and shifted signals on the same graph for comparison.
import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
f = 5  # Frequency of sine wave (Hz)

# Original sine wave
original_signal = np.sin(2 * np.pi * f * t)

# Time shift (delay) of 0.1 seconds
time_shift = 0.1  # seconds
shifted_signal = np.sin(2 * np.pi * f * (t - time_shift))  # Time-shifted version

# Plot both signals
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Signal (5 Hz)', linewidth=2)
plt.plot(t, shifted_signal, '--', label='Shifted Signal (Delayed by 0.1 s)', linewidth=2)

plt.title('Original and Time-Shifted 5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.

import numpy as np
import matplotlib.pyplot as plt


fs = 1000 
t = np.linspace(0, 1, fs, endpoint=False)  
f = 10 

# Generate the original sine wave
original_signal = np.sin(2 * np.pi * f * t)

# Scale the amplitude by a factor of 3
scaled_signal = 3 * original_signal

# Plot both signals
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original 10 Hz Sine Wave', linewidth=2)
plt.plot(t, scaled_signal, '--', label='Scaled Signal (×3 Amplitude)', linewidth=2)

plt.title('Original and Amplitude-Scaled 10 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 

import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
f = 5  # Frequency of sine wave (Hz)

# Generate original sine wave
original_signal = np.sin(2 * np.pi * f * t)

# Reverse the signal in time
reversed_signal = original_signal[::-1]  # Reverse array
t_reversed = t[::-1]  # Corresponding reversed time axis (optional for clarity)

# Plot both signals
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original 5 Hz Sine Wave', linewidth=2)
plt.plot(t_reversed, reversed_signal, '--', label='Time-Reversed Signal', linewidth=2)

plt.title('Original and Time-Reversed 5 Hz Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
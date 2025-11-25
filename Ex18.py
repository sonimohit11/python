# Use Python to create a script that performs both linear and circular convolution on an audio file with an impulse response. Compare and visualize the results.

# Load audio signal and impulse response
fs_x, x = wavfile.read("audio.wav")
fs_h, h = wavfile.read("impulse.wav")
x = x.astype(float)
h = h.astype(float)
# If stereo, convert to mono
if len(x.shape) == 2:
    x = x.mean(axis=1)
if len(h.shape) == 2:
    h = h.mean(axis=1)
# Linear convolution
linear_conv = np.real(np.fft.ifft(np.fft.fft(x, len(x)+len(h)-1) * np.fft.fft(h, len(x)+len(h)-1)))
# Circular convolution using FFT
N = max(len(x), len(h))
x_pad = np.pad(x, (0, N - len(x)))
h_pad = np.pad(h, (0, N - len(h)))
circular_conv = np.real(np.fft.ifft(np.fft.fft(x_pad) * np.fft.fft(h_pad)))
# Plot results
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(x)
plt.title("Original Audio Signal")
plt.subplot(3, 1, 2)
plt.plot(linear_conv)
plt.title("Linear Convolution Output")
plt.subplot(3, 1, 3)
plt.plot(circular_conv)
plt.title("Circular Convolution Output")
plt.tight_layout()
plt.show()
# Save output audio (optional)
linear_out = np.int16(linear_conv / np.max(np.abs(linear_conv)) * 32767)
circular_out = np.int16(circular_conv / np.max(np.abs(circular_conv)) * 32767)
wavfile.write("linear_output.wav", fs_x, linear_out)
wavfile.write("circular_output.wav", fs_x, circular_out)
plt.show(block=True)



# Use Python to implement both cross-correlation and autocorrelation on a set of audio files (clean_audio.wav, noisy_audio.wav, periodic_audio.wav). Visualize and compare the results.

# Generate periodic audio
fs = 44100
t = np.linspace(0, 1, fs, endpoint=False)
x = 0.5 * np.sin(2 * np.pi * 440 * t)
wavfile.write("periodic_audio.wav", fs, x.astype(np.float32))
# Load audio files
fs1, clean = wavfile.read("clean_audio.wav")
fs2, noisy = wavfile.read("noisy_audio.wav")
fs3, periodic = wavfile.read("periodic_audio.wav")
# Use first 2 seconds
clean = clean[:fs1 * 2]
noisy = noisy[:fs2 * 2]
periodic = periodic[:fs3 * 2]
# Mono conversion
if clean.ndim == 2:
    clean = clean.mean(axis=1)
if noisy.ndim == 2:
    noisy = noisy.mean(axis=1)
if periodic.ndim == 2:
    periodic = periodic.mean(axis=1)
# Autocorrelation
auto_clean = np.correlate(clean, clean, mode="full")
auto_noisy = np.correlate(noisy, noisy, mode="full")
auto_periodic = np.correlate(periodic, periodic, mode="full")
# Cross-correlation
cross_clean_noisy = np.correlate(clean, noisy, mode="full")
cross_clean_periodic = np.correlate(clean, periodic, mode="full")
# Autocorrelation plots
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(auto_clean)
plt.title("Autocorrelation: Clean Audio")
plt.subplot(3, 1, 2)
plt.plot(auto_noisy)
plt.title("Autocorrelation: Noisy Audio"
plt.subplot(3, 1, 3)
plt.plot(auto_periodic)
plt.title("Autocorrelation: Periodic Audio")
plt.tight_layout()
plt.show()
# Cross-correlation plots
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(cross_clean_noisy)
plt.title("Cross-Correlation: Clean vs Noisy")
plt.subplot(2, 1, 2)
plt.plot(cross_clean_periodic)
plt.title("Cross-Correlation: Clean vs Periodic")
plt.tight_layout()
plt.show()

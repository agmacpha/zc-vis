import numpy as np
import matplotlib.pyplot as plt

def read_zc(file_path):
	with open(file_path, 'rb') as file:
		raw = np.fromfile(file, dtype=np.uint8)
	
	if len(raw) < 4:
		raise ValueError("File is corrupted or too short.")

	# Checking the file type
	FTYPE = raw[3]
	if not (129 <= FTYPE <= 132):
		raise ValueError("File type must be between 129 and 132.")
# TODO:
# 	this currently works for *.zc but got an error for a *.00# file
# 	check what these actually mean and do different things for different files like in the C version

	# Checking file integrity
	p = raw[0] + raw[1] * 256 + 1
	if p != 283:
		raise ValueError("File pointer check failed, file is corrupted!")
	times = []
	frequencies = []
	i = 4
	while i < len(raw) - 2:
		freq = raw[i] + (raw[i+1] << 8)
		time = raw[i+2] + (raw[i+3] << 8) + (raw[i+4] << 16) + (raw[i+5] << 24)
		if 10000 <= freq <= 180000:  # Example frequency range check
			times.append(time)
			frequencies.append(freq)
		i += 6

	return np.array(times), np.array(frequencies)
# TODO:
# 	adapt the plots to the frequency range of the file

def plot_zc(times, frequencies, HPF=16000, LPF=180000, pngpath='zc_plot.png'):
	# Filter the data
	valid_indices = (frequencies >= HPF) & (frequencies <= LPF)
	frequencies = frequencies[valid_indices]
	times = times[valid_indices] / 1e6  # convert microseconds to seconds

	plt.figure(figsize=(10, 5))
	plt.scatter(times, frequencies, c='red', s=0.1)
	plt.title("Zero Crossing Spectrogram")
	plt.xlabel("Time (Seconds)")
	plt.ylabel("Frequency (Hz)")
	plt.ylim([HPF, LPF])
	plt.grid(True)
	plt.savefig(pngpath)
	plt.close()

# Usage
file_path = '../test2.zc' 
times, frequencies = read_zc(file_path)
plot_zc(times, frequencies, pngpath='test2.png')

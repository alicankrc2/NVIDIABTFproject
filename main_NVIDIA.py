

import sounddevice as sd
import numpy as np
import wave
import math
import subprocess
import time
import matplotlib.pyplot as plt
import os

fig = []
ax = []

sd.default.device = 11
sd.default.samplerate = 44100
sd.default.channels = 2
sd.default.blocksize = 44100


def plot_sound_source(theta_degrees):
	# Mikrofonlar arası mesafe
	mic_distance = 1  # 0.07 metre
	mic1 = (-mic_distance / 2, 0)
	mic2 = (mic_distance / 2, 0)

	# Açıyı radian cinsine çevir
	angle_radians = np.radians(theta_degrees)

	# Ses kaynağının konumunu hesapla
	source_distance = 2.0  # Ses kaynağını 2 birim uzakta varsayalım
	source_x = source_distance * np.sin(angle_radians)
	source_y = source_distance * np.cos(angle_radians)

	fig = plt.figure(1)
	
	ax = fig.add_subplot(1, 1, 1)

	# Ses kaynağı konumu
	ax.plot([mic1[0], mic2[0]], [mic1[1], mic2[1]], 'bo', label='Mikrofonlar')
	ax.plot(source_x, source_y, 'rx', label='Ses Kaynağı')
	ax.plot([mic1[0], mic2[0]], [mic1[1], mic2[1]], 'b-')
	ax.plot([mic1[0], source_x], [mic1[1], source_y], 'r--')
	ax.plot([mic2[0], source_x], [mic2[1], source_y], 'r--')
	ax.set_aspect('equal')
	ax.set_xlim(-3, 3)
	ax.set_ylim(-3, 3)
	ax.axhline(0, color='black', linewidth=0.5)
	ax.axvline(0, color='black', linewidth=0.5)
	ax.grid(color='gray', linestyle='--', linewidth=0.5)
	ax.legend()
	ax.set_title('İki Mikrofon ile Ses Kaynağı Konum Tespiti')
	ax.set_xlabel('X Eksen')
	ax.set_ylabel('Y Eksen')

	# Açı bilgisini ekle
	angle_text = f'Açı: {theta_degrees}°'
	ax.text(0, 2.5, angle_text, fontsize=12, ha='center')

	fig.show()
	sd.sleep(3000)

	plt.close(fig)


def gcc_phat(sig, refsig, fs, max_tau=None, interp=16):
	n = sig.shape[0] + refsig.shape[0]

	SIG = np.fft.rfft(sig, n=n)
	REFSIG = np.fft.rfft(refsig, n=n)
	R = SIG * np.conj(REFSIG)

	cc = np.fft.irfft(R / np.abs(R), n=(interp * n))

	max_shift = int(interp * n / 2)
	if max_tau:
		max_shift = np.minimum(int(interp * fs * max_tau), max_shift)

	cc = np.concatenate((cc[-max_shift:], cc[:max_shift+1]))

	shift = np.argmax(cc) - max_shift

	tau = shift / float(interp * fs)

	return tau, cc

def calculate_doa(sample_rate, audio_data):

	data1 = audio_data[:, 0]
	data2 = audio_data[:, 1]

	sound_speed = 343.2 
	distance = 0.10  

	tau, _ = gcc_phat(data1, data2, fs=sample_rate, max_tau=distance / sound_speed)

	max_tau = distance / sound_speed
	theta = math.degrees(math.asin(tau / max_tau))

	return theta


def audio_callback(indata,frames,time,status):

	if status:
		print(f'Durum {status}')

	print(indata.shape)
	print(indata.dtype)
	doa = calculate_doa(sd.default.samplerate, indata)
	print(f'DoA: {doa:.2f}')
	plot_sound_source(doa)


def main():
	str2 = None
	# Grafiği oluştur

	str2 =  sd.InputStream(callback=audio_callback)
	str2.start()
	while True:
		sd.sleep(1000)


if __name__ == '__main__':

	main()






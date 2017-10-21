# -*- coding:utf-8 -*- 
# Author: Roc-J

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

output_file = 'output_generated.wav'

# 指定音频生成的参数
'''
时间， 采样频率， 音频的频率，
'''
duration = 3
sampling_freq = 44100
tone_freq = 587
min_val = -2 * np.pi
max_val = 2 * np.pi

t = np.linspace(min_val, max_val, duration * sampling_freq)
audio = np.sin(2 * np.pi * tone_freq * t)

# 加入噪声
noise  = 0.4 * np.random.rand(duration* sampling_freq)
audio += noise

# 转换成int16的整形
scaling_factor = pow(2, 15) -1
audio_normalized = audio / np.max(np.abs(audio))
audio_scaled = np.int16(audio_normalized * scaling_factor)

# write
write(output_file, sampling_freq, audio_scaled)

audio = audio[:100]
x_values = np.arange(0, len(audio), 1) / float(sampling_freq)

x_values *= 1000

plt.figure()
plt.plot(x_values, audio, color='black')
plt.title('Audio signal')
plt.xlabel('Times ')
plt.ylabel('Amplitude ')
plt.show()
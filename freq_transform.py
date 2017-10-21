# -*- coding:utf-8 -*- 
# Author: Roc-J

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sampling_freq, audio = wavfile.read('input_freq.wav')

audio = audio/(2.**15)

len_audio = len(audio)

# 傅里叶变化
transformed_signal = np.fft.fft(audio)
half_length = np.ceil((len_audio + 1)/2.0).astype(np.int16)
transformed_signal = abs(transformed_signal[0:half_length])
transformed_signal /= float(len_audio)
transformed_signal ** 2

# 提取信号的长度
len_ts = len(transformed_signal)

# 根据信号的长度将信号乘以2
if len_audio % 2:
    transformed_signal[1:len_ts] *= 2
else:
    transformed_signal[1:len_ts-1] *= 2

# 获取功率信号
power = 10 * np.log10(transformed_signal)

x_values = np.arange(0, half_length, 1) *(sampling_freq/len_audio) /1000.0

# plot
plt.figure()
plt.plot(x_values, power, color='black')
plt.xlabel('Freq (in kHz)')
plt.ylabel('Power (in db)')
plt.show()

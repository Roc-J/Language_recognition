# -*- coding:utf-8 -*- 
# Author: Roc-J

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# read the video file
sample_freq, audio = wavfile.read('input_read.wav')

# print the video params
print '\nShape: ', audio.shape
print 'Datatype: ', audio.dtype
print 'Duration: ', round(audio.shape[0]/float(sample_freq), 3), 'seconds'

# 标准化数值
audio = audio / (2.**15)

#
audio = audio[:30]

x_values = np.arange(0, len(audio), 1) /float(sample_freq)

x_values *= 1000

# 画出声音信号图形
plt.plot(x_values, audio, color='black')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude')
plt.title('Audio signal')
plt.show()

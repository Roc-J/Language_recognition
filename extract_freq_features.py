# -*- coding:utf-8 -*- 
# Author: Roc-J

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features  import mfcc, logfbank

sampling_freq, audio = wavfile.read('input_freq.wav')

# 提取MFCC和过滤器组特征
mfcc_features = mfcc(audio, sampling_freq)
filterbank_features = logfbank(audio, sampling_freq)

# 打印参数
print '\nMFCC: \n Number of windows = ', mfcc_features.shape[0]
print 'Length of each feature = ', mfcc_features.shape[1]
print '\nFilter bank: \n Number of windows =', filterbank_features.shape[0]
print 'Length of each feature = ', filterbank_features.shape[1]

# plot
mfcc_features = mfcc_features.T
plt.matshow(mfcc_features)
plt.title('MFCC')

filterbank_features = filterbank_features.T
plt.matshow(filterbank_features)
plt.title('Filter bank')
plt.show()
# -*- coding:utf-8 -*- 
# Author: Roc-J

import json
import numpy as np
from scipy.io.wavfile import write

def synthesizer(freq, duration, amp=1.0, sampling_freq=44100):
    # 创建时间轴
    t = np.linspace(0, duration, duration * sampling_freq)
    # 用输入参数构建音频实例
    audio = amp * np.sin(2 * np.pi * freq * t)
    return audio.astype(np.int16)

if __name__ == '__main__':
    tone_map_file = 'tone_freq_map.json'
    with open(tone_map_file, 'r') as f:
        tone_freq_map = json.loads(f.read())

    # 生成G调
    input_tone = 'E'
    duration = 2
    amplitude = 10000
    sampling_freq = 44100

    # 生成音阶
    synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)
    write('output_tone.wav', sampling_freq, synthesized_tone)

    tone_seq = [('D', 0.3), ('G', 0.6), ('C', 0.5), ('A', 0.3), ('Asharp', 0.7)]

    output = np.array([])
    for item in tone_seq:
        input_tone = item[0]
        duration = item[1]
        synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)
        output = np.append(output, synthesized_tone, axis=0)

    write('output_tone_seq.wav', sampling_freq, output)
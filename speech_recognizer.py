# -*- coding:utf-8 -*- 
# Author: Roc-J

import os
import argparse

import numpy as np
from scipy.io import wavfile
from hmmlearn import hmm
from python_speech_features import mfcc

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Trains the HMM classifier')
    parser.add_argument('--input-folder', dest='input_folder', required=True, help="Input folder containing the audio files insubfolders")
    return parser

class HMMTrainer(object):
    def __init__(self, model_name='GaussianHMM', n_components=4, cov_type='diag', n_iter=1000):
        self.model_name = model_name
        self.n_components = n_components
        self.cov_type = cov_type
        self.n_iter = n_iter
        self.models = []

        if self.model_name == 'GaussianHMM':
            self.model = hmm.GaussianHMM(n_components=self.n_components, covariance_type=self.cov_type, n_iter=self.n_iter)
        else:
            raise TypeError('Invalid model type')

    def train(self, X):
        '''
        训练
        :param X:
        :return:
        '''
        np.setter(all='ignore')
        self.models.append(self.model.fit(X))

    def get_score(self, input_data):
        '''
        得分
        :param input_data:
        :return:
        '''
        return self.model.score(input_data)

if __name__ == '__main__':
    args = build_arg_parser().parse_args()
    input_folder = args.input_folder

    hmm_models = []

    for dirname in os.listdir(input_folder):
        subfolder = os.path.join(input_folder, dirname)

        if not os.path.isdir(subfolder):
            continue

        labels = subfolder[subfolder.rfind('/') + 1:]

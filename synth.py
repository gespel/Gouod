import math
from abc import abstractmethod

import numpy as np


class Synth:
    phase: np.float32 = 0.0
    sample: np.float32 = 0.0
    freq: np.float32 = 600.0
    samplerate: np.float32 = 48000.0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_synth_name(self):
        pass

    @abstractmethod
    def set_frequency(self, freq: float):
        pass


class SineSynth(Synth):
    def __init__(self):
        pass

    def get_sample(self) -> np.float32:
        self.phase += (self.freq / self.samplerate) * 2.0 * 3.14159265
        return np.float32(np.sin(self.phase))

    def get_synth_name(self):
        return "SineSynth"

    def set_frequency(self, freq: np.float32):
        self.freq = freq

    def get_buffer(self):
        sampleslist = []
        for i in range(0, 1023):
            sampleslist.append(self.get_sample())
            # x.setFrequency(abs(y.getSample())*1000)

        samples = np.array(sampleslist).astype(np.float32)
        return samples


class SquareSynth(Synth):
    def __init__(self):
        pass

    def get_sample(self) -> np.float32:
        self.phase += (self.freq / self.samplerate) * 2.0 * 3.14159265
        if np.float32(np.sin(self.phase)) > 0:
            return 0.5
        elif np.float32(np.sin(self.phase)) < 0:
            return -0.5
        else:
            return 0

    def get_synth_name(self):
        return "SineSynth"

    def set_frequency(self, freq: np.float32):
        self.freq = freq

    def get_buffer(self):
        sampleslist = []
        for i in range(0, 1023):
            sampleslist.append(self.get_sample())
            # x.setFrequency(abs(y.getSample())*1000)

        samples = np.array(sampleslist).astype(np.float32)
        return samples
from abc import abstractmethod
from synth import *


class Module:
    parts = []
    input_sample: np.float32 = 0.0

    @abstractmethod
    def set_input(self, input_sample: np.float32):
        pass

    @abstractmethod
    def get_sample(self):
        pass

    @abstractmethod
    def get_buffer(self):
        pass


class DualSine(Module):
    def __init__(self):
        self.parts.append(SineSynth())
        self.parts.append(SineSynth())
        self.parts[0].set_frequency(440.0)
        self.parts[1].set_frequency(700.0)

    def set_input(self, input_sample: np.float32):
        pass

    def get_sample(self):
        sample: np.float32 = 0.0
        for part in self.parts:
            sample += part.get_sample()
        sample *= 1/len(self.parts)
        return sample

    def get_buffer(self):
        pass

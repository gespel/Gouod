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
        sample *= 1 / len(self.parts)
        return sample

    def get_buffer(self):
        pass


class StrangeOne(Module):
    def __init__(self):
        self.parts.append(SquareSynth())
        self.parts.append(SineSynth())
        self.parts.append(SineSynth())
        self.parts.append(SineSynth())

        self.parts[1].set_frequency(6)
        self.parts[2].set_frequency(2)
        self.parts[3].set_frequency(1)

    def set_input(self, input_sample: np.float32):
        pass

    def get_sample(self):
        sample: np.float32 = 0.0
        sample += self.parts[0].get_sample()*0.5
        self.parts[0].set_frequency(abs(self.parts[1].get_sample()) * 440)
        self.parts[1].set_frequency(abs(self.parts[2].get_sample()) * 2)
        self.parts[2].set_frequency(self.parts[3].get_sample() * 3)

        return sample

    def get_buffer(self):
        pass

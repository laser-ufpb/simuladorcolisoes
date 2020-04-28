import numpy as np

class Drone(object):
    def __init__(self, num_steps):
        self.num_steps = num_steps
        self.x = np.zeros((num_steps + 1,))
        self.y = np.zeros((num_steps + 1,))
        self.z = np.zeros((num_steps + 1,))
        self.tipo = 0
        self.ativo = True


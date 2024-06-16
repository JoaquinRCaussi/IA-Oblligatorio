import numpy as np
from pendulum_env_extended import PendulumEnvExtended


class Pend_Model():
    def __init__(self, env, x_quantity, y_quantity, vel_quantity, action_quantity):
        self.env = env
        self.x_space = np.linspace(-1, 1, x_quantity)
        self.y_space = np.linspace(-1, 1, y_quantity)
        self.vel_space = np.linspace(-8, 8, vel_quantity)
        self.actions = list(np.linspace(-2, 2, action_quantity))
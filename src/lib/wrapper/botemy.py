import lib.utils.gui as gui

import numpy as np
import gymnasium as gym
from gymnasium import spaces

N_DISCRETE_ACTIONS = 4

HIGH = 255
SHAPE = (3, gui.GAME_HEIGHT, gui.GAME_WIDTH)

def get_reward():
    reward = 0

    try:
        with open('reward.npy', 'rb') as f:
            reward = np.load(f)
    except:
        reward = get_reward()

    return reward

class BotemyEnv(gym.Env):
    metadata = {"render_modes": [""]}

    def __init__(self, max_steps, region):
        super().__init__()
        self.curr_step = 0
        self.max_steps = max_steps
        self.terminated = False

        self.region = region

        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(
            low=0, high=HIGH, dtype=np.uint8, shape=SHAPE
        )

    def is_done(self):
        return self.terminated

    def step(self, action):
        with open('action.npy', 'wb') as f:
            np.save(f, action)

        observation = gui.get_obs(self.region)

        reward = get_reward()

        self.curr_step += 1

        terminated = False
        info = {}
        truncated = False

        if self.curr_step >= self.max_steps:
            truncated = True

        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        gui.close_app()
        gui.open_app()
        gui.play_game()
        gui.close_chat()
        gui.click_api()
        gui.start_connection()
        gui.close_menu()

        observation = gui.get_obs(self.region)
        print(observation.shape)
        info = {}

        self.curr_step = 0
        return observation, info

    def render(self):
        print('render')

    def close(self):
        print('close')

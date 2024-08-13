import time

from lib.wrapper.botemy import BotemyEnv
from lib.utils.gui import get_region
from stable_baselines3 import DQN

from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.callbacks import CheckpointCallback

MODEL_PATH = "./models"
MODEL_LOAD_PATH = "./models/rl_model_1600_steps.zip"
TENSORBOARD_LOG = "./tensorboard/"

N_STEPS = 200
N_EPOCHS = 30
SAVE_FREQ = 200
TOTAL_TIMESTEPS = N_STEPS * N_EPOCHS
MAX_ENV_STEPS = N_STEPS
BUFFER_SIZE = 1000

class CustomCallback(BaseCallback):
    def __init__(self, verbose: int = 0):
        super().__init__(verbose)

    def _on_step(self) -> bool:
        time.sleep(1)

        return super()._on_step()

checkpoint_callback = CheckpointCallback(
    save_freq=SAVE_FREQ,
    save_path="./models/",
    name_prefix="dqn_cnn_model",
    save_replay_buffer=True,
    save_vecnormalize=True,
)

region = get_region()

callback = CustomCallback()
env = BotemyEnv(MAX_ENV_STEPS, region)

model = DQN("CnnPolicy", env=env, verbose=1, tensorboard_log=TENSORBOARD_LOG, buffer_size=BUFFER_SIZE)
# model = PPO.load(MODEL_LOAD_PATH, env=env, verbose=1, n_steps=N_STEPS, n_epochs=N_EPOCHS, tensorboard_log=TENSORBOARD_LOG)

model.learn(TOTAL_TIMESTEPS, callback=[callback, checkpoint_callback], progress_bar=True)
model.save("dqn")

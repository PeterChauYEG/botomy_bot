from lib.wrapper.botemy import BotemyEnv
from lib.inference import inference
from lib.utils.gui import get_region

from stable_baselines3 import DQN

MODEL_LOAD_PATH = "/Users/peterchau/botemy_bot/models/dqn_model_5000_steps.zip"
MAX_ENV_STEPS = 1000
TOTAL_INFERENCE_STEPS = 1000

region = get_region()
env = BotemyEnv(MAX_ENV_STEPS, region)

# model = PPO("MlpPolicy", env, verbose=1)
model = DQN.load(MODEL_LOAD_PATH, env=env, verbose=1)

top_score = inference(env, model, TOTAL_INFERENCE_STEPS)
print(f"Top score: {top_score}")

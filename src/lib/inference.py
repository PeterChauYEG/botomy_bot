import numpy as np
import time

def inference(env, model, total_steps):
    top_score = 0

    obs, info = env.reset()

    for i in range(total_steps):
        action, _states = model.predict(obs,  deterministic=True)

        obs, rewards, terminated, truncated, info = env.step(action)
        top_score = max(top_score, rewards)

        if terminated or truncated:
            obs, info = env.reset()

    return top_score

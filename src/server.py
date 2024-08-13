from fastapi import FastAPI, Request
import numpy as np

app = FastAPI()

def get_action():
    action = -1

    try:
        with open('action.npy', 'rb') as f:
            action = np.load(f)
    except:
        action = get_action()

    return action

@app.post("/")
async def root(request: Request):
    data = await request.json()

    reward = data["own_player"]["score"]

    with open('reward.npy', 'wb') as f:
        np.save(f, reward)

    mapped_action = []

    action = get_action()

    with open('action.npy', 'wb') as f:
        np.save(f, -1)

    if action == -1:
        return mapped_action

    if action == 0:
        mapped_action.append("move_left")
    elif action == 1:
        mapped_action.append("move_up")
    elif action == 2:
        mapped_action.append("move_right")
    elif action == 3:
        mapped_action.append("move_down")

    return mapped_action

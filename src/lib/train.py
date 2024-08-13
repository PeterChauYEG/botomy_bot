def train(model, total_train_steps):
    model.learn(total_timesteps=total_train_steps)

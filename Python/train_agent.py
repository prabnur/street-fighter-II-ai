from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

import gym
import numpy as np
import json

from models import vanilla, convex, concave, less_layer, lstm
import gym_sf2
# 16 relu sigmoid vanilla is DEFAULT
# CONFIGURE HERE
title = "Basic_7_ReLU"
neuron_count = 7
activation = 'relu'
final_activation = 'sigmoid'
function = 'vanilla'

nb_steps = 10000


print('Making Gym')
winrate = ''
average_rewards = []
hp_differences = []
statistics = {}

with gym.make('sf2-v0') as env:
    # nb_actions = env.action_space.n
    nb_actions = 10
    nb_obs = 11
    print("Gym initialized")

    print("making model")
    model = vanilla(neuron_count, activation, final_activation)
    # model.build((None, 11))
    print(model.summary())

    agent = DQNAgent(
        model=model,
        nb_actions=nb_actions,
        memory=SequentialMemory(limit=50000, window_length=1),
        nb_steps_warmup=50,
        target_model_update=13-2, # 11?
        policy=BoltzmannQPolicy()
    )
    agent.compile(Adam(lr=1e-3), metrics=['mae'])
    agent.fit(env, nb_steps=nb_steps) 
    agent.save_weights(f'Python/weights/{title}.hdf5', overwrite=True)

    # Get evaluation statistics
    statistics = {
        'title': title,
        'neuron_count' : neuron_count,
        'activation' : activation,
        'final_activation' : final_activation,
        'function' : function,
        'winrate': f'{round(env.wins / (env.wins + env.losses) * 100)} %',
        'average_rewards' : env.average_rewards,
        'hp_differences' : env.hp_differences
    }

if statistics:
    with open(f'Python/stats/{title}.txt', 'w') as outfile:
        json.dump(statistics, outfile)

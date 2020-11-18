# from tensorflow.keras import Input, Model
# from tensorflow.keras.layers import Dense
# import numpy as np

# from tensorflow.keras.layers import Dense, Concatenate, Reshape
# from tensorflow.keras.optimizers import Adam 
# from tensorflow.keras.backend import reshape
# from tensorflow import convert_to_tensor

# from rl.agents.dqn import DQNAgent
# from rl.policy import BoltzmannQPolicy
# from rl.memory import SequentialMemory

# # from sf2arena import Sf2Env
# import gym
# import gym_sf2

# inputs = Input(shape=(11,))
# x = Dense(16, activation='relu')(inputs)
# x = Dense(13, activation='relu')(x)
# x = Dense(10, activation='relu')(x)
# movements = Dense(4, activation='relu')(x[:4])
# actions = Dense(6, activation='sigmoid')(x[4:])
# outputs = Concatenate(axis=1)([movements, actions])
# model = Model(inputs=inputs, outputs=outputs)

import json
statistics = {
    'title': 'test',
    'neuron_count' : 16,
    'activation' : 'relu',
    'final_activation' : 'sigmoid',
    'function' : 'EZPZ',
    'winrate': 'PLUS ULTRQA',
    'average_rewards' : [1,1,1],
    'hp_differences' : [0,0,0]
  }
if statistics:
    with open(f'Python/stats/test.txt', 'w') as outfile:
        json.dump(statistics, outfile)
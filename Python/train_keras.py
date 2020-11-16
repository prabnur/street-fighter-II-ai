import gym
import gym_sf2
# from keras.models import Sequential
# from keras.layers import Dense, Activation, Flatten
# from keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
# from rl.policy import BoltzmannQPolicy
# from rl.memory import SequentialMemory

# from rl.agents import DQNAgent

print("Making Gym")
env = gym.make('sf2-v0')
agent = DQNAgent(env.action_space)
agent.fit(env, nb_steps=10000) # This function hasa bunch of options we can play with
# See https://keras-rl.readthedocs.io/en/latest/agents/overview/#fit for all of them
# Also returns a keras.callbacks.History that records its training
agent.save_weights('weights.hdf5', overwrite=True) 
# we can save agents with different weights in different files and see how they do in arcade
import gym
import gym_sf2

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten
from tensorflow.keras.optimizers import Adam

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

# from rl.agents import DQNAgent

print("Making Gym")
env = gym.make('sf2-v0')
# nb_actions = env.action_space.n
nb_actions = 10
print("Gym initialized")
shape = (1,)
for key in env.observation_space:
    shape += env.observation_space[key].shape

print("making model")
model = Sequential()
model.add(Flatten(input_shape=shape))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))
model.add(Dense(nb_actions))
model.add(Activation('linear'))
print(model.summary())

print("makin memory and policy")
memory = SequentialMemory(limit=50000, window_length=1)
policy = BoltzmannQPolicy()

agent = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10, target_model_update=13-2, policy=policy)
agent.compile(Adam(lr=1e-3), metrics=['mae'])
agent.fit(env, nb_steps=10000) # This function hasa bunch of options we can play with
# See https://keras-rl.readthedocs.io/en/latest/agents/overview/#fit for all of them
# Also returns a keras.callbacks.History that records its training
agent.save_weights('weights.hdf5', overwrite=True) 
# we can save agents with different weights in different files and see how they do in arcade
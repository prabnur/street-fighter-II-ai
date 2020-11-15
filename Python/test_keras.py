import gym
import gym_sf2
# from keras.models import Sequential
# from keras.layers import Dense, Activation, Flatten
# from keras.optimizers import Adam

# from rl.agents.dqn import DQNAgent
# from rl.policy import BoltzmannQPolicy
# from rl.memory import SequentialMemory

# from rl.agents import DQNAgent

print("hello2!")
env = gym.make('sf2-v0')
# nb_actions = env.action_space.n
# print("hello!")
while True:
    env.step(env.action_space.sample())
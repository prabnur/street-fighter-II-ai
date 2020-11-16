from rl.agents.dqn import DQNAgent
import gym
import gym_sf2

with gym.make('sf2-v0') as env:
  agent = DQNAgent(env.action_space)
  agent.load_weights('weights.hdf5')

# Make it play a game

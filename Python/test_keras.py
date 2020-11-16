from rl.agents.dqn import DQNAgent

env = gym.make('sf2-v0')
agent = DQNAgent(env.action_space)
agent.load_weights('weights.hdf5')

# Make it play a game

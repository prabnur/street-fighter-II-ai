import gym
import numpy as np
from gym import spaces

class CustomEnv(gym.Env):

    metadata = {'render.modes': []}

    # reward is ((our health - enemy health) / max health)
    reward_range = (0, 1)
    spec = None

    action_space = None
    observation_space = None
    
    # not sure about the arg1 or arg2, will need to change
    def __init__(self, arg1, arg2):
        super(CustomEnv, self).__init__()

        # action space is whether or not the button is pressed
        # it's binary so there are 2 possible values (true or false)
        self.action_space = spaces.Tuple((
            spaces.Discrete(2), # UP
            spaces.Discrete(2), # DOWN
            spaces.Discrete(2), # LEFT
            spaces.Discrete(2), # RIGHT
            spaces.Discrete(2), # Y
            spaces.Discrete(2), # X
            spaces.Discrete(2), # L
            spaces.Discrete(2), # B
            spaces.Discrete(2), # A
            spaces.Discrete(2), # R
        ))

        self.observation_space = spaces.Tuple((
           spaces.Discrete(177), # our health [0, 176]
           spaces.Discrete(177), # enemy health [0, 176]
           spaces.Discrete(3), # 1 is standing, 2 is crouch, 3 is jumping
           spaces.Discrete(2), # 0 is not attacking, 1 is attacking
           spaces.Discrete(4), # 0 is punch, 2 is kick (from the lua) - not sure about not attacking and grab
           spaces.Discrete(2), # whether or not there's a projectile
           spaces.Discrete(385), # distance between two players in pixels [0, 385] (need to confirm)
           spaces.Box(np.array([0,99])) # time remaining in the round
        ))

    def step(self, action):
        # execute one time step within environment
        
        # call keras
        # get action back
        # send to socket server
        pass

    def reset(self):
        # reset environment state to initial state
        pass

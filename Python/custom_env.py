import gym
import numpy as np
from gym import spaces

class CustomEnv(gym.Env):

    metadata = {'render.modes': []}

    reward_range = (0, 1)
    reward = 0
    spec = None
    max_health = 176

    action_space = None
    observation_space = None
    
    # not sure about the arg1 or arg2, will need to change
    def __init__(self, arg1, arg2):
        super(CustomEnv, self).__init__()

        # action space is whether or not the button is pressed
        # it's binary so there are 2 possible values (true or false)
        self.action_space = spaces.MultiDiscrete([
            2, # None, Up - NOOP[0], Pressed[1]
            2, # None, Right - NOOP[0], Pressed[1]
            2, # None, Down - NOOP[0], Pressed[1]
            2, # None, Left - NOOP[0], Pressed[1]
            2, # None, A - NOOP[0], Pressed[1]
            2, # None, B - NOOP[0], Pressed[1]
            2, # None, X - NOOP[0], Pressed[1]
            2, # None, Y - NOOP[0], Pressed[1]
            2, # None, L - NOOP[0], Pressed[1]
            2, # None, R - NOOP[0], Pressed[1]
        ])

        self.observation_space = spaces.Dict({
            "self_health":spaces.Box(0, self.max_health, (1,)), 
            "opp_health":spaces.Box(0, self.max_health, (1,)),
            "opp_attacking":spaces.Discrete(2),
            "opp_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "opp_stance":spaces.Discrete(3), # standing, crouching, jumping
            "opp_projectile":spaces.Discrete(2),
            "distance":spaces.Box(0, 187, (1,)), # [0, 187]
            "timer":spaces.Box(0, 152, (1,)),
            "game_finished":spaces.Discrete(2),
        })

    def reward(self):
        # reward is ((our health - enemy health) / max health)
        self.reward = (self.observation_space["self_health"] - self.observation_space["opp_health"]) / self.max_health

    def step(self, action):
        # have to tell lua that its reset if the game is done
        done = False
        if self.observation_space["game_finished"] == 0:
            done = True 
        
        return self.observation_space, self.reward(), done

    def reset(self):
        # reset observation to initial state

        self.observation_space = spaces.Dict({
            "self_health":spaces.Box(0, self.max_health, (1,)), 
            "opp_health":spaces.Box(0, self.max_health, (1,)),
            "opp_attacking":spaces.Discrete(2),
            "opp_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "opp_stance":spaces.Discrete(3), # standing, crouching, jumping
            "opp_projectile":spaces.Discrete(2),
            "distance":spaces.Box(0, 187, (1,)), # [0, 187]
            "timer":spaces.Box(0, 152, (1,)),
            "game_finished":spaces.Discrete(2),
        })

        return self.observation_space

test = CustomEnv(None, None)

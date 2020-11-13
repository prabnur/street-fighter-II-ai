import gym
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
            [0, 4], # None, Up, Right, Down, Left
            [0, 6], # None, A, B, X, Y, L, R
        ])

        self.observation_space = spaces.Dict({
            "self_health":spaces.Box(0, self.max_health, (1,)), 
            "opp_health":spaces.Box(0, self.max_health, (1,)),
            "opp_attacking":spaces.Discrete(2),
            "opp_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "opp_stance":spaces.Discrete(3), # standing, crouching, jumping
            "opp_projectile":spaces.Discrete(2),
            "distance":spaces.Box(0, 385, (1,)), # the game is 385 pixels wide but not sure if this is correct
            "timer":spaces.Box(0, 152, (1,)), # not sure why its 152 when the timer is 99 seconds
        })

    def reward(self):
        # reward is ((our health - enemy health) / max health)
        reward = (self.observation_space["self_health"] - self.observation_space["opp_health"]) / self.max_health

    def step(self, action):
        done = False 
        """ not sure how to check the value from spaces.Box
        if(self.observation_space["self_health"] == 0 || 
           self.observation_space["opp_health"] == 0 ||
           self.observation_space["timer"] == 0):
            done = True
        """
        return observation_space, reward(self), done

    def reset(self):
        # reset observation to initial state
        # is this how to reset it?
        self.observation_space = spaces.Dict({
            "self_health":spaces.Box(0, self.max_health, (1,)), 
            "opp_health":spaces.Box(0, self.max_health, (1,)),
            "opp_attacking":spaces.Discrete(2),
            "opp_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "opp_stance":spaces.Discrete(3), # standing, crouching, jumping
            "opp_projectile":spaces.Discrete(2),
            "distance":spaces.Box(0, 385, (1,)), # the game is 385 pixels wide but not sure if this is correct
            "timer":spaces.Box(0, 152, (1,)), # not sure why its 152 when the timer is 99 seconds
        })

        return observation_space
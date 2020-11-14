import gym
import json
import numpy as np
import socket
from gym import spaces

class CustomEnv(gym.Env):

    metadata = {'render.modes': []}

    reward_range = (0, 1)
    reward = 0
    spec = None
    max_health = 176

    action_space = None
    observation_space = None

    s = None
    c = None
    addr = None
    
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

        # TESTING
        self.s = socket.socket()
        self.s.bind(("127.0.0.1", 8080))
        self.s.listen(5)

        self.c, self.addr = self.s.accept()
        # this is to keep the instance going, but normally keras would
        # be the one to infinitely call the step function
        while True:
            self.step("test")

    def reward(self):
        # reward is ((our health - enemy health) / max health)
        self.reward = (self.observation_space["self_health"] - self.observation_space["opp_health"]) / self.max_health

    def step(self, action):
        # have to tell lua that its reset if the game is done
        # done = False
        # if self.observation_space["game_finished"] == 0:
        #     done = True 
        msg_from_lua = str(self.c.recv(1024).decode('utf-8'))
        from_lua = json.loads(msg_from_lua)
        print("from lua", from_lua) # debug output
        command = {}
        command['message'] = "test"
        command['type'] = "processing" # temp
        if from_lua['time'] <= 130:
            command['type'] = "reset" # temp
        print("dumping", json.dumps(command).encode('utf-8'))
        self.c.sendall(json.dumps(command).encode('utf-8')) # To Emulator
        
        # return self.observation_space, self.reward(), done

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

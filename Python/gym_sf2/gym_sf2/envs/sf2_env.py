import gym
import json
import numpy as np
import socket
from gym import spaces

class Sf2Env(gym.Env):

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
    # def __init__(self, arg1, arg2):
    def __init__(self):
        super(Sf2Env, self).__init__()
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
            "p1_hp":spaces.Discrete(self.max_health+1), # [0, 176]
            "p2_hp":spaces.Discrete(self.max_health+1), # [0, 176]
            "p2_attacking":spaces.Discrete(2),
            "p2_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "p2_stance":spaces.Discrete(3), # 0 standing, 1 crouching, 2 air
            "p2_projectile":spaces.Discrete(2),
            "distance":spaces.Discrete(188), # [0, 187]
            "time":spaces.Discrete(153), # [0, 152]
            "p1_x":spaces.Discrete(260),
            "p2_x":spaces.Discrete(260)
        })

        # TESTING
        self.s = socket.socket()
        self.s.bind(("127.0.0.1", 8080))
        self.s.listen(5)
        self.c, self.addr = self.s.accept()
        print("Gym created and Socket Server set up")
    
    def close(self):
        self.s.close()

    def parse_observation(self, from_lua):
        del from_lua['game_start']
        obs = []
        for key in from_lua:
            obs.append(from_lua[key])
        return obs

    def step(self, action):
        print("step")

        # Get an observation
        msg_from_lua = ''
        from_lua = {}
        while from_lua == {}:
            try:
                msg_from_lua = str(self.c.recv(1024).decode('utf-8'))
                msg_from_lua = msg_from_lua[:msg_from_lua.index("}")+1]
                print(msg_from_lua)
                from_lua = json.loads(msg_from_lua)
                print("from lua", from_lua) # debug output
            except:
                pass
        print("action", action)
        command = {}
        command['type'] = "processing" # temp
        keys = ['Up', 'Right', 'Down', 'Left', 'A', 'B', 'X', 'Y', 'L', 'R']
        key_dict = {}
        for i in range(len(keys)):
            if i == action:
                key_dict[keys[i]] = 1
            else:
                key_dict[keys[i]] = 0
            # key_dict[keys[i]] = str(action[i])
        command['input'] = key_dict
        done = from_lua["game_start"] == 0
        if done:
            command['type'] = "reset" # temp
        print("dumping", json.dumps(command).encode('utf-8'))
        self.c.sendall(json.dumps(command).encode('utf-8')) # To Emulator

        # obs['opp_stance'] = int(obs['opp_stance']) - 1
        obs = self.parse_observation(from_lua)

        # reward is ((our health - enemy health) / max health)
        self.reward = (from_lua["p1_hp"] - from_lua["p2_hp"]) / self.max_health

        return obs, self.reward, done, {} # last thing should be info

    def reset(self):
        # reset observation to initial state (not sure)
        self.reward = 0
        # Get an observation
        msg_from_lua = str(self.c.recv(1024).decode('utf-8'))
        obs = self.parse_observation(json.loads(msg_from_lua))
        print("from lua", obs) # debug output
        return obs

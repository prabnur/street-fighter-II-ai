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
        print("hello!")

    def step(self, action):
        print("step")

        done = False 

        msg_from_lua = str(self.c.recv(1024).decode('utf-8'))
        from_lua = json.loads(msg_from_lua)
        print("from lua", from_lua) # debug output

        if from_lua["game_start"] == 0:
            done = True

        print("from lua", from_lua) # debug output
        print("action", action)
        command = {}
        command['type'] = "processing" # temp
        keys = ['Up', 'Right', 'Down', 'Left', 'A', 'B', 'X', 'Y', 'L', 'R']
        key_dict = {}
        for i in range(len(keys)):
            key_dict[keys[i]] = str(action[i])
        command['input'] = key_dict
        if from_lua['time'] <= 130:
            command['type'] = "reset" # temp
        print("dumping", json.dumps(command).encode('utf-8'))

        # reward is ((our health - enemy health) / max health)
        self.reward = (from_lua["p1_hp"] - from_lua["p2_hp"]) / self.max_health

        obs = {
            "self_health":from_lua["p1_hp"], 
            "opp_health":from_lua["p2_hp"],
            "opp_attacking":from_lua["p2_attacking"],
            "opp_attack_type":from_lua["p2_attack_type"], 
            "opp_stance":from_lua["p2_crouch"], 
            "opp_projectile":from_lua["p2_fireball"],
            "distance":from_lua["distance"],
            "timer":from_lua["time"],
        }

        self.c.sendall(json.dumps(command).encode('utf-8')) # To Emulator

        return obs, self.reward, done

    def reset(self):
        # reset observation to initial state (not sure)
        self.reward = 0
        return None
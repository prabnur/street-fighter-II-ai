from socketserver import ThreadingTCPServer
from handler import EmuTCPHandler, RunServer
from gym import Env, spaces

class Sf2Env(Env):
    metadata = {'render.modes': []}
    reward_range = (0, 1)
    reward = 0
    max_health = 176

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
            "self_health":spaces.Discrete(self.max_health+1), # [0, 176]
            "opp_health":spaces.Discrete(self.max_health+1), # [0, 176]
            "opp_attacking":spaces.Discrete(2),
            "opp_attack_type":spaces.Discrete(4), # punch, kick, grab, no attack
            "opp_stance":spaces.Discrete(3), # standing, crouching, jumping
            "opp_projectile":spaces.Discrete(2),
            "distance":spaces.Discrete(188), # [0, 187]
            "timer":spaces.Discrete(153), # [0, 152]
            "game_finished":spaces.Discrete(2),
        })

        self.next_action = {}
        self.next_observation = {}

        self.server = ThreadingTCPServer(('127.0.0.1', 8080), EmuTCPHandler)
        self.server.env = self # Allows the server to access next_action and write to next_observation
        self.runserver = RunServer(self.server)
        self.runserver.start()
        self.runserver.join()

    def step(self, action):
        print("step")
        self.next_action = action
        self.server.handle_request() # Updates next_observation
        # reward is ((our health - enemy health) / max health)
        self.reward = (self.next_observation["p1_hp"] - self.next_observation["p2_hp"]) / self.max_health

        done = self.next_observation["game_start"] == 0

        return self.next_observation, self.reward, done

    def reset(self):
        # reset observation to initial state (not sure)
        self.reward = 0
        return None
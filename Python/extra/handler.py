import json
from socketserver import BaseRequestHandler
from multiprocessing import Process

class EmuTCPHandler(BaseRequestHandler):
    def handle(self):
        action = self.server.env.next_action

        msg_from_lua = str(self.request.recv(1024).decode('utf-8'))
        from_lua = json.loads(msg_from_lua)
        print("from lua", from_lua) # debug output
        print("action", action)

        # TO:DO Fix opp_stance
        if from_lua:
            self.server.env.next_observation = {
                "self_health":from_lua["p1_hp"], 
                "opp_health":from_lua["p2_hp"],
                "opp_attacking":from_lua["p2_attacking"],
                "opp_attack_type":from_lua["p2_attack_type"], 
                "opp_stance":from_lua["p2_crouch"], 
                "opp_projectile":from_lua["p2_fireball"],
                "distance":from_lua["distance"],
                "timer":from_lua["time"],
            }
        if action.any:
            command = {}
            command['type'] = "processing" # temp
            keys = ['Up', 'Right', 'Down', 'Left', 'A', 'B', 'X', 'Y', 'L', 'R']
            command['input'] = {}
            for i in range(len(keys)):
                command['input'][keys[i]] = str(action[i])
            if from_lua['time'] <= 130:
                command['type'] = "reset" # temp
            print("dumping", json.dumps(command).encode('utf-8'))
            self.request.sendall(json.dumps(command).encode('utf-8')) # To Emulator

class RunServer(Process):
    def __init__(self, server): 
        super(Process, self).__init__() 
        self.server = server
    def run(self):
        server.serve_forever()

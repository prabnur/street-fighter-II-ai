# Following code is courtesy of Adam Fletcher and Jonathan Mortensen
import json
import socketserver
from server_interface import interface

class EmuTCPHandler(socketserver.BaseRequestHandler):    
    def handle(self):
        # while True: Not sure if we need this since we are serving forever

        # self.request is the TCP socket connected to the client
        # receive bytes of size 1024
        msg_from_lua = str(self.request.recv(1024).decode('utf-8'))
        new_observation = json.loads(msg_from_lua)
        interface.next_observation = new_observation
        print(new_observation) # debug output

        command = {}
        # If the emulator isn't started, load a save state
        # and reset the current state
        if not interface.game_started:
            command['type'] = 'reset'
            self.request.sendall(json.dumps(command).encode('utf-8'))
        
        # If we're currently waiting on the AI, tell the emulator
        # to pause for a bit
        elif interface.state == 'processing':
            command['type'] = 'processing'
            self.request.sendall(json.dumps(command).encode('utf-8'))
        
        # Send the AI's action (button presses) to the emulator
        elif interface.state == 'send_actions':
            command['type'] = 'buttons'
            command['p1'] = interface.p1_buttons
            # command['p2'] = interface.p2_buttons
            # wait on the threads to signal the buttons are set
            self.server.ec.e.wait()
            self.request.sendall(json.dumps(command).encode('utf-8'))
        
        # # deal with parsed json here
        # command = {}
        # command['message'] = "test"
        # command['type'] = "processing" # temp
        # # this resets once the round timer reduces to a certain amount, this flag
        # # obviously needs to be changed
        # if from_lua['time'] <= 130:
        #     command['type'] = "reset" # temp
        # self.request.sendall(json.dumps(command).encode('utf-8')) # To Emulator

# Following code is courtesy of Adam Fletcher and Jonathan Mortensen
import json
import socketserver

server_address = '127.0.0.1'
port = 8080

class EmuTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            # self.request is the TCP socket connected to the client
            # receive bytes of size 1024
            msg_from_lua = str(self.request.recv(1024).decode('utf-8'))
            from_lua = json.loads(msg_from_lua)
            print(from_lua) # debug output
            # deal with parsed json here
            command = {}
            command['message'] = "test"
            command['type'] = "processing" # temp
            # this resets once the round timer reduces to a certain amount, this flag
            # obviously needs to be changed
            if from_lua['time'] <= 130:
                command['type'] = "reset" # temp
            self.request.sendall(json.dumps(command).encode('utf-8')) # To Emulator

            # command = {}
            # # If the emulator isn't started, load a save state
            # # and reset the current state
            # if not self.server.ec.emulator_started:
            #     command['type'] = 'reset'
            #     self.request.sendall(json.dumps(command).encode('utf-8'))
            
            # # If we're currently waiting on the AI, tell the emulator
            # # to pause for a bit
            # elif self.server.ec.state == 'processing':
            #     command['type'] = 'processing'
            #     self.request.sendall(json.dumps(command).encode('utf-8'))
            
            # # Send the AI's action (button presses) to the emulator
            # elif self.server.ec.state == 'send_buttons':
            #     command['type'] = 'buttons'
            #     command['p1'] = self.server.ec.p1_buttons
            #     command['p2'] = self.server.ec.p2_buttons
            #     # wait on the threads to signal the buttons are set
            #     self.server.ec.e.wait()
            #     self.request.sendall(json.dumps(command).encode('utf-8'))

# ThreadingServer is asynchronous
with socketserver.ThreadingTCPServer((server_address, port), EmuTCPHandler) as server:
    # server.handle_request() # Handle One
    server.serve_forever() # Handle requests until an explicit server.shutdown()
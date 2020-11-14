from socket_server import EmuTCPHandler
import socketserver

class ServerInterface(object):
  def __init__(self):
    self.next_observation = {'index': -1}
    self.next_action = {'index': -1}
    self.game_started = False

  def reset():
    next_observation = {'index': -1}
    next_action = {'index': -1}

  def serve():
    with socketserver.ThreadingTCPServer(('127.0.0.1', 8080), EmuTCPHandler) as server:
      # server.handle_request() # Handle One
      server.serve_forever() # Handle requests until an explicit server.shutdown()

interface = ServerInterface()  
interface.serve()

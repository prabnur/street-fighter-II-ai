# from sf2arena import Sf2Env
import gym
import gym_sf2
from sf2arena import Sf2Env
# from sf2_env import Sf2Env

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation, Flatten
max_health = 176
with gym.make('sf2-v0') as env:
# with Sf2Env() as env:
  print('Env created')
  obs = env.reset()
  print(obs)

# obs_space = gym.spaces.Dict({
#   "self_health":gym.spaces.Box(0, max_health, (1,)), 
#   "opp_health":gym.spaces.Box(0, max_health, (1,)),
#   "opp_attacking":gym.spaces.Discrete(2),
#   "opp_attack_type":gym.spaces.Discrete(4), # punch, kick, grab, no attack
#   "opp_stance":gym.spaces.Discrete(3), # standing, crouching, jumping
#   "opp_projectile":gym.spaces.Discrete(2),
#   "distance":gym.spaces.Box(0, 187, (1,)), # [0, 187]
#   "timer":gym.spaces.Box(0, 152, (1,)),
#   "game_finished":gym.spaces.Discrete(2),
# })

# # model = Sequential()
# shape = (1,)
# for key in obs_space:
#   print(f'Shape {key}: ', obs_space[key].shape)
#   shape += obs_space[key].shape
# print(shape)
# # model.add(Flatten(input_shape=(1,) + env.observation_space.shape))

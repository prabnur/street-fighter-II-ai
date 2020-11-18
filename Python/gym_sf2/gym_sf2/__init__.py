from gym.envs.registration import register

register(
    id='sf2-v0',
    entry_point='gym_sf2.envs:Sf2Env',
)
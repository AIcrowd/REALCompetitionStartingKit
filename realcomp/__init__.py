from gym.envs.registration import register
 
register(id='REALComp-v0', 
    entry_point='realcomp.envs:REALCompEnv', 
)
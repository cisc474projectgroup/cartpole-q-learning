from gym.envs.registration import register

register(
	id = 'cartpole-v474',
	entry_point = 'env.cartpole_474:CartPoleEnv'
)

import gym 
env = gym.make('CartPole-v0')
env.reset()
for i_eps in range(20):
    obs = env.reset()
    for t in range(100):
        env.render()
        print(obs)
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action) #take a random action
        if done: 
            print("Episode finished after {} timesteps.".format(t+1))
            break
env.close()
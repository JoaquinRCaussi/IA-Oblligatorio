import numpy as np
import wandb

class Agent():
    def __init__(self, env, Qtable, gamma, alpha, epsilon, policy_func):
        self.env = env
        self.gamma = gamma
        self.Qtable = Qtable
        self.alpha = alpha
        self.epsilon = epsilon
        self.policy_func = policy_func
        self.state = env.reset()
        
        

    def get_action(self, state):
        return self.policy_func(state, self.Qtable, self.epsilon)
        
    def train(self, num_k_episodes=1000):
        for i in range(num_k_episodes):
            obs,_ = self.env.reset()
            print(obs)
            done = False
            total_reward = 0
            step_count = 0
            while not done:
                state = obs
                action = self.get_action(state)
                obs, reward, done, _, _ = self.env.step(action)
                self.Qtable[state, action] += self.alpha * (reward + self.gamma * np.max(self.Qtable[obs]) - self.Qtable[state, action]) ##Q-Learning
                total_reward += reward
                step_count += 1
                print('->', state, action, reward, obs, done)
                self.env.render()
            print("Episode finished: reward={0}, steps={1}".format(total_reward, step_count))
            if i % 2 == 0:
                wandb.log({'reward': total_reward})
                
    def play(self, num_l_episodes=100):
        for _ in range(num_l_episodes):
            obs,_ = self.env.reset()
            total_reward = 0
            step_count = 0
            done = False
            while not done:
                state = obs
                action = np.argmax(self.Qtable[state])
                obs, reward, done,_,_ = self.env.step(action)
                total_reward += reward
                step_count += 1
                self.env.render()
            print("Episode finished: reward={0}, steps={1}".format(total_reward, step_count))
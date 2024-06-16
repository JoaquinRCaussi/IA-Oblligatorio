import numpy as np
import wandb
from pendulum_env_extended import PendulumEnvExtended
import random
from tqdm import tqdm

class PendAgent():
    def __init__(self, Pend_Model, alpha, gamma):
        self.Pend_Model = Pend_Model
        self.Qtable = np.zeros((len(Pend_Model.x_space) +1, len(Pend_Model.y_space) +1, len(Pend_Model.vel_space) + 1, len(Pend_Model.actions)))
        self.alpha = alpha
        self.gamma = gamma
    
    def get_sample_action(self):
        return random.choice(self.Pend_Model.actions)
    
    def epsilon_greedy_policy(self, state, Q, epsilon=0.1):
        explore = np.random.binomial(1, epsilon)
        if explore:
            action = self.get_sample_action()
        # exploit
        else:
            action = self.optimal_policy(state, Q)
        return action

    def optimal_policy(self, state, Q):
        action = self.Pend_Model.actions[np.argmax(Q[state])]
        return action

    def get_state(self, obs):
        x, y, vel = obs
        x_bin = np.digitize(x, self.Pend_Model.x_space)
        y_bin = np.digitize(y, self.Pend_Model.y_space)
        vel_bin = np.digitize(vel, self.Pend_Model.vel_space)
        return x_bin, y_bin, vel_bin


    def train(self,num_k_episodes, epsilon):
        all_rewards = []
        for i in tqdm(range(num_k_episodes)):
            obs,_ = self.Pend_Model.env.reset()
            done = False

            total_reward = 0
            state = self.get_state(obs)
            while not done:

                # Acción del modelo
                action = self.epsilon_greedy_policy(state, self.Qtable, epsilon)

                # Indice de la accion en Q
                action_idx = self.Pend_Model.actions.index(action)

                # Acción del ambiente
                real_action = np.array([action])

                obs, reward, done, _, _ = self.Pend_Model.env.step(real_action)
                ## Hacer Q-learning Checkear si esto esta bien
                next_state = self.get_state(obs)

                self.Qtable[state][action_idx] = self.Qtable[state][action_idx] + self.alpha * (reward + self.gamma * np.max(self.Qtable[next_state]) - self.Qtable[state][action_idx])
            
                state = next_state
            # Usar action_idx para actualizar Q
                total_reward += reward
                self.Pend_Model.env.render()
            all_rewards.append(total_reward)
            if i % 10 == 0:
                wandb.log({'reward': total_reward, 'episodes' : i})
        return np.mean(all_rewards)

    def play(self, num_l_episodes):
        all_rewards = []
        for _ in range(num_l_episodes):
            obs,_ = self.Pend_Model.env.reset()
            total_reward = 0
            done = False
            state = self.get_state(obs)
            while not done:
                action = self.optimal_policy(state, self.Qtable)
                action_idx = self.Pend_Model.actions.index(action)
                real_action = np.array([action])
                obs, reward, done, _, _ = self.Pend_Model.env.step(real_action)
                state = self.get_state(obs)
                total_reward += reward
                self.Pend_Model.env.render()
            all_rewards.append(total_reward)
        return np.mean(all_rewards)
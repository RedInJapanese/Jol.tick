import torch
import numpy as np
import dqn as d
import replay_buffer as rb
import torch.optim as optim
import random 

class DQNAgent:
    def __init__(self, input_size, num_actions, buffer_capacity=10000, batch_size=32, gamma=0.99, lr=0.001):
        self.num_actions = num_actions
        self.batch_size = batch_size
        self.gamma = gamma
        
        self.memory = rb.ReplayBuffer(buffer_capacity)
        self.q_network = d.DQN(input_size, num_actions)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=lr)
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
    
    def act(self, state):
        if np.random.rand() < self.epsilon:
            return random.randrange(self.num_actions)
        q_values = self.q_network(torch.FloatTensor(state))
        return q_values.argmax().item()
    
    def train(self):
        if len(self.memory) < self.batch_size:
            return
        
        batch = self.memory.sample(self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        
        states = torch.FloatTensor(states)
        actions = torch.LongTensor(actions)
        rewards = torch.FloatTensor(rewards)
        next_states = torch.FloatTensor(next_states)
        dones = torch.FloatTensor(dones)
        
        # Q-value for the current state-action pair
        current_q_values = self.q_network(states).gather(1, actions.unsqueeze(1)).squeeze(1)
        
        # Compute target Q-values for the next state
        next_q_values = self.q_network(next_states).max(1)[0]
        target_q_values = rewards + self.gamma * next_q_values * (1 - dones)
        
        loss = (current_q_values - target_q_values.detach()).pow(2).mean()
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        # Decay epsilon
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

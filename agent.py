import pygame
from random import randint
from sprites import Sprites
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque

MAX_MEMORY = 10000

class AIPlayer(Sprites):

    def __init__(self, pos_x, pos_y, player_path, current_sprite, run_speed):
        super().__init__(pos_x, pos_y, player_path, current_sprite, run_speed)
        self.is_jumping = False
        self.jump_vel = 8.5
        self.jump_sprites = []
        self.jump_sprites.append(pygame.image.load('sprites/ai_player/jump/image_8.png'))
        self.jump_sprites.append(pygame.image.load('sprites/ai_player/jump/image_9.png'))

    #####################
    # Parâmetros da IA #
    ###################

        self.n_games = 0
        self.epsilon = 1.0
        self.gamma = 0
        self.learning_rate = 0.001
        self.memory = deque(maxlen=MAX_MEMORY)
        self.state_size = 5
        self.action_size = 2
        self.q_network = QNetwork(self.state_size, self.action_size)
        self.optimizer = optim.Adam(self.q_network.parameters(), lr=self.learning_rate)
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01

    def jump(self):
        if self.is_jumping:
            self.image = self.jump_sprites[0]
            self.rect.y -= self.jump_vel * 2.5
            self.jump_vel -= 0.45

        if self.jump_vel <= 0:
            self.image = self.jump_sprites[1]

        if self.jump_vel < -8.5:
            self.rect.y = 500
            self.is_jumping = False
            self.jump_vel = 8.5


        
       


    def make_decision(self):
        if self.rect.y < 400: 
            return 1  # Pular
        else:
            return 0  # Não fazer nada

    #altura do obstaculo
    #comprimento do obstaculo
    #distancia do obstaculo
    #altura da ia
    #comprimento da ia


    def select_action(self, state):
        if torch.rand(1).item() < self.epsilon:
            return randint(0, self.action_size - 1)  # Explorar
        else:
            with torch.no_grad():
                action = self.q_network(state)
                return action.argmax().item()  # Explorar

    def learn(self, state, action, reward, next_state, done):
        q_values = self.q_network(state)
        next_q_values = self.q_network(next_state)
        max_next_q_value = next_q_values.max().unsqueeze(0)
        target_q_value = torch.tensor(reward) + self.gamma * max_next_q_value * torch.tensor(1)
        
        loss = nn.MSELoss()(q_values[action], target_q_value)
        
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.epsilon_decay

class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, 64)    
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)

    def forward(self, state):
        x = torch.relu(self.fc1(state))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

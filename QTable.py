import numpy as np
import random

class QTable:
    def __init__(self, ambient_size, actions):
        self.q_table = np.zeros((ambient_size[0], ambient_size[1], actions))

    # Atualização da tabela-Q usando a equação de Bellman
    def update(self, state, action, reward, next_state, alpha, gamma):
        self.q_table[state[0], state[1], action] = (1 - alpha) * self.q_table[state[0], state[1], action] + alpha * (reward + gamma * np.max(self.q_table[next_state[0], next_state[1]]))

    def choose_action(self, state, epsilon, actions):
        if random.uniform(0, 1) < epsilon:
            return random.randint(0, actions - 1)  # Escolhe uma ação aleatória
        else:
            return np.argmax(self.q_table[state[0], state[1]])



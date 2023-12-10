import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time


class Environment:
    def __init__(self, ambient_size, obstacles_points, delivery_points):
        self.ambient_size = ambient_size
        self.obstacles_points = obstacles_points
        self.delivery_points = delivery_points
        self.agent_position = (0, 0)
        self.maze = np.zeros(ambient_size)

        for obstacles in obstacles_points:
            self.maze[obstacles] = 1

        for delivery in delivery_points:
            self.maze[delivery] = 2

        # Configuração inicial do gráfico
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, self.ambient_size[0])
        self.ax.set_ylim(0, self.ambient_size[1])

        # Adicione obstáculos ao gráfico
        for obstacle in self.obstacles_points:
            rect = patches.Rectangle(obstacle, 1, 1, linewidth=1, edgecolor='r', facecolor='r')
            self.ax.add_patch(rect)

        # Adicione pontos de entrega ao gráfico
        for delivery_point in self.delivery_points:
            rect = patches.Rectangle(delivery_point, 1, 1, linewidth=1, edgecolor='g', facecolor='g')
            self.ax.add_patch(rect)

    def is_valid_move(self, move):
        x, y = self.agent_position
        new_x, new_y = x + move[0], y + move[1]
        return 0 <= new_x < self.ambient_size[0] and 0 <= new_y < self.ambient_size[1] and (new_x, new_y) not in self.obstacles_points

    def take_action(self, action):
        # Simulação de movimento do agente
        if action == 0 and self.is_valid_move((-1, 0)): # Movimento pra cima
            self.agent_position = (self.agent_position[0] - 1, self.agent_position[1])
        elif action == 1 and self.is_valid_move((1, 0)): # Movimento pra baixo
            self.agent_position = (self.agent_position[0] + 1, self.agent_position[1])
        elif action == 2 and self.is_valid_move((0, -1)): # Movimento pra esquerda
            self.agent_position = (self.agent_position[0], self.agent_position[1] - 1)
        elif action == 3 and self.is_valid_move((0, 1)): # Movimento pra direita
            self.agent_position = (self.agent_position[0], self.agent_position[1] + 1)

        reward = -1  # Living penalty
        if self.agent_position in self.delivery_points:
            reward += 10  # Recompensa por encontrar o delivery_point

        return self.agent_position, reward
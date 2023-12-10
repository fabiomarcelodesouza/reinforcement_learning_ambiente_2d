import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

class Environment:
    """
    Classe que representa o ambiente para um problema de entrega.

    Attributes:
        ambient_size (tuple): Tamanho do ambiente, representado como (largura, altura).
        obstacles_points (list): Lista de coordenadas dos pontos de obstáculos no ambiente.
        delivery_points (list): Lista de coordenadas dos pontos de entrega no ambiente.
        agent_position (tuple): Posição atual do agente no ambiente.
        maze (numpy.ndarray): Matriz representando o ambiente com obstáculos (1) e pontos de entrega (2).
        fig (matplotlib.figure.Figure): Objeto de figura para visualização gráfica do ambiente.
        ax (matplotlib.axes._subplots.AxesSubplot): Eixo para visualização gráfica do ambiente.

    Methods:
        __init__(ambient_size, obstacles_points, delivery_points): Inicializa o ambiente com o tamanho, obstáculos e pontos de entrega dados.
        is_valid_move(move): Verifica se um movimento é válido no ambiente.
        take_action(action): Realiza uma ação no ambiente, simulando o movimento do agente e fornecendo uma recompensa.
    """

    def __init__(self, ambient_size, obstacles_points, delivery_points):
        """
        Inicializa o ambiente com o tamanho, obstáculos e pontos de entrega dados.

        Parameters:
            ambient_size (tuple): Tamanho do ambiente, representado como (largura, altura).
            obstacles_points (list): Lista de coordenadas dos pontos de obstáculos no ambiente.
            delivery_points (list): Lista de coordenadas dos pontos de entrega no ambiente.
        """
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
        """
        Verifica se um movimento é válido no ambiente.

        Parameters:
            move (tuple): Movimento a ser verificado, representado como (dx, dy).

        Returns:
            True se o movimento for válido, False caso contrário.
        """
        x, y = self.agent_position
        new_x, new_y = x + move[0], y + move[1]
        return 0 <= new_x < self.ambient_size[0] and 0 <= new_y < self.ambient_size[1] and (new_x, new_y) not in self.obstacles_points

    def take_action(self, action):
        """
        Realiza uma ação no ambiente, simulando o movimento do agente e fornecendo uma recompensa.

        Parameters:
            action (int): Ação a ser realizada pelo agente.

        Returns:
            agent_position (tuple): Nova posição do agente após a ação.
            reward (int): Recompensa associada à ação.
        """
        # Simulação de movimento do agente
        if action == 0 and self.is_valid_move((-1, 0)):  # Movimento para cima
            self.agent_position = (self.agent_position[0] - 1, self.agent_position[1])
        elif action == 1 and self.is_valid_move((1, 0)):  # Movimento para baixo
            self.agent_position = (self.agent_position[0] + 1, self.agent_position[1])
        elif action == 2 and self.is_valid_move((0, -1)):  # Movimento para a esquerda
            self.agent_position = (self.agent_position[0], self.agent_position[1] - 1)
        elif action == 3 and self.is_valid_move((0, 1)):  # Movimento para a direita
            self.agent_position = (self.agent_position[0], self.agent_position[1] + 1)

        reward = -1  # Penalidade por estar vivo
        if self.agent_position in self.delivery_points:
            reward += 10  # Recompensa por encontrar o ponto de entrega

        return self.agent_position, reward

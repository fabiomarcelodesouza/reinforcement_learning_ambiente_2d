import numpy as np
import random

class QTable:
    """
    Classe que representa uma tabela Q para aprendizado por reforço.

    Attributes:
        q_table (numpy.ndarray): Tabela Q que armazena os valores Q para cada estado e ação.

    Methods:
        __init__(ambient_size, actions): Inicializa a tabela Q com base no tamanho do ambiente e no número de ações disponíveis.
        update(state, action, reward, next_state, alpha, gamma): Atualiza a tabela Q usando a equação de Bellman.
        choose_action(state, epsilon, actions): Escolhe uma ação com base no estado atual usando uma política epsilon-greedy.
    """

    def __init__(self, ambient_size, actions):
        """
        Inicializa a tabela Q com base no tamanho do ambiente e no número de ações disponíveis.

        Parameters:
            ambient_size (tuple): Tamanho do ambiente, representado como (largura, altura).
            actions (int): Número de ações disponíveis.
        """
        self.q_table = np.zeros((ambient_size[0], ambient_size[1], actions))

    def update(self, state, action, reward, next_state, alpha, gamma):
        """
        Atualiza a tabela Q usando a equação de Bellman.

        Parameters:
            state (tuple): Estado atual, representado como (x, y).
            action (int): Ação realizada no estado atual.
            reward (float): Recompensa recebida pela ação.
            next_state (tuple): Próximo estado resultante da ação, representado como (x, y).
            alpha (float): Taxa de aprendizado.
            gamma (float): Fator de desconto para recompensas futuras.
        """
        self.q_table[state[0], state[1], action] = (1 - alpha) * self.q_table[state[0], state[1], action] + alpha * (reward + gamma * np.max(self.q_table[next_state[0], next_state[1]]))

    def choose_action(self, state, epsilon, actions):
        """
        Escolhe uma ação com base no estado atual usando uma política epsilon-greedy.

        Parameters:
            state (tuple): Estado atual, representado como (x, y).
            epsilon (float): Parâmetro de exploração para a política epsilon-greedy.
            actions (int): Número de ações disponíveis.

        Returns:
            Ação escolhida.
        """
        if random.uniform(0, 1) < epsilon:
            return random.randint(0, actions - 1)  # Escolhe uma ação aleatória
        else:
            return np.argmax(self.q_table[state[0], state[1]])
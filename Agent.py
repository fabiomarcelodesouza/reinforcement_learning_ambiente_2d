from QTable import QTable

class Agent:
    """
    Classe que representa um agente para aprendizado por reforço.

    Attributes:
        q_table (QTable): Tabela Q utilizada pelo agente para tomar decisões.

    Methods:
        __init__(ambient_size, actions): Inicializa um agente com uma tabela Q baseada no tamanho do ambiente e nas ações disponíveis.
        learn(state, action, reward, next_state, alpha, gamma): Atualiza a tabela Q do agente com informações sobre a transição de estado.
        choose_action(state, epsilon, actions): Escolhe uma ação com base no estado atual, usando a tabela Q do agente e uma política epsilon-greedy.
    """

    def __init__(self, ambient_size, actions):
        """
        Inicializa um agente com uma tabela Q.

        Parameters:
            ambient_size (int): Tamanho do ambiente.
            actions (list): Lista de ações disponíveis para o agente.
        """
        self.q_table = QTable(ambient_size, actions)

    def learn(self, state, action, reward, next_state, alpha, gamma):
        """
        Atualiza a tabela Q do agente com informações sobre a transição de estado.

        Parameters:
            state: Estado atual.
            action: Ação realizada no estado atual.
            reward: Recompensa recebida pela ação.
            next_state: Próximo estado resultante da ação.
            alpha (float): Taxa de aprendizado.
            gamma (float): Fator de desconto para recompensas futuras.
        """
        self.q_table.update(state, action, reward, next_state, alpha, gamma)

    def choose_action(self, state, epsilon, actions):
        """
        Escolhe uma ação com base no estado atual, usando a tabela Q do agente e uma política epsilon-greedy.

        Parameters:
            state: Estado atual.
            epsilon (float): Parâmetro de exploração para a política epsilon-greedy.
            actions (list): Lista de ações disponíveis para o agente.

        Returns:
            Ação escolhida.
        """
        return self.q_table.choose_action(state, epsilon, actions)
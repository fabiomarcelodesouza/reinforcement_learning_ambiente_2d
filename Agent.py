from QTable import QTable


class Agent:
    def __init__(self, ambient_size, actions):
        self.q_table = QTable(ambient_size, actions)

    def learn(self, state, action, reward, next_state, alpha, gamma):
        self.q_table.update(state, action, reward, next_state, alpha, gamma)

    def choose_action(self, state, epsilon, actions):
        return self.q_table.choose_action(state, epsilon, actions)

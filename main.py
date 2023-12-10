# main.py

import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from Enviroment import Environment
from Agent import Agent

# Limpar a tela do console
os.system('cls')

# Definição do ambiente, agente e parâmetros de treinamento

# Ponto de partida do agente
start_position = (0, 0)

# Tamanho do ambiente
ambient_size = (20, 20)

# Localização dos obstáculos
obstacles_points = [(1, 1), (2, 2), (19, 19), (12, 11)]

# Localização dos pontos de entrega
delivery_points = [(4, 4), (19, 18), (15, 15)]

# Número de ações possíveis
actions = 4

# Número de episódios de treinamento
qtde_episodios = 100

# Listas para armazenar informações sobre o agente
path = []    # Lista de posições do agente durante o treinamento
titulo = []  # Lista de títulos associados a cada estado do agente

# Criação do ambiente
env = Environment(ambient_size=ambient_size, obstacles_points=obstacles_points, delivery_points=delivery_points)

# Criação do agente
agent = Agent(ambient_size=ambient_size, actions=actions)

# Parâmetros de treinamento
alpha = 0.1   # Taxa de aprendizado
gamma = 0.9   # Fator de desconto
epsilon = 0.1 # Taxa de exploração

# Função de treinamento do agente
def train():
    state = (0, 0)
    total_reward = 0
    epoca = 0 

    while state not in delivery_points:        
        action = agent.choose_action(state, epsilon, actions)
        next_state, reward = env.take_action(action)

        agent.learn(state, action, reward, next_state, alpha, gamma)
        total_reward += reward
        state = next_state  # Atualização do estado
        path.append(state)  # Adiciona o estado à lista de posições do agente
        tit = f"Episódio {episodio + 1}, Estado: {epoca}, Recompensa: {total_reward}"
        titulo.append(tit)
        print(tit)
        epoca = epoca + 1

    return total_reward

# Loop de treinamento
for episodio in range(qtde_episodios):
    print(f"Episódio {episodio + 1}, Recompensa Total: {train()}")

# Função para atualizar o gráfico da animação
def update(frame):
    ax.cla()
    ax.matshow(env.maze, cmap=plt.cm.Accent)

    if frame < len(path):
        state = path[frame]
        ax.plot(state[1], state[0], 'bo', markersize=11, label="Agente")
        ax.set_title(titulo[frame])

# Preparação da representação gráfica do labirinto
fig, ax = plt.subplots()

# Configurações de plotagem
ax.set_xticks([])
ax.set_yticks([])

# Criação da animação
ani = FuncAnimation(fig, update, frames=len(path), repeat=False)
print(path)
plt.show()
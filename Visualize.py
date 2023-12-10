import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Enviroment as env

class Animation:
    # Função para atualizar o gráfico da animação
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_yticks([])
        self.ax.set_xticks([])

    # Função para atualizar o gráfico da animação
    def update(self, frame, path):
        self.ax.cla()
        self.ax.matshow(env.maze)

        if frame < len(path):
            state = path[frame]
            self.ax.plot(state[1], state[0], 'bo', markersize=5, label="Agente")
            self.ax.set_title(f"Época {frame + 1}")

    def show(self, path):
        ani = FuncAnimation(self.fig, self.update, frames=len(path), repeat=False)
        plt.show()
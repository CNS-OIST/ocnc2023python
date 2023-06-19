import numpy as np
import matplotlib.pyplot as plt

X_LIM = (-1, 1)
Y_LIM = (-1, 1)

class Ant:
    speed = 0.5

    def __init__(self):
        self.x = 0
        self.y = 0
    
    def move(self, dt):
        self.x += np.random.normal(scale=self.speed * dt)
        self.y += np.random.normal(scale=self.speed * dt)


class Simulation:

    def __init__(self, nb_ants):
        self.ants = [Ant() for i in range(nb_ants)]

    def plot(self, t):
        plt.clf()
        plt.scatter(
            [ant.x for ant in self.ants],
            [ant.y for ant in self.ants],
            color='brown'
        )
        plt.xlim(X_LIM)
        plt.ylim(Y_LIM)
        plt.title(f'{t = :.3f}')
        plt.pause(0.01)

    def run(self, end_time, dt=0.05):
        plt.figure()
        for t in np.arange(0, end_time, dt):
            self.plot(t)
            for ant in self.ants:
                ant.move(dt)

# Run the simulation
sim = Simulation(150)
sim.run(10)
plt.show()

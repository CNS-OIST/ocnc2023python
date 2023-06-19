import numpy as np
import matplotlib.pyplot as plt

X_LIM = (-1, 1)
Y_LIM = (-1, 1)

# TODO
# Implement an Ant class that defines:
#     - x and y attributes, initialized to 0
#     - a move(dt) method that uses np.random.normal() to modify the position of the ant

class Simulation:

    def __init__(self, nb_ants):
        # TODO
        # Initialize the list of ants as an attribute
        self.ants = []

    def plot(self, t):
        plt.clf()
        # TODO
        # Use plt.scatter to plot the position of the ants
        plt.xlim(X_LIM)
        plt.ylim(Y_LIM)
        plt.title(f'{t = :.3f}')
        plt.pause(0.01)

    def run(self, end_time, dt=0.05):
        plt.figure()
        for t in np.arange(0, end_time, dt):
            self.plot(t)
            # TODO
            # Call the move(dt) method for all ants

# Run the simulation
sim = Simulation(150)
sim.run(10)
plt.show()

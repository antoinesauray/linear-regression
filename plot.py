import matplotlib.pyplot as plt
import numpy as np
import hypothesis

def compare(x, Y, X, Theta, xlabel, ylabel):
    # we use scatter
    # with a marker size of 10
    plt.scatter(x,Y, s=10)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.plot(x, hypothesis.compute(Theta, X))
    plt.show()

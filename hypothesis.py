import numpy
"""
    This file calculates the hypothesis of our vector x based on our theta vector
    which contains our parameters

"""
def compute(Theta, X):
    return numpy.dot(X, Theta)

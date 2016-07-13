import hypothesis
import numpy

def compute(Theta, X, Y):
    return (numpy.sum(numpy.square(hypothesis.compute(Theta, X) - Y)))/(2*len(Y))

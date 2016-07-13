import numpy
import hypothesis

def predict(theta, x):
    return hypothesis.compute(theta, [1,x])

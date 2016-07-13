import numpy
import hypothesis
import cost

def compute(Theta, X, Y, alpha, iterations):
    m = len(Y)
    J_history = []
    xTrans = numpy.transpose(X)
    for i in range(iterations):
        H = hypothesis.compute(Theta, X)
        loss = H - Y
        #costOfTheta = cost.compute(Theta, X, Y)
        gradient = numpy.dot(xTrans, loss) / m
        Theta = Theta - alpha * gradient
    return Theta

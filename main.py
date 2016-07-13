import numpy
import scipy
import cost
data = numpy.loadtxt(open("./ex1data1.txt","rb"),delimiter=",")

# test hypothesis
m = len(data)
print 'm=',m

# features
# first is X0 (always is equals 1)
# second is surface in squared meters

# append a column of one to our features
X = numpy.c_[numpy.ones(m), data[:,0]]
Y = numpy.c_[data[:,1]]
Theta = numpy.zeros((2,1))
#print type(Theta)
#print Theta.shape
#print type(X)
#print X.shape
#print type(Y)
#print Y.shape

cost = cost.compute(Theta, X, Y)
print "cost without training: ",cost

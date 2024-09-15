# simulated annealing search of a one-dimensional objective function
# This code is from Jason Brownlee's site “Machine Learning Mastery”,
# but it was adapted
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot


# objective function
def objective(x):
    #return x[0]**2.0
    return  x1+x2**2/(x1*x2-1)

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # generate an initial point
    x_cb = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    Jx_cb = objective(x_cb)
    # current working solution
    current, Jcurrent = x_cb, Jx_cb
    scores = list()
    # run the algorithm
    for i in range(n_iterations):
        # calculate temperature for current epoch
        t = temp / float(i + 1)
        # perturb x
        x_per = current + randn(len(bounds)) * step_size
        # evaluate x_per 
        Jx_per = objective(x_per)
        # check for new x_cb solution
        if Jx_per < Jx_cb:
            # store new x_cb point
            x_cb, Jx_cb = x_per, Jx_per
            # keep track of scores
            scores.append(Jx_cb)
            # report progress
            print('>%d f(%s) = %.5f' % (i, x_cb, Jx_cb))
        # difference between x_per and current point evaluation
        diff = Jx_per - Jcurrent
        # check if we should keep the new point
        if diff < 0 or rand() < exp(-diff / t):
            # store the new current point
            current, Jcurrent = x_per, Jx_per
    return [x_cb, Jx_cb, scores]

# define range for input
bounds = asarray([[-5.0, 5.0]])
# define the total iterations
n_iterations = 1000
# define the maximum step size
step_size = 0.1
# initial temperature
temp = 10
# perform the simulated annealing search
x_cb, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Done!')
print('f(%s) = %f' % (x_cb, score))
# line plot of x_cb scores
pyplot.plot(scores, '.-')
pyplot.xlabel('Improvement')
pyplot.ylabel('J(x)')
pyplot.show()
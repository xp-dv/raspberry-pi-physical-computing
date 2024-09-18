import numpy
from scipy.integrate import odeint
from matplotlib import pyplot

def plot(dydx, initial_y, initial_x = 0, end_x = 10, resolution = 100, x_label = 'x', y_label = 'y'):
  domain = numpy.linspace(initial_x, end_x, resolution)
  y = odeint(dydx, initial_y, domain)
  figure = pyplot.figure()
  pyplot.plot(domain, y)
  pyplot.title('Solution Plot')
  pyplot.xlabel(x_label)
  pyplot.ylabel(y_label)

  figure.savefig(f'./ode_solution_plot.png', dpi=figure.dpi)
  pyplot.show()

from computeXYZ_numpy import *
import matplotlib.pyplot as plotter

def varf(f_X, f_Y):
    '''Generates a Lissajous figure (XY plot) with given f_X and f_Y and
    preset values for other variables.'''
    (t, X, Y, Z) = calctXYZ(f_X, f_Y, 1, 2, 0.5, 0.001, 1000)
    plotter.plot(X, Y)
    plotter.xlabel('X')
    plotter.ylabel('Y')
    plotter.show()

def varphi(phi):
    '''Generates a Lissajous figure (XY plot) with given list of phi
    values and preset values for other variables.'''
    plotter.xlabel('X')
    plotter.ylabel('Y')
    for phi_i in phi:
        (t, X, Y, Z) = calctXYZ(1, 1, 1, 2, phi_i, 0.001, 1000)
        plotter.plot(X, Y, label=str(phi_i/np.pi) + 'pi')
    plotter.legend()
    plotter.show()

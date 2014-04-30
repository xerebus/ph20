import numpy as np
import matplotlib.pyplot as plotter

def is_python_or_numpy_int(N):
    '''Returns true if N is an integer or a numpy array of integers.'''

    int_types = [int, np.int8, np.int16, np.int32, np.int64]

    for i in int_types:
        if type(N) is i:
            return True
    return False

def trap(func, a, b, N):
    '''Integrates func(x) from a to b using the trapezoid method with N
    subintervals.'''

    if not is_python_or_numpy_int(N):
        raise TypeError('N is %s, must be an int or array of ints' % type(N))

    h = float(b - a) / float(N)

    # where to evaluate func
    ix = a + (h * np.arange(1, N)) # interior points
    ex = a + (h * np.array([0, N])) # exterior points

    # evaluate function at relevant points
    vfunc = np.vectorize(func) # version accepting array of x
    fval_ix = vfunc(ix)
    fval_ex = vfunc(ex)

    # sum function values
    sum_ix = np.sum(fval_ix)
    sum_ex = np.sum(fval_ex)

    # trapezoidal formula
    I = h * (sum_ix + (sum_ex / 2))

    return I

def simps(func, a, b, N):
    '''Integrates func(x) from a to b using the Simpson method with N
    subintervals.'''

    if not is_python_or_numpy_int(N):
        raise TypeError('N is %s, must be an int or array of ints' % type(N))

    h = float(b - a) / float(N)

    # where to evaluate func
    ix = a + (h * np.arange(1, N)) # interior regular points
    mx = a + (h / 2) + (h * np.arange(0, N)) # interior midpoints
    ex = a + (h * np.array([0, N])) # exterior points

    # evaluate function at relevant points
    vfunc = np.vectorize(func) # version accepting array of x
    fval_ix = vfunc(ix)
    fval_mx = vfunc(mx)
    fval_ex = vfunc(ex)

    # sum function values
    sum_ix = np.sum(fval_ix)
    sum_mx = np.sum(fval_mx)
    sum_ex = np.sum(fval_ex)

    # Simpson's formula
    I = (h / 6) * (sum_ex + 4*sum_mx + 2*sum_ix)

    return I

def plot_eff(func, a, b, exact, showplots='both'):
    '''Plots error against exact in integrating func(x) from a to b using
    the trapezoid and Simpson methods. Set showplots to 'both', 'trap', 
    or 'simps' depending on which plots you want to see.'''

    N_arr = np.logspace(1, 5)
    N_arr = N_arr.astype(int)

    # create versions of trap and simps that accept an array of N
    vtrap = np.vectorize(trap, excluded=['func', 'a', 'b'])
    vsimps = np.vectorize(simps, excluded=['func', 'a', 'b'])
    
    # evaluate integrals over all N in N_arr
    trap_val = vtrap(func, a, b, N=N_arr)
    simps_val = vsimps(func, a, b, N=N_arr)

    # get errors
    trap_err = np.abs(trap_val - exact)
    simps_err = np.abs(simps_val - exact)

    if showplots == 'both' or showplots == 'trap':
        plotter.loglog(N_arr, trap_err, color='blue', label='Trapezoidal')
    if showplots == 'both' or showplots == 'simps':
        plotter.loglog(N_arr, simps_err, color='red', label='Simpsons\'s')
    plotter.xlabel('N')
    plotter.ylabel('Error')
    plotter.legend()
    plotter.show()

def simps_ac(func, a, b, ac):
    '''Integrates func(x) from a to b to the desired accuracy, ac, by
    repeating Simpson's method until successive iterations differ by less than
    ac.'''

    # have the initial number of subintervals scale roughly with the size
    # of the interval, but make sure it's at least a sensible size to begin
    # with
    N = 10 + int((b - a) / 5)

    # set initial guess
    I_old = 1

    while True:
        I_new = simps(func, a, b, N)
        if abs((I_new - I_old) / I_old) < ac:
            return I_new
        else:
            N *= 2
            I_old = I_new

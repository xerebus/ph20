import numpy as np
import matplotlib.pyplot as plotter

def explicit_Euler(x_0, v_0, h, s, plot=False, plotname='explicit.eps'):
    '''Given a starting position x_0 and velocity v_0, plots the position x
    and velocity v of a spring over time using the explicit Euler method
    with a step size h from t = 0 to t = s.'''

    x = np.array([x_0])
    v = np.array([v_0])
    t = np.arange(0, s, h)

    for i in xrange(len(t) - 1):
        x = np.append(x, x[i] + h*v[i])
        v = np.append(v, v[i] - h*x[i])

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(t, x, color='blue', label='x')
        plotter.plot(t, v, color='red', label='v')
        plotter.xlabel('t')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

    return (t, x, v)

def analytic(x_0, v_0, h, s, plot=False, plotname='analytic.eps'):
    '''Given a starting position x_0 and velocity v_0, plots the position x
    and velocity v of a spring over time evaluating the analytic ODE solution
    at t = i*h from t = 0 to t = s.'''

    t = np.arange(0, s, h)

    x = v_0 * np.sin(t) + x_0 * np.cos(t)
    v = v_0 * np.cos(t) - x_0 * np.sin(t)

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(t, x, color='blue', label='x')
        plotter.plot(t, v, color='red', label='v')
        plotter.xlabel('t')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

    return (t, x, v)

def implicit_Euler(x_0, v_0, h, s, plot=False, plotname='implicit.eps'):
    '''Given a starting position x_0 and velocity v_0, plots the position x
    and velocity v of a spring over time using the implicit Euler method
    from t = 0 to t = s.'''

    x = np.array([x_0])
    v = np.array([v_0])
    t = np.arange(0, s, h)

    for i in xrange(len(t) - 1):
        x = np.append(x, (x[i] + h*v[i]) / (h**2 + 1))
        v = np.append(v, (v[i] - h*x[i]) / (h**2 + 1))

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(t, x, color='blue', label='x')
        plotter.plot(t, v, color='red', label='v')
        plotter.xlabel('t')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

    return (t, x, v)

def global_error(x_0, v_0, h, s, method_a, method_b, plot=False, plotname=None):
    '''Generates arrays of the global error method_b - method_a for x and v.
    Returns maximum error in x and v.'''

    (t_a, x_a, v_a) = method_a(x_0, v_0, h, s)
    (t_b, x_b, v_b) = method_b(x_0, v_0, h, s)

    x_diff = x_b - x_a
    v_diff = v_b - v_a
    
    assert np.array_equal(t_a, t_b)
    t = t_a

    if plotname is None:
        plotname = '%s_error.eps' % method_a

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(t, x_diff, color='blue', label='x error')
        plotter.plot(t, v_diff, color='red', label='v error')
        plotter.xlabel('t')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

    max_x_error = np.max(np.absolute(x_diff))
    max_v_error = np.max(np.absolute(v_diff))

    return (max_x_error, max_v_error)

def error_vs_h(x_0, v_0, h_0, s, method_a, method_b, plot=False, plotname=None):
    '''Compares global error between method_a and method_b for x and v
    for h ranging from h_0 to h_0/16.'''

    coeff = np.logspace(0, 4, base=2)
    h = h_0 / coeff

    # allow global_error function to take an array of h and s
    global_error_vec = np.vectorize(global_error, excluded=['x_0', 'v_0', \
    's', 'method_a', 'method_b', 'plot'])

    errors = global_error_vec(x_0, v_0, h, s, method_a, method_b)
    x_errors = errors[0]
    v_errors = errors[1]

    if plotname is None:
        plotname = '%s_error_v_h.eps' % method_a

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(h, x_errors, color='blue', label='x error')
        plotter.plot(h, v_errors, color='red', label='v error')
        plotter.xlabel('h')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

def plot_E(x_0, v_0, h, s, method, plotname=None):
    '''Given a spring numerical solution method, plot E(t) = x^2 + v^2.'''

    (t, x, v) = method(x_0, v_0, h, s)
    E = np.power(x, 2) + np.power(v, 2)

    if plotname is None:
        plotname = '%s_E.eps' % method
    
    plotter.figure(figsize=(10, 4))
    plotter.plot(t, E)
    plotter.xlabel('t')
    plotter.ylabel('E')
    plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

def plot_phase(x_0, v_0, h, s, method, plotname=None):
    '''Given a spring numerical solution method, plot v vs. x.'''

    (t, x, v) = method(x_0, v_0, h, s)

    if plotname is None:
        plotname = '%s_xv.eps' % method

    plotter.figure(figsize=(6, 6))
    plotter.plot(x, v)
    plotter.xlabel('x')
    plotter.ylabel('v')
    plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

def symplectic_Euler(x_0, v_0, h, s, plot=False, plotname='symplectic.eps'):
    '''Given a starting position x_0 and velocity v_0, plots the position x
    and velocity v of a spring over time using a simple symplectic Euler method
    from t = 0 to t = s.'''

    x = np.array([x_0])
    v = np.array([v_0])
    t = np.arange(0, s, h)

    for i in xrange(len(t) - 1):
        x = np.append(x, x[i] + h*v[i])
        v = np.append(v, v[i] - h*x[i] - (h**2)*v[i])

    if plot:
        plotter.figure(figsize=(10, 4))
        plotter.plot(t, x, color='blue', label='x')
        plotter.plot(t, v, color='red', label='v')
        plotter.xlabel('t')
        plotter.legend()
        plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

    return (t, x, v)

def plot_symplectic_lag(x_0, v_0, h, s, plotname='symplectic_error.eps'):
    '''Plots x(t) and v(t), with symplectic Euler method in dashed lines, and
    analytic solutions in solid lines.'''

    (t_sym, x_sym, v_sym) = symplectic_Euler(x_0, v_0, h, s)
    (t_act, x_act, v_act) = analytic(x_0, v_0, h, s)

    assert np.array_equal(t_sym, t_act)
    t = t_sym

    plotter.figure(figsize=(10, 4))
    plotter.plot(t, x_sym, color='blue', ls='dashed', label='x, symplectic')
    plotter.plot(t, x_act, color='blue', ls='solid', label='x, analytic')
    plotter.plot(t, v_sym, color='red', ls='dashed', label='v, symplectic')
    plotter.plot(t, v_act, color='red', ls='solid', label='v, analytic')
    plotter.xlabel('t')
    plotter.set_xlim(s - 50, s) # rightmost 50 units to show lag at large t
    plotter.legend()
    plotter.savefig(plotname, format='eps', bbox_inches='tight', pad_inches=0.1)

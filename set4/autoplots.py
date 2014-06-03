import numpy as np
import matplotlib.pyplot as plotter
from spring import *
import sys

# Generate all plots required for set 3 PDF

# EDITABLE VALUES

x_0 = 0
v_0 = 5
h = 0.05
s = 50
h_0_small = 0.01
h_0_big = 0.1

print 'Generating plots...'

if 'explicit' in sys.argv or len(sys.argv) < 2:
    print 'numerical solutions with explicit Euler method'
    explicit_Euler(x_0, v_0, h, s, plot=True, plotname='explicit.eps')

if 'explicit_error' in sys.argv or len(sys.argv) < 2:
    print 'explicit method error'
    global_error(x_0, v_0, h, s, explicit_Euler, analytic, plot=True, plotname='explicit_error.eps')

if 'explicit_error_v_h' in sys.argv or len(sys.argv) < 2:
    print 'explicit method error vs h'
    error_vs_h(x_0, v_0, h_0_big, s, explicit_Euler, analytic, plot=True, plotname='bigh.eps')
    error_vs_h(x_0, v_0, h_0_small, s, explicit_Euler, analytic, plot=True, plotname='smallh.eps')

if 'explicit_E' in sys.argv or len(sys.argv) < 2:
    print 'explicit method energy'
    plot_E(x_0, v_0, h, s, explicit_Euler, log=False, plotname='explicit_E.eps')

if 'explicit_E_log' in sys.argv or len(sys.argv) < 2:
    print 'explicit method energy log plot'
    plot_E(x_0, v_0, h, s, explicit_Euler, log=True, plotname='explicit_E_log.eps')

if 'implicit' in sys.argv or len(sys.argv) < 2:
    print 'numerical solutions with implicit Euler method'
    implicit_Euler(x_0, v_0, h, s, plot=True, plotname='implicit.eps')
    
if 'implicit_error' in sys.argv or len(sys.argv) < 2:
    print 'implicit method error'
    global_error(x_0, v_0, h, s, implicit_Euler, analytic, plot=True, plotname='implicit_error.eps')

if 'implicit_E' in sys.argv or len(sys.argv) < 2:
    print 'implicit method energy'
    plot_E(x_0, v_0, h, s, implicit_Euler, log=False, plotname='implicit_E.eps')

if 'xv' in sys.argv or len(sys.argv) < 2:
    print 'explicit and implicit method phase space plots'
    plot_phase(x_0, v_0, h, s, explicit_Euler, plotname='explicit_xv.eps')
    plot_phase(x_0, v_0, h, s, implicit_Euler, plotname='implicit_xv.eps')

if 'symplectic' in sys.argv or len(sys.argv) < 2:
    print 'numerical solutions with symplectic Euler method'
    symplectic_Euler(x_0, v_0, h, s, plot=True, plotname='symplectic.eps')

if 'combined_xv' in sys.argv or len(sys.argv) < 2:
    print 'symplectic and analytical phase space plot'
    plot_2_phase(x_0, v_0, h, s, symplectic_Euler, analytic, plotname='combined_xv.eps')

if 'symplectic_E' in sys.argv or len(sys.argv) < 2:
    print 'symplectic energy'
    plot_E(x_0, v_0, h, s, symplectic_Euler, log=False, plotname='symplectic_E.eps')

if 'symplectic_error' in sys.argv or len(sys.argv) < 2:
    print 'symplectic error lag'
    plot_symplectic_lag(x_0, v_0, h, 5000, plotname='symplectic_error.eps')
    
print 'Done!'

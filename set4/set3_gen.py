import numpy as np
import matplotlib.pyplot as plotter
from spring import *

# Generate all plots required for set 3 PDF

# EDITABLE VALUES

x_0 = 0
v_0 = 5
h = 0.05
s = 50
h_0_small = 0.01
h_0_big = 0.1

if __name__ == '__main__':
    
    # numerical solutions with explicit Euler method
    explicit_Euler(x_0, v_0, h, s, plot=True, plotname='explicit.eps')
    
    # explicit method error
    global_error(x_0, v_0, h, s, explicit_Euler, analytic, plot=True, plotname='explicit_error.eps')

    # explicit method error vs h
    error_vs_h(x_0, v_0, h_0_big, s, explicit_Euler, analytic, plot=True, plotname='bigh.eps')
    error_vs_h(x_0, v_0, h_0_small, s, explicit_Euler, analytic, plot=True, plotname='smallh.eps')

    # explicit method energy
    plot_E(x_0, v_0, h, s, explicit_Euler, plotname='explicit_E.eps')

    # numerical solutions with implicit Euler method
    implicit_Euler(x_0, v_0, h, s, plot=True, plotname='implicit.eps')
    
    # implicit method error
    global_error(x_0, v_0, h, s, implicit_Euler, analytic, plot=True, plotname='implicit_error.eps')

    # implicit method energy
    plot_E(x_0, v_0, h, s, implicit_Euler, plotname='implicit_E.eps')

    # explicit and implicit method phase space plots
    plot_phase(x_0, v_0, h, s, explicit_Euler, plotname='explicit_xv.eps')
    plot_phase(x_0, v_0, h, s, implicit_Euler, plotname='implicit_xv.eps')

    # numerical solutions with symplectic Euler method
    symplectic_Euler(x_0, v_0, h, s, plot=True, plotname='symplectic.eps')

    # symplectic phase space plot
    plot_phase(x_0, v_0, h, s, symplectic_Euler, plotname='symplectic_xv.eps')

    # symplectic energy
    plot_E(x_0, v_0, h, s, symplectic_Euler, plotname='symplectic_E.eps')

    # symplectic error lag
    plot_symplectic_lag(x_0, v_0, h, 5000, plotname='symplectic_error.eps')
    



    

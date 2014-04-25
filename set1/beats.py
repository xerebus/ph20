from computeXYZ_numpy import *
import matplotlib.pyplot as plotter

# predetermined values
A_X = 1
A_Y = 1
phi = 0.5
dt = 0.001
N = 50000

def plotZ(f_X, f_Y, fourier=False):
    '''Given f_X, f_Y, and predetermined values, plot Z vs. t. If fourier
    variable is True, plot Z(f) vs. f.'''
    (t, X, Y, Z) = calctXYZ(f_X, f_Y, A_X, A_Y, phi, dt, N)
    if fourier:
        assert t.size == N + 1
        f = np.fft.fftfreq(t.size, d=dt) # frequency samples
        Zh = np.fft.fft(Z)
        plotter.plot(f, Zh.real, f, Zh.imag)
        plotter.xlabel('f')
        plotter.ylabel('Zh')
    else:
        plotter.plot(t, Z)
        plotter.xlabel('t')
        plotter.ylabel('Z')
    plotter.show()

import math
import numpy as np
import sys

def usage():
    '''Prints an usage message.'''
    print 'Usage: %s [f_X] [f_Y] [A_X] [A_Y] [phi] [dt] [N]' % sys.argv[0]
    print 'N must be an integer, all other values must be integers or floats'

def calctXYZ(f_X, f_Y, A_X, A_Y, phi, dt, N):
    '''Given relevant constants, evaluates X(t), Y(t), and Z(t) for t = n * dt
    where n = 0, ..., N. Returns t, X, Y, and Z arrays.'''
    n = np.arange(0, N + 1)
    t = n * dt
    X = A_X * np.cos(2 * np.pi * f_X * t)
    Y = A_Y * np.sin((2 * np.pi * f_Y * t) + phi)
    Z = X + Y
    return (t, X, Y, Z)

def writetXYZ(t, X, Y, Z):
    '''Given t, X, Y, and Z arrays, prints CSV output as t,X,Y,Z.'''
    data = np.column_stack((t, X, Y, Z))
    np.savetxt(sys.stdout, data, delimiter=',')

if __name__ == '__main__': 
    try: 
        f_X = float(sys.argv[1])
        f_Y = float(sys.argv[2])
        A_X = float(sys.argv[3])
        A_Y = float(sys.argv[4])
        phi = float(sys.argv[5])
        dt = float(sys.argv[6])
        N = int(sys.argv[7])
        (t, X, Y, Z) = calctXYZ(f_X, f_Y, A_X, A_Y, phi, dt, N)
        writetXYZ(t, X, Y, Z)
    except IndexError, TypeError:
        usage()


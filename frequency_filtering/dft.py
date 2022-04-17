# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
from cmath import pi
import numpy as np
import cmath

class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        up = [5, 7]
        down = [8, 3]
        matrix = np.matrix([up, down])

        local = matrix.copy()
        result = np.zeros(local.shape, dtype= np.complex_)
        complex = 1j
        N = local.shape[0]
        for u in range (0, result.shape[0]):
            for v in range (0, result.shape[1]):
                for i in range (0, local.shape[0]):
                    for j in range (0, local.shape[1]):
                        result[u, v] += local[i, j]*np.exp(-1* complex * ((2*pi)/N) * (u*i + v*j))
        return result

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        local = matrix.copy()
        complex = 1j
        result = np.zeros(local.shape, dtype= np.complex_)
        N = local.shape[0]
        for i in range (0, result.shape[0]):
            for j in range (0, result.shape[1]):
                for u in range (0, local.shape[0]):
                    for v in range (0, local.shape[1]):
                        result[i, j] += local[u, v]*np.exp(complex * ((2*pi)/N) * (u*i + v*j))
        return result

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        local = matrix.copy()
        for num_1 in local:
            for num_2 in num_1:
                temp = cmath.sqrt( (num_2.real)**2 + (num_2.imag)**2 )
                num_2 = temp
        return local
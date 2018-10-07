'''
_cy_p2mesh.pyx in pyP2Mesh

author  : cfeng
created : 10/06/18 5:00PM
'''

cimport cython

from libcpp.vector cimport vector
from libcpp.string cimport string
import numpy as np
cimport numpy as np

#ref: https://stackoverflow.com/a/45928289
np.import_array()

cdef extern from "src/p2mesh.cpp" namespace "p2mesh":
    void find_closest_point_on_mesh(
        const vector[float]& P,
        const vector[float]& V,
        const vector[int]&   F,
        vector[float]& C,
        vector[int]&   I,
        vector[float]& D
    )

@cython.boundscheck(False)
@cython.wraparound(False)
def _cy_p2mesh(
    np.ndarray[np.float32_t, ndim=1]  P,
    np.ndarray[np.float32_t, ndim=1]  V,
    np.ndarray[np.int_t,     ndim=1]  F
    ):
    '''
    Input:
        P <Kx3>: query points
        V <Nx3>: mesh vertices
        F <Mx3>: mesh face indices
    Output:
        C <Kx3>: closest points on mesh
        I <Kx1>: corresponding face indices
        D <Kx1>: squared distances
    '''
    cdef vector[float] C
    cdef vector[int] I
    cdef vector[float] D

    find_closest_point_on_mesh(
        P, V, F,
        C, I, D
    )
    C_ = np.array(C).reshape((3,-1)).transpose()
    I_ = np.array(I)
    D_ = np.array(D)
    return C_, I_, D_

def p2mesh(P, V, F):
    P = P.reshape(-1,order='F').astype(dtype=np.float32) #use F since libigl uses col-major Eigen::MatrixXd
    V = V.reshape(-1,order='F').astype(dtype=np.float32)
    F = F.reshape(-1,order='F').astype(dtype=np.int)
    C, I, D = _cy_p2mesh(P, V, F)
    return C, I, D
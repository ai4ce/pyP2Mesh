'''
demo.py in pyP2Mesh

author  : cfeng
created : 10/6/18 11:45PM
'''

import os
import sys
import argparse

import numpy as np
import p2mesh

#https://stackoverflow.com/a/31133917
def read_off(fname):
    with open(fname) as file:
        if 'OFF' != file.readline().strip():
            raise('Not a valid OFF header')
        n_verts, n_faces, n_dontknow = tuple([int(s) for s in file.readline().strip().split(' ')])
        verts = [[float(s) for s in file.readline().strip().split(' ')] for i_vert in range(n_verts)]
        faces = [[int(s) for s in file.readline().strip().split(' ')][1:] for i_face in range(n_faces)]
        return verts, faces

def write_vtk(fname, V, F, P, C):
    with open(fname, 'w') as out:
        out.write('# vtk DataFile Version 2.0\n')
        out.write('demo\n')
        out.write('ASCII\n')
        out.write('DATASET POLYDATA\n')
        out.write('POINTS {:d} float\n'.format(V.shape[0]+P.shape[0]+C.shape[0]))
        out.write('\n'.join(['{:f} {:f} {:f}'.format(v[0], v[1], v[2]) for v in V])+'\n')
        out.write('\n'.join(['{:f} {:f} {:f}'.format(v[0], v[1], v[2]) for v in P])+'\n')
        out.write('\n'.join(['{:f} {:f} {:f}'.format(v[0], v[1], v[2]) for v in C])+'\n')

        out.write('LINES {:d} {:d}\n'.format(P.shape[0], P.shape[0]*3))
        out.write('\n'.join(['2 {:d} {:d}'.format(i+V.shape[0], i+V.shape[0]+P.shape[0])
                             for i in range(P.shape[0])])+'\n')

        out.write('POLYGONS {:d} {:d}\n'.format(F.shape[0], F.shape[0]*4))
        out.write('\n'.join(['3 {:d} {:d} {:d}'.format(v[0], v[1], v[2]) for v in F]))

def main(args):
    V = np.array(
        [
            [0,0,0],
            [1,0,0],
            [1,0,1],
            [0,0,1],
            [0,1,1],
            [0,1,0],
        ],
        dtype=np.float32
    )
    F = np.array(
        [
            [0,1,2],
            [0,2,3],
            [0,3,4],
            [0,4,5]
        ],
        dtype=np.int
    )
    P = np.array(
        [
            [0,0,0],
            [1,0,0],
            [1,0,1],
            [0,0,1],
            [0,1,1],
            [0,1,0],
            [0.5,0.5,0],
            [0.5,0.5,0.5],
        ],
        dtype=np.float32
    )
    C, I, D=p2mesh.p2mesh(P,V,F)
    print(C)
    print(I)
    print(D)

    #read mesh
    V, F = read_off('data/bunny.off')
    V = np.asarray(V, dtype=np.float32)
    F = np.asarray(F, dtype=np.int)

    #generate query points
    Vmax = V.max(0)
    Vmin = V.min(0)
    mag = np.mean(Vmax-Vmin) * 0.1
    P = np.random.rand(*V.shape).astype(dtype=np.float32) * mag + V

    C, I, D = p2mesh.p2mesh(P, V, F)

    write_vtk('bunny_p2mesh.vtk', V, F, P, C)
    print('done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(sys.argv[0])

    args = parser.parse_args(sys.argv[1:])
    args.script_folder = os.path.dirname(os.path.abspath(__file__))

    main(args)
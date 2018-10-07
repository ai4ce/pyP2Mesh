import os
import glob
import platform
import numpy as np
from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

"""
Run setup with the following command:
```
python setup.py build_ext --inplace
```
"""

# Determine current directory of this setup file to find our module
CUR_DIR = os.path.dirname(__file__)
sys_name = platform.system()
if sys_name == 'Linux':
    libigl_incs = ['/usr/local/include/']

elif sys_name == 'Windows':
    libigl_incs = ['C:/lib/libigl/include']

libigl_incs += [os.path.join(libigl_incs[-1],'..','external','eigen')]

self_incs = [os.path.join(CUR_DIR, 'src')]

if sys_name == 'Linux':
    extensions = [
    Extension('p2mesh._p2mesh',
              sources=[os.path.join(CUR_DIR, '_cy_p2mesh.pyx')],
              language='c++',
              include_dirs=[np.get_include()] + libigl_incs + self_incs,
              extra_compile_args=['-O3', '-w'],
              # extra_link_args=
              )]
elif sys_name == 'Windows':
    extensions = [
    Extension('p2mesh._p2mesh',
              sources=[os.path.join(CUR_DIR, '_cy_p2mesh.pyx')],
              language='c++',
              include_dirs=[np.get_include()] + libigl_incs + self_incs,
              extra_compile_args=['/O2'],
              # extra_link_args=
              )]

setup(
    name="p2mesh._p2mesh",
    version = "0.0.1",
    author = "Chen Feng",
    author_email= "cfeng@nyu.edu",
    description="python wrapper for libigl's igl::point_mesh_squared_distance function",
    # platforms=
    license="BSD",
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(extensions)
)
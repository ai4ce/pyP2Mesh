pyP2Mesh
========

Overview
--------

This is the python3 wrapper for projecting a set of points onto a mesh, using [libigl](https://github.com/libigl/libigl/).

Currently it is tested under Windows10(VC2017, x64), and python3.6 in Anaconda3.

![](https://raw.githubusercontent.com/ai4ce/pyP2Mesh/499dc99c3b583fa3cb8ef5735a74ff2162521734/data/p2mesh.jpg)

Version
-------

0.0.1

Installation
------------

1. prepare your environment:   
```
"C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars64.bat"
```

2. Clone [libigl](https://github.com/libigl/libigl/).

3. Change libigl_incs in setup.py accordingly

2. compile the project:
```
python setup.py build_ext --inplace
```

3. Enjoy!   
```
python demo.py
```
This will generate a bunny_p2mesh.vtk file, which visualizes the projection using vtk file.
VTK file can be viewed using [ParaView](https://www.paraview.org/download/).


Contact
-------

Chen Feng <cfeng at nyu dot edu>

**Feel free to email any bugs or suggestions to help us improve the code. Thank you!**
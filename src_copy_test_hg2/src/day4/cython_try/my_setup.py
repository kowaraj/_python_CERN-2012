from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("c3", 
                         ["c3.pyx"])]

setup(
    name = "Cython-test",
    cmdclass = {'build_ext':build_ext},
    ext_modules = ext_modules)


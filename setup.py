from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize



setup(
    name='levlpy',
        version='0.1.0',
        py_modules=['levlpy'],
    ext_modules = cythonize([
    Extension("levlpy", ["src/levlpy/levlpy.pyx"],
              libraries=["leveldb"])
    ]))
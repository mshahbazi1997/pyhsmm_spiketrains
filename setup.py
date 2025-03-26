from distutils.core import setup
from setuptools.extension import Extension
import numpy as np
from Cython.Build import cythonize

extensions = cythonize([
    Extension(
        name="pyhsmm_spiketrains.internals.poisson_statistics",
        sources=["pyhsmm_spiketrains/internals/poisson_statistics.pyx"],
        include_dirs=[np.get_include()],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"]
    )
])

setup(
    name='pyhsmm_spiketrains',
    ext_modules=extensions,
)
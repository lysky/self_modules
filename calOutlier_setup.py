# -*- coding: utf-8 -*-
"""
Created on Thu Jan 03 21:07:20 2013

@author: corin li
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("outlier", ["outlier.pyx"])]
)
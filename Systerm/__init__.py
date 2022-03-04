"""Systerm is a multipurpose python library"""
import sys
sys.path.append("..")
del sys

# Importing libraries in Systerm
from Systerm.module import Module
from Systerm.module import modules

from Systerm import module
from Systerm import instance
from Systerm import version
from Systerm import console
from Systerm import time
from Systerm import math
from Systerm import exit

from Systerm.version import Version

# SystermMod
@module.add(__name__)
@instance.super(modules[__name__])
class SystermMod(Module):
	"""Module class for Systerm"""
	__version__: version.Version = version

"""Systerm is a multipurpose python library"""

# Adding Systerm to path
import sys
sys.path.append("..")
del sys

# Importing libraries in Systerm
from Systerm.module import Module
from Systerm.module import modules

from Systerm import module
from Systerm import instance

# SystermMod
@module.add(__name__)
@instance.super(modules[__name__])
class SystermMod(Module):
	"""Module class for Systerm"""
	pass

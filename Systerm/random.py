"""This module is a copy of the python's random module"""
import Systerm
import random

# RandomMod
class RandomMod(Systerm.module.Module.super(random)):
	"""Module class for Systerm.random"""

del random
Systerm.module.modules[__name__].__class__ = RandomMod

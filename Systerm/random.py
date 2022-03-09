"""This module is a copy of the python's random module."""
import Systerm
import random

# RandomMod
class RandomMod(Systerm.module.Module.super(random)):
	
	"""Module class for Systerm.random."""
	int = random.randint
	float = random.uniform
	bool = lambda self:self.random() < 0.5
	range = random.randrange
	__call__ = lambda self:self.random()
	randfloat = float
	randbool = bool

del random
Systerm.module.modules[__name__].__class__ = RandomMod

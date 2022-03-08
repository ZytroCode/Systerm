"""Mathematical module for Systerm"""
import Systerm
import math

# MathMod
class MathMod(Systerm.module.Module.super(math)):
	"""Module class for Systerm.math"""

Systerm.module.modules[__name__].__class__ = MathMod

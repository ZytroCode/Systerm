"""Mathematical module for Systerm"""
import Systerm
import math

# MathMod
@Systerm.module.add(__name__)
@Systerm.instance.super(math)
class MathMod(Systerm.Module):
	"""Module class for Systerm.math"""

"""Mathematical module for Systerm."""
import Systerm
import math

# MathMod class
class MathMod(Systerm.module.Module.super(math)):
    pass

Systerm.module.modules[__name__].__class__ = MathMod

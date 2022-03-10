"""A duplicate of the original python's random module."""
import datetime as date
import time

import Systerm

# TimeMod class
class TimeMod(Systerm.module.Module.super(date, time)):
	__call__ = get = lambda self:self.time()

del time
Systerm.module.modules[__name__].__class__ = TimeMod

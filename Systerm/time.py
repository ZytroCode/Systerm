"""This module is a copy of the python's time module"""
import Systerm
import time
import datetime as date

# TimeMod
class TimeMod(Systerm.module.Module.super(date, time)):
	
	"""Module class for Systerm.time"""
	def get(self) -> float:
		"""
		Return the current time in seconds since the Epoch.
		Fractions of a second may be present if the system clock provides them.
		"""
		return self.time()
	
	def __call__(self) -> float:
		"""
		Return the current time in seconds since the Epoch.
		Fractions of a second may be present if the system clock provides them.
		"""
		return self.time()

del time
Systerm.module.modules[__name__].__class__ = TimeMod

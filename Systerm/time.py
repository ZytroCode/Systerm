"""This module is a copy of the python time module"""
import Systerm
import time

# TimeMod
@Systerm.module.add(__name__)
@Systerm.instance.super(time)
class TimeMod(Systerm.Module):
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

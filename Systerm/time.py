"""This module is a copy of the python time module"""
import Systerm
import time

# TimeMod
@Systerm.module.add(__name__)
@Systerm.instance.super(time)
class TimeMod(Systerm.Module):
	"""Module class for Systerm.time"""

del time

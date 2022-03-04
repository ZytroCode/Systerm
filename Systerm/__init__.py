"""Systerm is a multipurpose python library"""
import builtins
import sys
builtins.systerm_installed: bool = False
sys.path.append("..")

# Importing libraries in Systerm
from Systerm.module import Module
from Systerm.module import modules

from Systerm import module
from Systerm import instance
from Systerm import version
from Systerm import console
from Systerm import time
from Systerm import math
from Systerm import exit

from Systerm.version import Version

# SystermMod
@module.add(__name__)
@instance.super(modules[__name__])
class SystermMod(Module):
	"""Module class for Systerm"""
	__version__: version.Version = version
	_old_builtins = {}

	def get_installed(self) -> bool:
		"""Returns True if Systerm is installed in runtime"""
		return builtins.systerm_installed

	def install(self) -> None:
		"""Installing the Systerm module by overriding the python's builtins module"""
		pass
	def uninstall(self) -> None:
		"""Undoing the installation of Systerm"""
		pass

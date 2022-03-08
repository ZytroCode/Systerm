"""Systerm is a multipurpose python library"""
import sys

sys.path.append("..")

# Importing libraries in Systerm
from Systerm import meta
from Systerm import module
from Systerm import version
from Systerm import console
from Systerm import time
from Systerm import math
from Systerm import random
from Systerm import file
from Systerm import exit

from Systerm.meta import Metaclass
from Systerm.meta import ABC
from Systerm.meta import Object
from Systerm.meta import List
from Systerm.meta import Dictionary
from Systerm.meta import abstractmethod
from Systerm.module import Module
from Systerm.module import modules
from Systerm.file import BaseFile
from Systerm.file import File
from Systerm.console import BaseLogger
from Systerm.console import Logger
from Systerm.version import Version

# SystermMod
@module.add(__name__)
@instance.super(modules[__name__])
class SystermMod(Module):
	"""Module class for Systerm"""
	__version__: version.Version = version
	_old_builtins = {}
	_overide_objects = dict(
		print = console.send,
		input = console.scan,
		exit = exit,
		systerm_installed = True
	)

	def get_installed(self) -> bool:
		"""Returns True if Systerm is installed in runtime"""
		return builtins.systerm_installed

	def install(self) -> None:
		"""Installing the Systerm module by overriding the python's builtins module"""
		for index, value in self._overide_objects.items():
			self._old_builtins[index] = getattr(builtins, index)
			setattr(builtins, index, value)
	
	def uninstall(self) -> None:
		"""Undoing the installation of Systerm"""
		for index, value in self._old_builtins.items():
			setattr(builtins, index, value)

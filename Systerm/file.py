"""This module is a copy of the python's shutil module"""
import Systerm
import pathlib
import shutil
import os

from typing import Optional, Union, NewType

# BaseFile class
class BaseFile(metaclass=Systerm.meta.Metaclass):
	
	"""Used for interpreting a file and it's contents"""
	def __init__(self, path: str, mode: Optional[Union[str, type]]="file") -> None:
		def set_mode(mode):
			for name in dir(mode):
				if not name.startswith("_"):
					setattr(self, name, getattr(mode(path), name))
			self.__class__ = mode
		
		if type(mode) != str and issubclass(mode, BaseFile):
			set_mode(mode)
		
		elif mode == "file":
			set_mode(File)
	
	def __enter__(self):
		return self
	
	def __exit__(self, type, value, traceback):
		self.close()
	
	def close(self):
		del self

# File class
class File(BaseFile):

	"""Used for interpreting a file and it's contents in a normal way"""
	def __init__(self, path: str) -> None:
		self.path: str = path
	
	def read(self, encoding: str="UTF-8") -> str:
		with Systerm._old_builtins["open"](self.path, "r", encoding=encoding) as f:
			return f.read()
	
	def write(self, value, encoding: str="UTF-8") -> None:
		with Systerm._old_builtins["open"](self.path, "w", encoding=encoding) as f:
			f.write(value)

# FileMod
class FileMod(Systerm.module.Module.super(shutil, os.path, pathlib)):

	"""Module class for Systerm.file"""

Systerm.module.modules[__name__].__class__ = FileMod

"""Used for managing files and folders."""
from ast import Pass
import os
import pathlib
import shutil
from typing import Optional, Union, NewType

import Systerm

# BaseFile class
class BaseFile(metaclass=Systerm.meta.Metaclass):
	"""Used for interpreting a file and its contents.

	The attributes and methods of this class depends on its parameter mode.
	"""

	def __init__(self, path: str, mode: Optional[Union[str, type]]="file") -> None:
		"""The constructor for the BaseFile class.

		Parameters:
			path - str:			The path of the file
			mode - str | type:	The type of mode to open the file
		"""
		def set_mode(mode):
			for name in dir(mode):
				if not name.startswith("_"):
					setattr(self, name, getattr(mode(path), name))
			self.__class__ = mode

		if type(mode) != str and issubclass(mode, BaseFile):
			set_mode(mode)

		elif mode == "file":
			set_mode(File)

	def __enter__(self) -> None:
		return self

	def __exit__(self, *_) -> None:
		self.close()

	def close(self) -> None:
		"""Deletes itself."""
		del self

# File class
class File(BaseFile):
	"""The normal mode to open a file.

	Attributes:
		path - str:	The path of the file

	Methods:
		read(encoding):			Reads the contents of the file
		write(value, encoding):	Rewrites the contents of the file
	"""
	def __init__(self, path: str) -> None:
		""""The constructor for the File class.

		Parameters:
			path - str: The path of the file
		"""
		self.path: str = path

	def read(self, encoding: Optional[str]="UTF-8") -> str:
		"""Reads the contents of the file.

		Parameters:
			encoding - Optional[str]:	The encoding format to read the file
		"""
		with Systerm._old_builtins["open"](self.path, "r", encoding=encoding) as f:
			return f.read()

	def write(self, value, encoding: str="UTF-8") -> None:
		"""Rewrites the contents of the file.

		Parameters:
			encoding - Optional[str]:	The encoding format to rewrite the file
		"""
		with Systerm._old_builtins["open"](self.path, "w", encoding=encoding) as f:
			f.write(value)

# FileMod class
class FileMod(Systerm.module.Module.super(shutil, os.path, pathlib)):
	pass

Systerm.module.modules[__name__].__class__ = FileMod

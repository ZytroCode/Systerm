"""Console is used for interpreting the stream."""
import Systerm
import builtins
import os

from copy import deepcopy

# Log formats
formats: dict = dict(
	Systerm = "[%(name)s] %(msg)s",
	basic = "%(msg)s",
)

# BaseLogger class
class BaseLogger(object):
	"""Low level logging."""
	def __init__(self, format: str=formats["basic"]) -> None:
		self.format = format

	def log(self, **keys):
		"""Logs values to the stream."""
		print(self.format % keys)
	
	def listen(self, **keys):
		"""Listens for an input in the stream."""
		return input(self.format % keys)

# Logger class
class Logger(BaseLogger):
	"""The main logging class for Systerm."""
	def __init__(self, name: str, format: str=formats["Systerm"], **keys) -> None:
		self.name = name
		self.format = format
		self.keys = keys
		self.keys["name"] = name

	def log(self, msg: str) -> None:
		"""Logs a message to the stream."""
		keys = deepcopy(self.keys)
		keys["msg"] = msg
		print(self.format % keys)
	
	def listen(self, msg: str) -> str:
		"""Listens for an input in the stream."""
		keys = deepcopy(self.keys)
		keys["msg"] = msg
		return input(self.format % keys)

# ConsoleMod
class ConsoleMod(Systerm.module.Module):
	"""Module class for Systerm.console."""
	send = write = print = builtins.print
	scan = input = builtins.input

	def call(self, command: str) -> int:
		"""Execute a command in a subshell."""
		return os.system(command)

Systerm.module.modules[__name__].__class__ = ConsoleMod

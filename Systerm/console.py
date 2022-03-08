"""Console is used for interpreting the stream"""
import Systerm
import builtins
import sys
import os

from copy import deepcopy

@Systerm.module.add(__name__)
class ConsoleMod(Systerm.Module):
	"""Module class for Systerm.console"""
	def write(self, value: object) -> None:
		"""Writes a value to the stream"""
		sys.stdout.write(str(value))
# Log formats
formats: dict = dict(
	Systerm = "[%(name)s] %(msg)s",
	basic = "%(msg)s",
)

# BaseLogger class
class BaseLogger(object):
	"""Low level logging"""
	
	def __init__(self, format: str=formats["basic"]) -> None:
		self.format = format

	def log(self, **keys):
		"""Logs values to the stream"""
		print(self.format % keys)
	
	def listen(self, **keys):
		"""Listens for an input in the stream"""
		return input(self.format % keys)
	
	def scan(self, prompt: Any) -> str:
		"""More like input but simpler"""
		self.send(prompt)
		for line in sys.stdin:
			return line.strip()
		
	def call(self, command: str) -> int:
		"""Execute a command in a subshell"""
		return os.system(command)

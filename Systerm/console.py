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
	
	def flush(self) -> None:
		"""Forces to flush the buffer"""
		sys.stdout.flush()
	
	def send(self, value: object) -> None:
		"""More like print but simpler"""
		self.write(value)
		self.flush()
	
	def scan(self, prompt: Any) -> str:
		"""More like input but simpler"""
		self.send(prompt)
		for line in sys.stdin:
			return line.strip()
		
	def call(self, command: str) -> int:
		"""Execute a command in a subshell"""
		return os.system(command)

"""Console is used for interpreting the stream"""
import Systerm
import sys

@Systerm.module.add(__name__)
class ConsoleMod(Systerm.Module):
	"""Module class for Systerm.console"""
	def write(self, value: object) -> None:
		"""Writes a value to the stream"""
		sys.stdout.write(str(value))
	
	def flush(self) -> None:
		"""Forces to flush the buffer"""
		sys.stdout.flush()
	
	def send(self, value: object) -> None:
		"""More like print but simpler"""
		self.write(value)
		self.flush()

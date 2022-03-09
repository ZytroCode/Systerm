"""Exit is a module from Systerm that manages everything on exit"""
import Systerm
import sys
import atexit

# ExitMod
class ExitMod(Systerm.module.Module.super(atexit)):

	"""Module class for Systerm.Exit"""
	def __call__(self, msg=None):
		self.exit(msg)

	@staticmethod
	def exit(self, msg=None):
		sys.exit(msg)
	
	@atexit.register
	@staticmethod
	def _() -> None:
		if Systerm.get_installed():
			Systerm.uninstall()

Systerm.module.modules[__name__].__class__ = ExitMod

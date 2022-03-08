"""Exit is a module from Systerm that manages everything on exit"""
import Systerm
import sys
import atexit

# ExitMod
class ExitMod(Systerm.module.Module.super(atexit).__class__):
	"""Module class for Systerm.Exit"""
	def exit(self, msg=None):
		sys.exit(msg)
	
	@atexit.register
	def _at_exit() -> None:
		if Systerm.get_installed():
			Systerm.uninstall()
	
	def __call__(self, msg=None):
		self.exit(msg)

del atexit

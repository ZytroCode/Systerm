"""Exit is a module from Systerm that manages everything on exit"""
import Systerm
import sys
import atexit

# ExitMod
@Systerm.module.add(__name__)
@Systerm.instance.super(atexit)
class ExitMod(Systerm.Module):
	"""Module class for Systerm.Exit"""
	def exit(self, msg=None):
		sys.exit(msg)

del atexit

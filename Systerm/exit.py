"""Exit is a module from Systerm that manages everything on exit."""
import atexit
import sys

import Systerm

# Uninstall Systerm on exit
@atexit.register
def _():
	try:
		Systerm.uninstall()
	except AttributeError:
		pass

# ExitMod class
class ExitMod(Systerm.module.Module.super(atexit)):
	__call__ = exit = sys.exit

Systerm.module.modules[__name__].__class__ = ExitMod

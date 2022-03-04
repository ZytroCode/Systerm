"""Exit is a module from Systerm that manages everything on exit"""
import Systerm

# ExitMod
@Systerm.module.add(__name__)
@Systerm.instance.super(atexit)
class ExitMod(Systerm.Module):
	"""Module class for Systerm.Exit"""

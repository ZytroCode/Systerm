"""Version contains the version of Systerm
This can also be used to create a version of something of yours"""
import Systerm

# VersionMod
@Systerm.module.add(__name__)
class VersionMod(Systerm.Module):
	"""Module class for Systerm.version"""
	# Version
	class Version():
		"""Class for an object to store a version"""
		def __init__(self, version):
			self.version = version
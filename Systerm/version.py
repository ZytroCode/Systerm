"""Version contains the version of Systerm
This can also be used to create a version of something of yours"""
import Systerm

# VersionMod
class VersionMod(Systerm.module.Module):
	"""Module class for Systerm.version"""
	# Version
	class Version(object):
		"""Class for an object to store a version"""
		def __init__(self, version: str) -> None:
			self.version: str = version

		def __str__(self) -> str:
			return self.version

		def __int__(self) -> int:
			return int(self.version.replace(".", ""))

		def __iter__(self) -> iter:
			for i in self.version.split("."):
				yield i

		@property
		def major(self) -> str:
			return list(self)[0]

		@property
		def minor(self) -> str:
			return list(self)[1]

		@property
		def micro(self) -> str:
			return list(self)[2]

	version: str = Version("0.3.0")
	__version__: str = Version("0.3.0")

	def __getattr__(self, name: str) -> object:
		try:
			return super().__getattr__(name)
		except Exception as e:
			try:
				return getattr(self.version, name)
			except AttributeError:
				raise e

	def __str__(self) -> str:
		return self.version.__str__()

	def __int__(self) -> int:
		return self.version.__int__()

	def __iter__(self) -> iter:
		return self.version.__iter__()

Systerm.module.modules[__name__].__class__ = VersionMod

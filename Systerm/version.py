"""Version is a module that manages a version of something"""
import Systerm

# Version class
class Version(object):
	"""Class for an object to store a version.

	Attributes:
		version - str:	The version of something
	"""
	__str__ = lambda self:self.version
	__int__ = lambda self:int(self.version.replace(".", ""))

	def __init__(self, version: str) -> None:
		"""The constructor for the Version class.

		Parameters:
			version - str:	The version of something
		"""
		self.version: str = version

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

# VersionMod class
class VersionMod(Systerm.module.Module):
	__version__ = version = Version("0.3.0")
	__str__ = lambda self:self.version.__str__
	__int__ = lambda self:self.version.__int__
	__iter__ = lambda self:self.version.__iter__

	def __getattr__(self, name: str) -> object:
		try:
			return super().__getattr__(name)
		except Exception as e:
			try:
				return getattr(self.version, name)
			except AttributeError:
				raise e

Systerm.module.modules[__name__].__class__ = VersionMod

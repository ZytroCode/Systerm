"""Instance is used for managing instances and classes"""
import Systerm

# InstanceMod
@Systerm.module.add(__name__)
class InstanceMod(Systerm.Module):
	"""Module class for Systerm.instance"""
	# Super function
	def super(instance):
		"""Inherits an instance to a class"""
		def wrapper(cls):
			for attr in dir(instance):
				setattr(cls, attr, getattr(instance, attr))
			return cls
		return wrapper

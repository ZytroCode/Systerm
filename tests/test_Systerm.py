def test_main():
	import Systerm
	Systerm.install()

	assert Systerm.version
	assert Systerm.Metaclass
	assert Systerm.get_installed(), "Systerm was not installed correctly"

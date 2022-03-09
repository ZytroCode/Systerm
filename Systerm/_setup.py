"""Used to avoid circular import."""
def init_meta():
	from Systerm import meta
	return meta

def init_module():
	from Systerm import module
	return module

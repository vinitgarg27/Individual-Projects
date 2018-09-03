class Error(Exception):
	"""
		Base class for other exceptions
	"""
	pass

class ErrorInvalidPath(Error):
	"""
		Raised when invalid path is given while operations
	"""
	pass

class ErrorInvalidCommand(Error):
	"""
		Raised when invalid command is entered
	"""
	pass

class ErrorDirectoryAlreadyExists(Error):
	"""
		Raised when user tries to create an already existing directory
	"""
	pass

class ErrorCannotRemoveCurrDir(Error):
	"""
		Raised when user tries to delete the current directory
	"""
	pass

class ErrorEnterPressed(Error):
	"""
		Raised when enter is pressed
	"""
	pass
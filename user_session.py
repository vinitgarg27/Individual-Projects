class directory_structure(object):
	"""
		this the structure of every directory
		has a name and list of child directories 
	"""
	def __init__(self, filename):
		self.name = filename
		self.child_nodes = []


class user_session(object):
	"""
		this class maintains the session of user like its current directory and current path
	"""
	def __init__(self):
		"""
			create new user session with root directory
			all private variables
		"""
		self.__root_dir = directory_structure("/")  ## maintains the directory structure
		self.__curr_dir_path = [self.__root_dir]
		self.__curr_file_dir = self.__root_dir

	def get_root_directory(self):
		"""
			returns the root directory of user
		"""
		return self.__root_dir

	
	def get_current_file_directory(self):
		"""
			returns the current directory of user
		"""
		return self.__curr_file_dir


	def get_current_file_directory_path(self):
		"""
			returns the path from root to current directory the user is on
		"""
		return self.__curr_dir_path


	def update_curr_dir_path(self, updated_path):
		"""
			updates the current user session path and also updates the current directory, which is the last
			directory in the path
		"""
		self.__curr_dir_path = updated_path
		self.__curr_file_dir = self.__curr_dir_path[-1]


	def reset_session(self):
		"""
			this resets the user session to root as if new user session has created
		"""
		self.__root_dir = directory_structure("/")
		self.__curr_dir_path = [self.__root_dir]
		self.__curr_file_dir = self.__root_dir


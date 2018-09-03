import sys
sys.path.append(".")
from user_session import user_session
from util_functions import *
from error import *

class handle_user_session(object):
	def __init__(self):
		""" 
			creates a ner user session when on creation of this object
		"""
		self.session = user_session()


	def get_user_session(self):
		"""
			Returns the session of the the user
		"""
		return self.session

	
	def update_user_session(self, updated_user_session_obj):
		"""
			This updates the session of an user which is updated by the command handler
		"""
		self.session = updated_user_session_obj


	def print_comlete_directory_structure(self):
		"""
			Helper func which can be used for debugging purposes.
			This prints the complete directory structure starting from root
		"""
		user_session_obj = self.get_user_session()
		root_file_obj = user_session_obj.get_root_directory()
		queue = [(None, root_file_obj)]
		prev_parent_name = None
		# sys.stdout.write("/ : ")
		while(queue):
			(parent_name, front) = queue.pop(0)
			if(parent_name == prev_parent_name):
				## print at same level
				sys.stdout.write("{} ".format(front.name))
				
			else:
				prev_parent_name = parent_name
				sys.stdout.write("\n")
				sys.stdout.write("{} : ".format(parent_name))
				sys.stdout.write("{} ".format(front.name))
				
			for each_child in front.child_nodes:
					queue.append((front.name, each_child))
		sys.stdout.write("\n")



import sys
sys.path.append(".")
from user_session import user_session, directory_structure
from error import *
from util_functions import *

class command_handler(object):
	"""
	this class handles the basic validation of commands and execution of it
	"""
	def __init__(self):
		self.possible_commands_names = ['cd', 'pwd', 'rm', 'ls', 'mkdir', 'session clear'] ## just for showing
		self.possible_commands = ['cd', 'pwd', 'rm', 'ls', 'mkdir', 'session']
		self.commands_with_operands = ['cd', 'rm', 'mkdir', 'session']
		self.stand_alone_commands = ['pwd', 'ls']


	def validate_command(self, input_stream):
		"""
			This func validates the user input and performs basic checks like
			if correct commands are given as input by an user
		"""
		if(input_stream == ""):
			raise ErrorEnterPressed
		split_command = input_stream.split(" ")
		command = split_command[0]
		if(command in self.possible_commands):
			if(command in self.stand_alone_commands and len(split_command)<=1):
				return command, split_command[1:]

			elif(command in self.commands_with_operands and len(split_command)>1):
				return command, split_command[1:]
		raise ErrorInvalidCommand

	def get_possible_commands(self):
		"""
			This func return the list of possible commands which a user can input
		"""
		return self.possible_commands_names


	def execute_command(self, input_stream, new_user_session_manager_obj):
		"""
			This functions does the core part i.e executing the input commands and thereby changing the
			state of the user session.

			Every command makes initial checks if the user has given the absolute path or relative path
		"""
		command, command_operands = self.validate_command(input_stream)
		user_session_obj = new_user_session_manager_obj.get_user_session()
		if (command == 'cd'):
			each_command_operand = command_operands[0]
			if(each_command_operand != ''):
				if(each_command_operand[0] == '/'):
					"""
						Below 3 lines extrates the directory name from the path given by user
						for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
					"""
					splitted_path = each_command_operand.split("/")[1:]
					filtered_path = remove_white_spaces(splitted_path)
					root_file_obj = user_session_obj.get_root_directory()
					new_path = self.change_directory(filtered_path, root_file_obj, [root_file_obj])
					user_session_obj.update_curr_dir_path(new_path)
					
				else:
					"""
						Below 3 lines extrates the directory name from the path given by user
						for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
					"""
					splitted_path = each_command_operand.split("/")
					filtered_path = remove_white_spaces(splitted_path)
					curr_file_obj = user_session_obj.get_current_file_directory()
					new_path = self.change_directory(filtered_path, curr_file_obj, [])
					updated_path = user_session_obj.get_current_file_directory_path() + new_path
					user_session_obj.update_curr_dir_path(updated_path)
				# self.print_current_directory_path()
				print("SUCC: REACHED")


		elif(command == 'mkdir'):
			"""
				NOTE: currently handling only creation of one directory per command execution
				i.e. mkdir /a /b /c will only create '/a' as a new directory
			"""
			if(command_operands != []):
				each_command_operand = command_operands[0]
				if(each_command_operand != ''):
					if(each_command_operand[0] == '/'):
						"""
							Below 3 lines extrates the directory name from the path given by user
							for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
						"""
						root_file_obj = user_session_obj.get_root_directory()
						splitted_path = each_command_operand.split("/")[1:]
						filtered_path = remove_white_spaces(splitted_path)
						self.make_new_directory(filtered_path, root_file_obj, user_session_obj)
					else:
						"""
							Below 3 lines extrates the directory name from the path given by user
							for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
						"""
						curr_fild_obj = user_session_obj.get_current_file_directory()
						splitted_path = each_command_operand.split("/")
						filtered_path = remove_white_spaces(splitted_path)
						self.make_new_directory(filtered_path, curr_fild_obj, user_session_obj)
					print("SUCC: CREATED")
					# self.print_comlete_directory_structure()


		elif(command == "rm"):
			"""
				This command removes the directory
			"""
			if(command_operands != []):
				each_command_operand = command_operands[0]
				if(each_command_operand != ''):
					if(each_command_operand[0] == '/'): ## absolute path given
						"""
							Below 3 lines extrates the directory name from the path given by user
							for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
						"""
						root_file_obj = user_session_obj.get_root_directory()
						splitted_path = each_command_operand.split("/")[1:]
						filtered_path = remove_white_spaces(splitted_path)
						self.remove_directory(filtered_path, root_file_obj, user_session_obj)
					else: ## relative path given
						"""
							Below 3 lines extrates the directory name from the path given by user
							for ex : '/a/b/c/' => ['a', 'b', 'c'], this list travesed
						"""
						curr_file_obj = user_session_obj.get_current_file_directory()
						splitted_path = each_command_operand.split("/")
						filtered_path = remove_white_spaces(splitted_path)
						self.remove_directory(filtered_path, curr_file_obj, user_session_obj)
					print("SUCC: DELETED")
		

		elif(command == "pwd"):
			"""
				This command prints the current working directory of user
			"""
			curr_dir_path = user_session_obj.get_current_file_directory_path()
			sys.stdout.write("PATH: ")
			for each in curr_dir_path:
				if(each.name == '/'):
					sys.stdout.write("{}".format(each.name))
				else:
					sys.stdout.write("{}/".format(each.name))
			sys.stdout.write("\n")


		elif(command == "ls"):
			"""
				This command lists out the directories in current directory
			"""
			curr_file_obj = user_session_obj.get_current_file_directory()
			sys.stdout.write("DIRS: ")
			for each in curr_file_obj.child_nodes:
				sys.stdout.write("{} ".format(each.name))
			sys.stdout.write("\n")


		elif(command == "session"):
			"""
				This command combines with "clear" to reset the user session to root('/')
				if "session unknow_command" is given, then nothing will happen 
			"""
			if(command_operands != []):
				each_command_operand = command_operands[0]
				if(each_command_operand == "clear"):
					user_session_obj.reset_session()
					print("SUCC: CLEARED: RESET TO ROOT")
				else:
					raise ErrorInvalidCommand

		new_user_session_manager_obj.update_user_session(user_session_obj)


	def make_new_directory(self, splitted_path, curr_file_obj, user_session_obj):
		"""
			This func creates a new directory.
			input format:
			1. 
				if absolute path given, then
					splitted_path: ['/from/to/dir_to_create']
				
				if relative path given
					splitted_path: ['from/to/dir_to_create']

			2. curr_file_obj is the root object or current directory object based on the path requested by user

			Logic:
				If while traversing the path given in splitted_path, 2 cases to handle:
				1. if it doesn't encounter the file obj, then it checks if it's the last file in path, if it
					is then a new directory object is created by this file name; else error is returned as 
					invalid path.
				2. if it encounter's the file obj, then it checks if it has more directory to traverse,
					if more directory to traverse then keep on travering until point 1 encounters;
					otherwise, error is returnes as already directory exists.
		"""
		try:
			n = len(splitted_path)
			for i in range(n):
				## if splitted_path[i] is not part of node but i+1 exists, then error
				found_file_obj = check_if_file_system_object_exists(splitted_path[i], curr_file_obj.child_nodes)
				if(found_file_obj is not None):
					if(i+1 == n):  ## if file object exists and doesn't have next dir, then user trying to create same dir
						raise ErrorDirectoryAlreadyExists
					else:
						curr_file_obj = found_file_obj
				else:
					if(i+1 == n):
						## create node
						new_file_obj = directory_structure(splitted_path[i])
						curr_file_obj.child_nodes.append(new_file_obj)
					else:  ## intermediate dir given is not valid
						raise ErrorInvalidPath
		except RuntimeError:
			raise RuntimeError


	def change_directory(self, splitted_path, curr_file_obj, base_path):
		"""
			This func changes the current directory.
			input format:
			1. splitted_path:
				if absolute path given, then
					splitted_path: ['/from/to/dir_to_change']
				
				if relative path given
					splitted_path: ['from/to/dir_to_change']

			2. curr_file_obj : it is the root object or current directory object based on the path requested by user
			3. base_path :
				if absolute path given, then
					base_path: [root_file_object]
				
				if relative path given
					base_path: []

			Logic:
				if while traversing the splitted_path at any moment if it doesn't encounter the directory object
				in path, then error is return as invalid path; otherwise current path is changed
		"""
		n = len(splitted_path)
		for i in range(n):
			found_file_obj = check_if_file_system_object_exists(splitted_path[i], curr_file_obj.child_nodes)
			if(found_file_obj is not None):
				# new_path.append(found_file_obj)
				base_path.append(found_file_obj)
				curr_file_obj = found_file_obj
			else:
				raise ErrorInvalidPath
		return base_path


	def remove_directory(self, splitted_path, curr_file_obj, user_session_obj):
		"""
			This func removes the directory requested by user.
			Its Behaviour:
				if user is in path /a/b/c and gives the command "rm /a/", then the directory wil get deleted but
				the "pwd" command will give /a/b/c which is the Linux behaviour


			input format:
			1. splitted_path:
				if absolute path given, then
					splitted_path: ['/from/to/dir_to_change']
				
				if relative path given
					splitted_path: ['from/to/dir_to_change']

			2. curr_file_obj : it is the root object or current directory object based on the path requested by user
			3. base_path :
				if absolute path given, then
					base_path: [root_file_object]
				
				if relative path given
					base_path: []

			Logic:
				while traversing the splitted_path, 2 cases possible
				1. if a directory is encounter while traversing, then it checks if further directory to traverse
					in path, if not then it checks the user's current directory, if both are same then error is
					returned as cannot remove current directory; else that directory is deleted
				2. if at any time directory is not encountered then error is returned as invalid path
		"""
		current_file_dir = user_session_obj.get_current_file_directory()
		n = len(splitted_path)
		for i in range(n):
			found_file_obj = check_if_file_system_object_exists(splitted_path[i], curr_file_obj.child_nodes)
			if(found_file_obj is not None):
				if(i+1==n):  ## directory to be removed
					if(current_file_dir != found_file_obj):  ## check if it's not current directory
						curr_file_obj.child_nodes.remove(found_file_obj)
					else:
						raise ErrorCannotRemoveCurrDir
				else:
					curr_file_obj = found_file_obj
			else:
				raise ErrorInvalidPath


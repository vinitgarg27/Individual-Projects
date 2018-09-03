import sys
import traceback
sys.path.append(".")
from error import *
from user_session import user_session, directory_structure
from util_functions import *
from command_handler import command_handler
from manage_user_session import handle_user_session


def initiate_application(command_handler_obj):
	print("<Starting your application...>\nTo Exit this session press Ctrl + D\n")
	print("Below are the possible commands supported for this session.")
	print(command_handler_obj.get_possible_commands())
	print("\n")

if __name__ == "__main__":
	"""
		1. creates a new user session object as new_user_session_obj which executes the command
		2. creates a command handler object as command_handler_obj which handles the user input validation
	"""
	new_user_session_manager_obj = handle_user_session()
	command_handler_obj = command_handler()
	initiate_application(command_handler_obj)
	while True:
	    try:
	    	## take input from user
	        input_stream = raw_input()
	        ## splits this user input into command and its operands to perform operations
	        command_handler_obj.execute_command(input_stream, new_user_session_manager_obj)
	        sys.stdout.write("\n")

	    except EOFError:
	    	print("Normally Exited Application")
	        break

	    except ErrorInvalidCommand:
	    	print("ERR: CANNOT RECOGNIZE INPUT \n")

	    except ErrorInvalidPath:
	    	print("ERR: INVALID PATH \n")

	    except ErrorDirectoryAlreadyExists:
	    	print("ERR: DIRECTORY ALREADY EXISTS \n")

	    except ErrorCannotRemoveCurrDir:
	    	print("ERR: CANNOT REMOVE CURRENT DIRECTORY \n")

	    except ErrorEnterPressed:
	    	pass

	    except RuntimeError:
	    	print("ERR: RUNTIME ERROR OCCURED. PLEASE CHECK YOUR INPUT \n")
	    	

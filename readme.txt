This small project handles the basic linux command operation like 
'cd', 'pwd', 'rm', 'ls', 'mkdir', 'session clear'.


NOTE:
	Currently above operations are ONLY valid for directories, but can be extended to accomodate for file as well.


CODE STRUCTURE:
	mainly 2 class has been used which command_handler and handle_user_session.
	1. command_handler class is responsible for execution and validation of commands.
	2. handle_user_session class is responsible for maintaining the current user session.
	

DATA STRUCTURES USED:
	n-ary tree is used for storing the complete structure of the user session where each tree node repesents the directory info which can have 'n' children.

	For maintaining the current path, an array of objects is used which on iterating gives the path of current directory.


HOW TO RUN ?
	simply open the terminal and run "python main.py" which will start the application. Currently this has been tested on python version 2.7, not sure if it will have any issue with python version >= 3


IMPROVEMENTS:
	1. for each command a class can be made which will handle the execution of each commands.
def check_if_file_system_object_exists(name, file_obj_list):
	"""
		This function itreates over the file_obj_list and checks if name exists or not
	"""
	for file_obj in file_obj_list:
		if(name == file_obj.name):
			return file_obj
	return None


def remove_white_spaces(arr):
	"""
		this fun removes unnecessary element from arr list which is created while splitting the
		inout user data
	"""
	new_arr = []
	for each in arr:
		if(each != ""):
			new_arr.append(each)
	return new_arr
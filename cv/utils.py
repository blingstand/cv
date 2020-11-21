def get_projects(nb):
	#return a dict like dict[line]=(value1, value2 ...)
	dict_to_return = {}
	dict_to_return['line1'] = []
	dict_to_return['line2'] = []
	dict_to_return['line3'] = []
	dict_to_return['line4'] = []
	for i in range(1, nb): 
		if i <= 4:
			dict_to_return['line1'].append(f"projet {i}")
		elif i <= 8:
			dict_to_return['line2'].append(f"projet {i}")
		elif i <= 12:
			dict_to_return['line3'].append(f"projet {i}")
		elif i <= 16:
			dict_to_return['line4'].append(f"projet {i}")
	return dict_to_return
		


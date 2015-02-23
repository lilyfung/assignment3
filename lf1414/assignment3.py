#Question 1
#To locate the file that os.path.abspath function is defined in:

import os
os.path.abspath??

#Type:	function
#String form: <function abspath at 0x01D0A1B0>
#File:	c:\users\mslil_000\anaconda\lib\ntpath.py
#Definition: os.path.abspath(path)
#Source:
	def abspath(path):
	""Returns the absolute version of a path.""

	if path: #Empty path must return current working directory.
		try:
			path = _getfullpathname(path)
		except WindowsError:
			pass # Bad path - return unchanged
	elif isinstance(path, unicode):
		path = os.getcwdu()
	else:
		path = os.getcwd()
	return normpath(path)


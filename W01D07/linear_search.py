x = ['A','B','C','D','E','F']
KEY = 'G'

for item in x:
	if item == KEY:
		print('Found the element')
		break
else:
	print('Did not found the element')
slrFile = open('slr.html', 'r')


while True:
	line = slrFile.readline()
	# End of file
	if line == '':
		break
	# Start a row
	if '<tr>' in line:
		

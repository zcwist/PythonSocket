import re


file = open("OriginalScriptEn.log","r")
output = open('PresolvedEnScript.log', 'w')

lines = file.readlines()

for x in range(0,len(lines)-1,1):
	line = lines[x]
	line = line[:-1]

	pattern = re.compile(r'^\d+\.')

	# match = pattern.search(line) 
	# if match:
	# 	print(pattern.sub('',line))

	line =  pattern.sub('',line)

	# if re.match("+{\d}",line):
	# 	print (line)

	# if line[-1] == '\b\n':
	# 	line = line[0:-1]
	# print (line)
	try:
		if line[0] == '!':
			if line[1] == ' ':
				line = ' #' + line[2:] + '# '
			else:
				line = ' #' + line[1:] + '# '
	except BaseException:
		pass


	

	# print (line)
	output.write(line)

	if re.match("\d",lines[x+1]):
		output.write("\r\n")

	
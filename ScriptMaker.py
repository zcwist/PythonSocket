import re

file = open("OriginalScript.log","r")
output = open('PresolvedScript', 'w')


for line in file:
	if re.match("\d",line):
		
		flag = 0;
		while (line.find("#",flag)!=-1):
			s = line.find("#",flag)
			# output.write("!")
			output.write(line[flag:s] + "\r\n")
			flag = s + 1
			s = line.find("#",flag)
			output.write("!")
			output.write(line[flag:s] + "\r\n")
			flag = s + 1
		output.write(line[flag:-1] + "\r\n")
		
